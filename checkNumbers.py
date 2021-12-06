#Check if the first and last number of a list is the same


def check(givenList):
    print("given list:", givenList)

    first = givenList[0]
    second = givenList[-1]

    if first == second:
        return True
    else:
        return False


numbers_x = [10, 20, 30, 40, 10]
print("result is ", check(numbers_x))

numbers_y = [10, 20, 30, 40, 11]
print("result is ", check(numbers_y))
