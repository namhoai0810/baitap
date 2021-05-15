def convert_String_toNumber(string):
    string_number = ""
    for item in range(0, len(string)): 
        string_number = string_number + str(ord(string[item]))
    
    return string_number

if __name__ == '__main__':
    string_number = convert_String_toNumber('abcd')
    print(string_number)