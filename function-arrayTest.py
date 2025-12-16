num1 = 4
num2 = 19

def addStuff():
    result = (num1 + num2)
    return result

print(addStuff())


bearTypes = ['black', 'grizzly', 'sun', 'polar', 'koala', 'teddy', 'brown', 'panda', 'cinnamon']

for i in bearTypes:
    print('{} bear!'.format(i))

print(bearTypes.count('panda'))
bearTypes.sort(reverse = True)
print(bearTypes)
