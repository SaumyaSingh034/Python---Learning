import argparse

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
        return a

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("num", help = "The Fibonnaci number "+  \
                                "You wish to calculate", type = int)
    parser.add_argument("-o","--output", help = "Output the result to a file", action ="store_true")
    args = parser.parse_args()
    result = fib(args.num)
    print("The "+str(args.num)+"th has fib no = "+str(result))

    if args.output:
        f = open("Fibonacci.txt", "a")
        f.write(str(result)+'\n')

if __name__ =="__main__":
    Main()
    
