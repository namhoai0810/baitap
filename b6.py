def returnform_0to100():
    string = ""
    for item in range(0,101):
        string = string + str(item)
    return string

if __name__ == '__main__':
    string_from0to100 = returnform_0to100()
    print(string_from0to100)