class Static:
    a=25
    def show():
        print("executing show method")
obj=Static
obj.show()
print(Static.a)