# 2. How to translate a string containing a binary code (1 and 0) into a number (integer)? Write a function to do this.
# Hàm trả về số nguyên truyển từ số nhị phân
def convert_FromBin_ToDectdecimal(bin):
    dectdecimal = int(bin,2)
    return dectdecimal

if __name__ == '__main__':
    number = convert_FromBin_ToDectdecimal("1101")
    print(number)