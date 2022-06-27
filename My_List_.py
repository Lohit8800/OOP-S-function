import logging
logging.basicConfig(filename="List1_prasing.log",level=logging.WARN,format='%(asctime)s %(levelname)s %(message)s')




class list_prasing:
    
    l=[10,59,61,21,18,3,64,99,61,61,21]
    logging.info("This is start of my code and i am entering %s as my list",l)
    try:
        
        def __init__(self,l):
            self.l=l
            
            
        def checklist(self):
            if type (self.l)!=list:
                raise Exception("Please enter the list")
            return 1
        
        def listappend(self):
            if self.checklist():
                t1=eval(input("Enter the list for append function  "))
                l1=list(t1)
                return (self.l + [l1])
                logging.info("List_append function excuted succesfully")
            
        def listextend(self):
            if self.checklist():
                t1=eval(input("Enter the list for extend function  "))
                l1=list(t1)
                return (self.l + l1)
                logging.info("List_extend function excuted succesfully")
            
        def listcopy(self):
            if self.checklist():
                l2=self.l
                return l2
                logging.info("List_copy function excuted succesfully")
            
            
        def listinsert(self):
            if self.checklist():
                try:
                    a=int(input("Enter the position for insert function "))
                    b=eval(input("Enter the value for insert functon "))
                    d=self.l[:a]+[b]+self.l[a:]
                    return d
                    logging.info("List_insert function excuted succesfully")
                except Exception as e:
                    print("Enter the correct value",e)
            
        def listclear(self):
            try:
                if self.checklist():
                    self.l=[]
                    return self.l
                    logging.info("List_clear function excuted succesfully")
            except Exception as e:
                print(e)
            
        def  listcount(self):
            try:
                b=[]
                if self.checklist():
                    a=int(input("Enter the value for count function "))
                    for i in self.l:
                        while a==i:
                            b=b+[i]
                            i+=1 
                    for h,j in enumerate (b):
                        pass
                    return h+1
                    logging.info("List_count function excuted succesfully")
            except Exception as e:
                    print("Enter the correct value",e)
            
            
        def  listindex(self):
            if self.checklist():
                try:
                    a=eval(input("Enter the value for index function "))
                    for i,j in enumerate (self.l):
                        if j==a:
                            return i
                            logging.info("List_index function excuted succesfully")
                except Exception as e:
                    print ("Enter the correct value ",e)
           
                
            
         
        def listpop(self):
            d=[]
            if self.checklist():
                for i in self.l:
                    d=self.l[:-1]
                return d
                logging.info("List_pop function excuted succesfully")
                        
                
        def listremove(self):
            d=[]
            if self.checklist():
                try:
                    a=eval(input("enter the value remove function  "))
                    for i,j in enumerate(self.l):
                        if a==j:
                            a=0
                            d=self.l[:i]+self.l[i+1:]
                    return d
                    logging.info("List_remove function excuted succesfully")
                except Exception as e:
                    print("Enter the correct value ",e)
                    
                    
                
        def listreverse(self):
            if self.checklist():
                try:
                    self.l=self.l[::-1]
                    return self.l
                    logging.info("List_reverse function excuted succesfully")
                except Exception as e:
                    print(e)
            
        def listsort(self):
            if self.checklist():
                try:
                    for i in range(len(self.l)):
                        for j in range (len(self.l)):
                            if self.l[i]<self.l[j]:
                                self.l[j],self.l[i]=self.l[i],self.l[j]
                    return self.l
                    logging.info("List_sort function excuted succesfully")
                except Exception as e:
                    print(e)
    except Exception as e:
        print(e)


l=[10,59,61,21,18,3,64,99,61,61,21]
d=list_prasing(l)