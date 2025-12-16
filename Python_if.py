


#num1 = 12
#key = False

#if num1 == 12:
#    if key:
#        print('Num1 is equal to Twelve and they have the key!')
#    else:
#        print('Num1 is equal to Twelve and they do NOT have the key!')
#elif num1 < 12:
#    print('Num1 is less than Twelve!')
#else:
#    print('Num1 is NOT equal to Twelve!')

num2 = 11
num3 = 10
fudge = False

if (num2 * num3) == 110:
    if num3 < 11:
        if not fudge:
            print('Multiplier is less than 11 without fudge.')
        else:
            print('Multiplier is less than 11 with fudge.')
    else:
        print('Equals 110!')
elif (num2 * num3) < 100:
    print('Less than 100.')
else:
    print('Greater than 110.')

bool(fudge)
bool(num3)
