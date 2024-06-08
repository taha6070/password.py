user_name = input("username")

if (user_name == 'taha'):
    print("authorized")

elif (user_name != "taha"):
    print("unauthorized")
    for i in range(3):
        x= input("hello")
        if (x=="taha"):
            print("authorized")
            break
        else :
            continue