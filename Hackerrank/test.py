email = input("Enter your email: ")    # joyhalder@gmail.com
j,k,l = 0,0,0
if len(email)<=25 and len(email)>=16:
    if email[0].isalpha():
        if email[0:] == email.lower():
            if email[-1]=="m" and email[-2]=="o" and email[-3]=="c" and email[-4]=="." and email[-5]=="l" and email[-6]=="i" and email[-7]=="a" and email[-8]=="m" and email[-9]=="g" and email[-10]=="@":
                for i in email: 
                    if i.isspace() == False:
                        if  i.isdigit() == False:
                            if i == "_" or i == "!" or i == "@":
                                print("Successful")
                                break
                            else:
                                print("Special charecter is not allow")
                                break
                        else:
                            print("Digits is not allow")
                            break
                    else:
                        print("Space is not allow")
            else:
                print("Email last fromat  ....@gmail.com")
        else:
            print("Upper case alphabate Character is not capable into email address")   
    else:
        print("Email contain frist Character Alphabet")
else: 
    print("Email contain 16 to 25 Character")