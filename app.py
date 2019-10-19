def intro():
    print("Hello!\nShortly you will be asked to enter either Y or N to enter Roman Numerical Converter Program\n")
    while True:
        welcome_message = input("Y/N: ").upper()
        if "Y" in welcome_message:
            print("YES") #there will add launch function
            quit()
        elif "N" in welcome_message:
            print("As you wish, have a good day !")
            quit()      #here maybe return False ?
        else:
            print("Please enter Y or N")
            continue


def choose():
    print("Please choose between two options:\n"
          "*Print 'R' if you want to convert Roman number to Arabic\n"
          "*Print 'A' if you want to convert Arabic number Roman\n")
    while True:
        choice_message = input("R/A: ").upper()
        if choice_message == "R":
            print("Roman to Arabic") #there will add launch function
        elif choice_message == "A":
            print("Arabic to Roman") #there will add launch function
        else:
            print("Please enter R or A")
            continue                        #should be quit()


#print(choose())
#print(intro())