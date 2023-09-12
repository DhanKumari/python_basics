class MyException(Exception):
    def __init__(self,args):
        self.args= args



try:
    l=[0,1,2]
    raise MyException("kannu")
    print("try block is executed")
except IndexError:
    print("Exeption occurred","index error")
else:
    print("there is no execption")
finally:
    print("Error occurred or successfully try block")


