#Make a program that reads keyboard input and display type and all relevant information
inp = input('make a input via keyboard and press enter: ')
print('the input type is {0}  \n the input is a letter? {1} \n the input is in lower cases only? {2} \n the input is in upper cases only? {3} \n \
the input is numeric? {4} \n the input is decimal? {5} \n the input is a blank space? {6} \
        ' .format(type(inp),inp.isalpha(),inp.islower(),inp.isupper(),inp.isnumeric(),inp.isdecimal(),inp.isspace()))