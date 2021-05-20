from blessed import Terminal

t = Terminal()

try:
    mynum = input('Give me a number: ')

    print(t.white(f"Type({mynum}) = {type(mynum)}"))

    if mynum.isnumeric():
        a = float(mynum)
        print(t.yellow(f"The number you entered is {a}"))
    else:
        print(t.white(f"The input: {mynum} is not a number"))

#  name = 'Amarjot'

    myname = input('What is your name: ')

    print(t.green(f'My name is {myname}'))

except Exception as error:
    print(t.green(error))
