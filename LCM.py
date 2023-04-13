def LCM(num1, num2):
    gcd = GCD(num1, num2)
    return int((abs(num1 * num2))/gcd)


def GCD(num1, num2):
    num1_div = find_divisor(num1)
    num2_div = find_divisor(num2)

    if len(num1_div) < len(num2_div):
        num1_div.reverse()
        for val in num1_div:
            if num2_div.count(val) > 0:
                return val
    else:
        num2_div.reverse()
        for val in num2_div:
            if num1_div.count(val) > 0:
                return val

    return 1


def find_divisor(num):
    div = []
    for val in range(1, num + 1):
        if num % val == 0:
            div.append(val)
    return div


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


print("The LCM of {} and {} is {}".format(num1, num2, LCM(num1, num2)))
