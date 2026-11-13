def main():
    print("Hello learners!")


def addmultiplenumbers(nums):
    total = 0

    for num in nums:
        total += num

    return total


def multiplymultiplenumbers(nums):
    result = 1

    for num in nums:
        result *= num

    return result


def isitaninteger(num):
    if isinstance(num, bool):
        return False

    if isinstance(num, int):
        return True

    if isinstance(num, float):
        return num.is_integer()

    return False


def isiteven(num):
    if not isitaninteger(num):
        return False

    return int(num) % 2 == 0


if __name__ == "__main__":
    main()
    
    
print("----addmultiplenumbers---------") 
print(addmultiplenumbers([2, 3, 4]))
print(addmultiplenumbers([10, 20, 30]))
print(addmultiplenumbers([10, -5, 2]))
print("----multiplymultiplenumbers---------")
print(multiplymultiplenumbers([2, 3, 4]))
print(multiplymultiplenumbers([5, 2, 3]))
print(multiplymultiplenumbers([5, -2]))
print("----isitaninteger---------")
print(isitaninteger(5))
print(isitaninteger(5.0))
print(isitaninteger(5.5))
print(isitaninteger(-3))
print("----isitevenr---------") 
print(isiteven(4))
print(isiteven(7))
print(isiteven(4.5))
