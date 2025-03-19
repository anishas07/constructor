#class creation
class employee: 
#constructor
    def __init__(self):
        print("employee is created.")
#destructor
    def __del__(self):
        print("Destructor was used.")
#object creation
object1 = employee()
del object1