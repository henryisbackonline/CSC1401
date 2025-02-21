def right_justify(s):
   
   ##### COMPLEX RIGHT JUSTIFY FUNCTION #####

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
    output = "" # output is empty at this stage. this is because the characters need to be added to output first. the result of output will be redefined later in the function
    stringlength = len(s)
    outputlength = 70-stringlength

    for i in range(outputlength):
        output += " "
        # '+=' is a modifier that performs string concatenation. 
        # it iterates over the string and appends the value: + the new value to the previous string, = the result of the addition to the variable
        #
        # the for loop is what repeats the process. Loop works like this:
        #    1: Take the range of the output length (in this case, 70 minus the length of the input string) and use this value as the range for the loop
        #    2: Concatenate a whitespace to the output 
        #    3: let the output equal the new concatenated value
        #    4: Loop finished. Haed back to the start having completed one loop of the total umber (range) of loops.
        #    5: Repeat until range is exhaused 
    
    output += s
    # '+=' here takes the concatenated whitespace string and appends the input string to the whitespace string

    print(output) # this is the final stap of the function
                  # output has been redefined as (number of space characters defined by outputlength) + s (the input string from right_justify)
                  # printing this concatenated output reveals text that is "justified" to column 70