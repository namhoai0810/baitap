
# Write a function that returns a string of numbers from 0 to 100, "0123456789101112...".
def returnform_0to100():
    string = ""
    for item in range(0,101):
        string = string + str(item)
    return string

if __name__ == '__main__':
    string_from0to100 = returnform_0to100()
    print(string_from0to100)