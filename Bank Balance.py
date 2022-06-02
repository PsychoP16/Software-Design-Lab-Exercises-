sav_bal = 1000.00
cur_bal = 63532.00
def_pin = 6765

for _ in range(3):
    inp = int(input("Enter Your Pin: "))
    if inp==def_pin:
        acc_type = input("Please enter c for checking, S for saving: ")
        if acc_type=='c':
            print("Your checking balance is: ${}".format(cur_bal))
            break
        else:
            if acc_type=='s':
                print("Your saving balance is: ${}".format(sav_bal))
                break
            else:
                print("Something wrong")
                break
else:
    print("Your bank card is blocked")


