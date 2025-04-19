def newline_matching(str1: str, str2: str):
    arr1 = str1.split("\n")
    arr2 = str2.split("\n")

    s = ""

    longest_arr1_element = len(max(arr1))

    len_operator_1 = len(arr1[0])-2
    len_operator_2 = len(arr2[0])-2
    length = max(len(arr1), len(arr2))

    for i in range(length):
        try:
            s += (arr1[i]) + " "*(longest_arr1_element-len(arr1[i]) + 1)
        except IndexError:
            s += " "*(longest_arr1_element+1)

        try:
            s += (arr2[i])
        except IndexError:
            s +=(" ")

        s += ("\n")

    return s, longest_arr1_element, len_operator_1, len_operator_2
