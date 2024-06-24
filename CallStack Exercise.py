# Write your code here :-)
def a():
    print("a() starts")
    b()#calls and finishes
    d()#calls and finishes
    print("a() returns")


def b():
    print("b() starts")
    c()#calls and finishes
    print("b() returns")


def c():
    print("c() starts")
    print("c() returns")


def d():
    print("d() starts")
    print("d() returns")


a()#should run all methods
b()#should only run b and c
c()#should only run c
d()#should only run d
