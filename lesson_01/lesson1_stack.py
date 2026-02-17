def funcA():
    print("Начали выполнять A")
    funcB()
    print("Закончили выполнять A")

def funcB():
    print("Начали выполнять B")
    funcC()
    print("Закончили выполнять B")

def funcC():
    print("Начали выполнять C")
    print("Закончили выполнять C")


funcA()