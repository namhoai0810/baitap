#8. Write a program that prints the numbers from 1 to 20. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers that are multiples of both three and five print “FizzBuzz”.
def print_numbers():
    string = ""
    for i in range(1,21):
        if(i % 3 == 0):
            string = string + "Fizz"
        if(i % 5 == 0):
            string = string + "Buzz"
        if(i % 3 != 0 and i % 5 != 0):
            string = string + str(i)
    return string

if __name__ == '__main__':
    string_num = print_numbers()
    print(string_num)