from time import sleep
def fibonacci(fn1, fn2):
    sleep(.3)
    fn3 = fn1 + fn2
    print(fn3)
    fibonacci(fn2, fn3)



def main():
    print('0')
    print('1')
    fibonacci(0, 1)


if __name__ == '__main__':
    main()
