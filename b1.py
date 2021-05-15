#1. Write a function that produces the Fibonacci sequence.
# Hàm trả dãy fibonacci ở vị trí 1 đến vị trí thứ n
def fibonacci(n):
    f0 = 0;
    f1 = 1;
    fn = 1;
    sb = "0, 1, "
    if (n < 0):
        sb = "-1"
        
    if (n == 0):
        sb = "0"
    if(n == 1):
        sb = "0, 1, "
    else:
        for i in range(2, n):
            f0 = f1;
            f1 = fn;
            fn = f0 + f1;
            sb = sb + str(fn) + ", "
    
    return(sb)


if __name__ == '__main__':
    string_fibonacci = fibonacci(3)
    print(string_fibonacci)
    