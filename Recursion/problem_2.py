result = []
digits = {"2": "abc",
          "3": "def",
          "4": "ghi",
          "5": "jkl",
          "6": "mno",
          "7": "qprs",
          "8": "tuv",
          "9": "wxyz", }


def letter_combo(index, currentString):
    if len(currentString) == len(digits):
        result.append(currentString)
        return

    for char in digits[currentString[index]]:
        print(char)
        letter_combo(index + 1, currentString + char)


letter_combo(0, "34")
print(result)