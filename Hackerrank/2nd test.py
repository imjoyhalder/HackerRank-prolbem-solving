# joyhalder@gamil.com
email = input("Enter your email: ")
k,j,l = 0,0,0
if len(email)>= 16:
    if email[0].isalpha():
        if email is email.upper():
            if "@" in email:
                if email[-10] == "@":
                    if email[-3] == ".":
                        for i in email:
                            if email.isspace():
                                k = 1
                            elif email.isdigit():
                                j = 1

                        if k == 1 or j == 1:
                            print("Wrong Email 6")
                else:
                    print("Wrong Email 5")
            else:
                print("Worng Email 4")
        else: 
            print("Wrong Email 3")            
    else:
        print("Wrong Email 2")
else:
    print("Email is not capabele greter than 16 Charecter")