import symbol
from symbol import Symbol
import numpy as np
from PIL import Image


class Frame:
    def __init__(self, name: str = "frame", size = [480, 720]):
        self.name = name
        self.functions: list = [] 
        self.size = size  
        self.axis_width = 3
        self.dead_space = 0.1

    def __add__(self, function):
        self.functions.append(function)

    def __sub__(self, function):
        try:
            self.functions.remove(function)
        except ValueError:
            print("No such function in frame.")

    def __repr__(self):
        return f"Frame-object. Current functions:\n{"\n".join([str(func) for func in self.functions])}"

    def plot(self, x_range: list[float]):

        image_array = np.zeros(self.size, dtype=np.uint8)
        
        if self.functions:
            function_values = self.get_function_values(x_range)
            image_array = self.plot_function_values(function_values, image_array)

        image_array = self.plot_axis(image_array)
        image = Image.fromarray(image_array, mode="L")
        image.show()

    def plot_axis(self, image_array: np.ndarray):
        left_most = round(self.size[1] * self.dead_space)
        top_most = round(self.size[0] * (1 - self.dead_space))
        for i in range(self.axis_width):
            image_array[:, left_most + i] = 255 
            image_array[top_most + i, :] = 255

        return image_array

    def get_function_values(self, x_range):
        values = []
        x_values = np.linspace(x_range[0], x_range[1], round(self.size[1] * (1 - self.dead_space)))
        for function in self.functions:
            values.append(list(function(x_values)))
        return values

    def plot_function_values(self, values : list[list[float]], image_array : np.ndarray):
        min_value = values[0][0]
        max_value = values[0][0]
        for func_vals in values:
            for value in func_vals:
                if value < min_value:
                    min_value = value
                elif value > max_value:
                    max_value = value

        for func_vals in values:
            for i, value in enumerate(func_vals):
                height = self.frac_to_index((value-min_value)/(max_value-min_value))
                image_array[height, i+round(self.size[1]*self.dead_space)] = 255
                try:
                    image_array[height-1, i+round(self.size[1]*self.dead_space)] = 127
                    image_array[height+1, i+round(self.size[1]*self.dead_space)] = 127
                except IndexError:
                    pass

        return image_array

    def frac_to_index(self, fraction : float):
        return round((1-fraction) * self.size[0] * (1-self.dead_space))

    
if __name__ == "__main__":
    x = Symbol()

    g = -5*x + 3**x
    g_prime = g.diff()

    fr = Frame([-1, 2])
    fr + g
    fr + g_prime
    fr.plot()