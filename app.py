from menu import menu,control
from functions import solveAccount,solveTest



line="""  

\t\t  ____ ____      _    ____ _  _______ ____  
\t\t / ___|  _ \    / \  / ___| |/ / ____|  _ \ 
\t\t| |   | |_) |  / _ \| |   | ' /|  _| | |_) |
\t\t| |___|  _ <  / ___ \ |___| . \| |___|  _ < 
\t\t \____|_| \_\/_/   \_\____|_|\_\_____|_| \_\ 


"""                                     
print(line)
selection="start"
menu()
while(selection!="0"):
    selection=control()

    if(selection=="0"):
        print("\n\tExit Program")
        break

    if(selection=="1"):
        _url=str(input("\t Enter URL your account : "))
        print()
        _email=str(input("\t Enter Email your account : "))
        _minChar=str(input("\t Password min Character Lenght : "))
        result = solveAccount(url=_url,head=_email,minChar=_minChar)

    elif(selection=="3"):
        _key=str(input("\tEnter test KEY : "))
        _minChar=str(input("\tPassword min Character Lenght : "))
        print()
        result = solveTest(head=_key,minChar=_minChar)
        if(result!=None):
            print("Key Found! Your key is "+result)







