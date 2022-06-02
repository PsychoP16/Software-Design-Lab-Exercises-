def verify_pin(pin):
    if pin == '0910':
        return True
    else:
        return False

def log_in():
    tries = 0
    while tries < 4:
        pin = input('Please Enter Your 4 Digit Pin: ')
        if verify_pin(pin):
            print("Pin accepted!")
            return True
        else:
            print("Invalid pin")
            tries += 1
    print("To many incorrect tries. Could not log in")
    return False


def main_menu():
    pass


def start_menu():
    print("Welcome to the atm!")
    if log_in():
        # you will need to make this one yourself!
        main_menu()
    print("Exiting Program")

start_menu()