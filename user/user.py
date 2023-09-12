from .decorators import is_new_account
class Account():
    accounts=[]
    id = 0 

    def __init__(self,id=None):
        self.id=id

    def get(self):
        if self.id:
            for a in Account.accounts:
                if a['id']==self.id:
                    return a 
        else:
            print("account is not created yet ")

    @is_new_account
    def create(self,data):
        Account.id+=1
        data['id']=Account.id
        Account.accounts.append(data)
        self.id =Account.id 



    def update(self,age=None,password=None):
        if self.id:
            for a in Account.accounts:
                if a['id']==self.id:
                    a['age']=age
                    a['password']=password
                    break
                    
        else:
            print("account is not created yet ")

    def delete(self):
        if self.id:
            for a in Account.accounts:
                if a['id']==self.id:
                    Account.accounts.remove(a) 
                    break
        else:
            print("account is not created yet ")