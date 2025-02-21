def right_justify(s):
    """
    Summary:
        right_justify takes an input string and adds space characters to the start.
        The result is 70 characters long, with the final character of the input string in the 70th column.

    Parameters:
        s (str) - input string
        stringlength (int) - length of input string
        outputlength (int) - lenth of output string
        output(str) - output string
    """
    output = ""
    stringlength = len(s)
    outputlength = 70-stringlength

    for i in range(outputlength):
        output += " "
    
    output += s

    print(output)