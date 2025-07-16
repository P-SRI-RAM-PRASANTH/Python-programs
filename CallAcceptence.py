def ringing(morning, mother,sleep):
    if  not morning and  not mother and  not sleep:
        return True
    if not morning and mother and not sleep:
        return True
    if morning and mother and  not sleep:
        return True
    return False

print(ringing(True,True,False))







              