user_password=input("Enter the password you want:\n")
upper_case="QWERTYUIOPASDFGHJKLZXCVBNM"
while(len(user_password)<8 or not(any(i for i in user_password if i in upper_case))):
    if(len(user_password)<8):
        print("Password is too short.\n")
    if(not(any(i for i in user_password if i in upper_case))):
        print("Password must contain an uppercase letter.")
    user_password=input("Enter the modified password:\n")
print("Password is strong.")


