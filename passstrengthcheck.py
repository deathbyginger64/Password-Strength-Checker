import re

def strenght_checker(password):
    strenght = 0
    remark = []

    if len(password) < 8:
        return "weak" , "weak password"

    if re.search(r"[a-z]",password):
        strenght += 1
    else:
        remark.append("Add a lower case letter")
    if re.search(r"[A-Z]",password):
        strenght += 1
    else:        
        remark.append("Add a capital letter")
    if re.search(r"[!@#$%^&*(),./?;'{\/}]",password):
        strenght += 1
    else:
        remark.append("Add a symbol to your password")
    if re.search(r"\d",password):
        strenght += 1
    else:
        remark.append("Add a digit to your password")
    
    if strenght == 1:
        level = "weak"
    elif strenght == 2:
        level = "Moderate"
    elif strenght == 3:
        level = "Good"
    elif strenght == 4:
        level = "Excelent"
    
    if not remark:
        remark.append("You have a strong and a good password!!!!!")

    return level," ".join(remark)

password = input("Enter your password : ")
level , feedback = strenght_checker(password)
print(f"The strength of your password is : {level}")
print(f"The feedback : {feedback}")
