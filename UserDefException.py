age=int(input())
try:
    if age>18:
        print("You are eligible to vote")
    else:
        raise "AgeLimitError"
except "AgeLimitError" :
    print("You are not eligible to vote")
