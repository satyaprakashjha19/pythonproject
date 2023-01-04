def disp():
    def show():
        print("show function")
    print("disp function")
    show()

disp()

#with return

def disp():
    def show():
        return "show function"
    result = show() + " Disp function"
    return result
a = disp()
print(a)
    
