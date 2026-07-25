phone = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

def words(digits, current=""):
    if not digits:
        print(current)
        return

    for letter in phone.get(digits[0], ""):
        words(digits[1:], current + letter)

digits = input("Enter digits: ").strip()

if digits.isdigit():
    words(digits)
else:
    print("Please enter only digits.")