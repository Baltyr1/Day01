"ex 11"
def FizzBuzz():
    for i in range(1, 101):
        if i%3 == 0 and i%5 != 0:
            print('Fizz')
        if i%5 == 0 and i%3 != 0:
            print('Buzz')
        if i%3 == 0 and i%5 == 0:
            print('FizzBuzz')
        else:
            print(i)
print(FizzBuzz())