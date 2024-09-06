print("Welcome to Health Management system \nWhat do you want to")
a = int(input("press 1 for log and press 2 for retriev\n"))
n1 = int(input("press 1 for exercise and press 2 for meal\n"))
n2 = int(input("press 1 for Aritra, press 2 for Kunal and press 3 for Monoj\n"))

def getdate() :
    import datetime
    return datetime.datetime.now()

#Log
if a == 1 :
    if n1 ==1 and n2 == 1 :
        with open("Aritrae.text", "a") as f1 :
            ine1 = input("Enter exrecise Aritra did today\n")
            time = str(getdate())
            f1.write("[" + time + "]" + ine1 + "\n")
    elif n1 == 2 and n2 == 1 :
        with open ("Aritraf.text", "a" ) as f2 :
            inm1 = input("Enter Aritra's meal\n")
            time = str(getdate())
            f2.write("[" + time + "]" + inm1 + "\n")
    elif n1 == 1 and n2 == 2 :
         with open("Kunale.text", "a") as f3 :
            ine2 = input("Enter exercise Kunal did today\n")
            time = str(getdate())
            f3.write("[" + time + "]" + ine2 + "\n")
    elif n1 == 2 and n2 == 2 :
        with open("Kunalf.text", "a") as f4 :
            inm2 = input("Enter kunal's meal\n")
            time = str(getdate())
            f4.write("[" + time + "]" + inm2 + "\n")
    elif n1 == 1 and n2 == 3 :
        with open("Monoje.text", "a") as f5 :
            ine3 = input("Enter exercise Monoj did today\n")
            time = str(getdate())
            f5.write("[" + time + "]" + ine3 + "\n")
    elif n1 == 2 and n2 == 3:
        with open("Monojf.text", "a") as f6 :
            inm3 = input("Enter Monoj's meal\n")
            time = str(getdate())
            f6.write("[" + time + "]" + inm3 + "\n")
    else :
        print("wrong input")

# Retrieve

if a== 2 :
    if n1 ==1 and n1 == 1 :
        with open("Aritrae.text") as f1 :
            print(f1.read())
    elif n1 == 2 and n2 == 1 :
        with open("Aritraf.text") as f2 :
            print(f2.read())
    elif n1 == 1 and n2 == 2 :
        with open("Kunale.text") as f3 :
            print(f3.read())
    elif n1 == 2 and n2 == 2 :
        with open("Kunalf.text") as f4 :
            print(f4.read())
    elif n1 == 1 and n2 == 3:
        with open("Monoje.text") as f5 :
            print(f5.read())
    elif n1 == 2 and n2 == 3 :
        with open("Monojf.text") as f6 :
            print(f6.read())
    else :
        print("Wrong option")