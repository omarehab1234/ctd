# the bag
bag = [12,33,14,54,11,100]

def check_Number(what_to_say):
    while True:
        try:
            number = int(input(what_to_say)) 
            return number
        except  ValueError as e:
            print(e)


while True:
    print(bag)
    todo = check_Number("what you want to do \n#1 Enter \n#2 Remove \n#3 Exit \n: ")
    
    if (todo == 1):
        add_Num = check_Number("What Number to add: ")
        bag.append(add_Num)
    elif (todo == 2):
        if(len(bag) <= 5):
            print("cannot remove, bag is at minimum capacity ")
        else:
            rem_num = check_Number("What Number to remove: ") 
            bag.remove(rem_num)
    else:
        break
