def reverse(number):
    rev_num = 0
    while number > 0:
        rev_num = rev_num * 10 + number % 10
        number = number // 10
    return rev_num

def isPalindrome(number):
    return number == reverse(number)

number = int(input("Enter an integer: "))
if isPalindrome(number):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")


