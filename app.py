
def intro():
    """ introduction message """
    print("Hello!\nShortly you will be asked to enter either Y or N to enter Roman Numerical Converter Program\n")
    while True:
        welcome_message = input("Y/N: ").upper()
        if "Y" in welcome_message:
            return choose()
        elif "N" in welcome_message:
            print("As you wish, have a good day !")
            quit()
        else:
            print("Please enter Y or N")
            continue


def choose():
    """ function to choose between two conversion ways roman to arabic or vice versa """
    print("Please choose between two options:\n"
          "*Print 'R' if you want to convert Roman number to Arabic\n"
          "*Print 'A' if you want to convert Arabic number Roman\n")
    while True:
        choice_message = input("R/A: ").upper()
        if choice_message == "R":
            return Converter().rta(str(input("Roman to Arabic: ").upper()))
        elif choice_message == "A":
            return atr(int(input("Arabic to Roman: ")))
        else:
            print("Please enter R or A")
            continue


roman_to_arabic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
arabic_to_romans = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400,
                    "D": 500, "CM": 900, "M": 1000}


class Converter:
    def rta(self, number):
        """ conversion from Roman to Arabic"""
        arabic = []
        if number.count("D") > 1 or number.count("L") > 1 or number.count("IIII") > 0 or number.count("V") > 1\
                or number.count("IV") > 1 or number.count("IX") > 1 or number.count("XXXX") > 0\
                or number.count("XL") > 1 or number.count("XC") > 1 or number.count("CD") > 1\
                or number.count("CCCC") > 0 or number.count("MMMM") > 0 or number.count("M") > 4\
                or number.count("C") > 4 or number.count("X") > 4 or number.count("I") > 4:
            Converter().rta(str(input("You entered incorrect Roman number. "
                                      "Please enter again. Roman to Arabic: ").upper()))
        for i in range(len(number)):
            if i > 0 and roman_to_arabic[number[i]] > roman_to_arabic[number[i - 1]]:
                arabic.append(roman_to_arabic[number[i]] - 2 * roman_to_arabic[number[i - 1]])
            else:
                arabic.append(roman_to_arabic[number[i]])
        print("Roman", number, "in Arabic numeral system is:", sum(arabic))
        return reply()


def atr(number):
    """ conversion from Arabic to Roman"""
    if number <= 0:
        return atr(int(input("Please enter positive number ahd higher than 0. Arabic to Roman: ")))
    range_flag = None
    for key, value in arabic_to_romans.items():
        if value == number:
            return key
        if number > value:
            range_flag = key
    remaining = number - arabic_to_romans[range_flag]
    return range_flag + atr(remaining)


def reply():
    """ this function replies converter"""
    reply_message = input("Do you want to convert again ? Y/N: ").upper()
    while True:
        if "Y" in reply_message:
            choose()
        elif "N" in reply_message:
            print("As you wish, have a good day !")
            quit()
        else:
            print("Please enter Y or N")
        continue


if __name__ == "__main__":
    intro()
    choose()
    reply()
