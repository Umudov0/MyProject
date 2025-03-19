def pass_control(p):
    if len(p) < 8:
        print("False")
        return "Your password must be at least 8 characters long"
    if not any(c.islower() for c in p) or not any(c.isupper() for c in p):
        print("False")
        return "Your password must contain both uppercase and lowercase letters"
    if not any(c.isdigit() for c in p):
        print("False")
        return "Your password must contain at least one digit"
    print("True")
    return "Your password is strong!"

p = input("Set your password: ")
print(pass_control(p))
