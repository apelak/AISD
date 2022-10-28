def foo(x: int)->None:
    if x<0:
        return
    print(x)
    foo(x-1)


def fib(x: int) -> int:
    if x == 0 or x == 1:
        return 1

    return fib(x-1) + fib(x-2)


def power(number: int, n: int) -> int:
    if n == 1:
        return number
    return power(number, n-1) * number


def factional(n: int) -> int:
    if n==1:
        return 1
    return factional(n-1)*n


 def prime(n: int) -> bool:
     if n == 2:
         return True
     if n % 2 == 0 or n <= 1:
         return False

     for x in range(3, n):
         if n % x == 0:
             return False
     return True


foo(10)
print(fib(6))
print(power(2, 10))
print(factional(5))
print(prime(5))
print(prime(6))
