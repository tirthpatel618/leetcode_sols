def fizzBuzz(n):
    for i in range(n+1):
        returnstr = ""

        if i % 3 == 0:
            returnstr += "Fizz"
        if i % 5 == 0:
            returnstr += "Buzz"
        if returnstr:
            print(returnstr)
        else:
            print(i)

fizzBuzz(15)