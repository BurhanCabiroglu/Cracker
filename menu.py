

def menu():
    print("\t\t  1) Bruteforce Web Accounts")
    print("\t\t  2) Bruteforce Rar or Zip Files")
    print("\t\t  3) Bruteforce Test")
    print("\t\t  0) exit\n")



def control():
    select=str(input("\tChoose what you want : "))
    group=["0","1","2","3","4"]
    while(not (group.__contains__(select))):
        select=str(input("\tWrong Selection. Please Choose Right Option : "))
    return select    