# 3. How to check that tuple A contains all elements of tuple B. Do both tuples contain unique values? Write a function to do this.

def check_Tuple(TupleA, TupleB):
    string = ""
    if((set(TupleA).issuperset(TupleB))):
        string = "Tuple A contains all elements of tuple B"
    if(len(TupleA) == len(set(TupleA)) and len(TupleB) == len(set(TupleB))):
        string = string + " both tuples contain unique values"
    else:
        string = "Tuple A is  not contains all elements of tuple B"
    return string

if __name__ == '__main__':
    tuple1 = (1, 2, 3, 4)
    tuple2 = (1, 2, 3, 4, 5)
    check = check_Tuple(tuple2, tuple1)
    print(check)