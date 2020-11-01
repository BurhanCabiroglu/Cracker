class CryptoNumber:
    def __init__(self,decimal=0):
        self.decimal=decimal
        self.value=""
        #self.characters=["0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,r,s,t,u,w,v,y,z"]
        self.characters=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","."]
        self.length=len(self.characters)
        self.calculate(self.decimal)
        
      

    def add(self):
        self.decimal+=1
        self.value=""
        self.calculate(self.decimal)

    def calculate(self,n):
        if(n//self.length==0):
            self.value+=(str(n%self.length))
            
        else:
            self.calculate(n//self.length)
            self.value+=(" - "+str(n%self.length))

    def getValue(self):
        ret=""
        val0=self.value.split("-")
        for i in val0:
            ret+=self.characters[int(i)]   
        return ret

           