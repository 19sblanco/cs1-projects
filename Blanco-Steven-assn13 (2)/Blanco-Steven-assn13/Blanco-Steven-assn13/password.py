class Password:
    # define instant variables
    def __init__(self):
        self.__valid = True
        self.__password = None
        self.__message = ""
    # checks if the password meets requirements using functions
    def __isValid(self):
        self.__isEndsWith123()
        self.__isInPassword()
        self.__isEnoughDigit()
        self.__isLong()
        self.__isAlphanumerical()
        return self.__valid
    # set password
    def setPassword(self, password):
        self.__password = password
    # check the length of password
    def __isLong(self):
        if len(self.__password) < 8:
            self.__message += "password must be at least 8 characters long\n"
            self.__valid = False
    # checks if its alpha numerical
    def __isAlphanumerical(self):
        if not self.__password.isalnum():
            self.__message += "password must not have special characters\n"
            self.__valid = False
    # checks each character if its a digit, if so add to num count
    def __checkNums(self):
        num = 0
        for i in str(self.__password):
            if i.isdigit():
                num += 1
        return num
    # uses checkNums() to see if password has atleast 2 digits
    def __isEnoughDigit(self):
        if self.__checkNums() <= 2:
            self.__message += "password must have at least 2 digits\n"
            self.__valid = False
    # checks is "password" is in their password
    def __isInPassword(self):
        if "password" in self.__password.lower():
            self.__message += "password must not contain 'password'\n"
            self.__valid = False
    # checks if password ends with 123
    def __isEndsWith123(self):
        if self.__password.endswith("123"):
            self.__message += "password must not end with '123'\n"
            self.__valid = False
    # returns error message
    def __getErrorMessage(self):
        return self.__message
    # prints if password is accepted or not, if not displays everything wrong with it
    def main(self):
        if self.__isValid():
            print("Password Created!")
        else:
            print(self.__getErrorMessage())

