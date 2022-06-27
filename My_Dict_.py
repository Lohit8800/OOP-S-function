import logging
logging.basicConfig(filename="Dict1_prasing.log",level=logging.WARN,format='%(asctime)s %(levelname)s %(message)s')






class dictionary_parsing:
    try:
        
        
        def __init__ (self,d):
            self.d=d
            
            
        def dictcheck(self):
            if type(self)!=dict:
                raise Exception ("please enter the  dictionary ")
            return 1
        
        
        def dictcopy(self):
            if self.dictcheck():
                d2={}
                d2=self.d
                return d2
            
        def dictget(self):
            if self.dictcheck():
                a=eval(input("Enter the value for get function "))
                for i in self.d:
                    if a==i:
                        break
            return list(self[i]) 
        
        
        def dictupdate(self):
            l=[]
            if self.dictcheck():
                c=eval(input("Enter the dictionary for the update function "))
                for i in self.d:
                    for a in c:
                        if a==i:
                            c[i]=self.d[i]
                            l.append(self.d)
                        else:
                            l.append(self.d)
                            return l                
                            
                            
        def keys(self):
            if self.dictcheck():
                return list(self.d.keys())
        
        
        def values(self):
            if self.dictcheck():
                return list(self.d.values())
        
        
        def userinput(self) :
            #eval enbales all type of variables
            self.d=eval(input())
            print("entered keys are ",self.keys())
            print("Entered values are ",self.values())
     
        
        
        def insertion(self,k,v):
            self.d[k]=v
            
            
    except Exception as e:
        print(e)
                        
                        
                            
                            
                            
                    
                
            