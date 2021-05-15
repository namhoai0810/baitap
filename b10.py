# 10. Write a function f() so that we can have the output above
def f(x):
    list_num = []
    for item in range(0, x):
        list_num.append(pow(item, 3))
    return list_num

for x in f(5):
    print(x)