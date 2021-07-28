numberList = []
oddList = []
evenList = []

def OddAndEEven(numbers):
    inputValues = input("Enter values in a list seperating by a space: ")
    print('\n')
    numberList = inputValues.split()

    for i in range(len(numberList)):
        numberList[i] = int(numberList[i])

    for x in range(len(numberList)):
        if (numberList[x] < 0 or numberList[x] == 0):
            continue
        elif (numberList[x]%2) == 0:
            evenList.append(numberList[x])
        else:
            oddList.append(numberList[x])

OddAndEven(numberList)
print("The odd list: ", oddList)
print("The Even list: ", evenList)
