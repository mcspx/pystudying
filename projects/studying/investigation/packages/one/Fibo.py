__author__ = 'rpm'
def fibo(num) :
    a = 0
    b = 1
    result = []
    while a < num :
        result.append(b)
        a, b, = b, b + a

    return result