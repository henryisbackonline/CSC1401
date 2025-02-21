def simple_rj(s):

##### SIMPLIFIED RIGHT JUSTIFY FUNCTION #####

    """
    Summary:
        simple_rj takes an input string and adds space characters to the start.
        The result is 70 characters long, with the final character of the input string in the 70th column.
    Parameters:
        s (str) -> input string        
    """
    space=' '                   
    result=(70-len(s))*space+s   
    print(result)

# The function works this way:

#   1. Define the variable 'space' as a single whitespace character

#   2. Define the variable 'result':
#     a. First, 70 minus the length of argument 's' (the input string) is calculated. This gives the number of spaces to appear at the start of the result.
#     b. Then, multiply 'space' by the result of 70-(len(s)). This is string repetition. Recall that multiplying strings concatenates them - 'h'*5 results in 'hhhhh'
#     c. Finally, add the argument 's' to the end of the spaces. Recall that this will not print 's' as a string, but rather the input from 's'. 

#   3. Print the output of the function 'result'