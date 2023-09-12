
import time 

def is_new_account(fun):
    def wrapper(*args,**kwargs):
        self_obj=args[0]
        data=args[1]
        if not self_obj.id:
            if "username" in data.keys():
                for a in self_obj.__class__.accounts: # ovoid circular dependencies 
                    if a['username']==data['username']:  #since its a dict there key is username , n we cant use it again 
                        return "username is not avalaibale "
                fun(*args,**kwargs)
            else:
                print("provide user name ")
        else:
            print("only one account can be created ")

    return wrapper







"""
def timing(fun):
    def wrapper(*arg,**kwargs): # We dont know the no. of arguments to pass there use *args
        print("start")
        t1=time.time() # Start time 
        fun(*arg,**kwargs)
        t2=time.time()   # End time
        print("end") 
        return str(t2-t1)  # u can use int, float 
    return wrapper


@timing  # Decorator
def printf(s):
    time.sleep(2)
    print(s)
"""


