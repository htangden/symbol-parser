import symbol
import plot
import numpy as np
import code

def main():

    banner = "\n--- WELCOME to SymPlot REPL! ---\nFor instructions, run 'help()'\n"

    x = symbol.Symbol()
    frame = plot.Frame()


    repl_locals = {
        'x': x,
        'frame': frame,
        'Symbol': symbol.Symbol,
        'Frame': plot.Frame,
        'help': lambda: print("\nCreate variable (x already available): t = Symbol()\nCreate functions: f = 3*x + e**x\nCreate frame (frame aldready available): fr = Frame()\nAdd functions to frame: frame + f\nCreate plot: frame.plot([x_start, x_end])\n"),
        'e': np.e,
    }

    code.interact(banner=banner, local=repl_locals)

if __name__ == "__main__":
    main()

