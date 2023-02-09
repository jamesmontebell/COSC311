numDots = 0
sumOdd = 0
sumEven = 0
for i in range(1, 21):
    numDots += i
    if(numDots % 2 == 0):
        sumEven += numDots
    else:
        sumOdd += numDots
    print('#' + str(i) + ': ' + str(numDots))
    
print('Sum of odd numbers: ' + str(sumOdd))
print('Sum of even numbers: ' + str(sumEven))

    
    