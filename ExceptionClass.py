password=input("enter your password: ")
try:
    if password !="Prasanth":
        raise NameError
    else:
        print("welcome to terminal")
except Exception:
    print("Password does not matched!..")