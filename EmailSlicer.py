"""
An email slicer that splits an email into its username, domain, and extension
"""

def email_slicer():
    """
    Returns a String detailing the username, domain, and extension of an inputted email.
    """
    next_step = False
    while next_step == False:
        full_email = input("What is your email?").strip()
        if "@" in full_email and "." in full_email:
            next_step = True
        else:
            print("Please enter a valid email.")
    index1 = full_email.index("@")
    index2 = full_email.rindex(".")
    username = full_email[:index1]
    domain = full_email[index1 + 1:index2]
    extension = full_email[index2 + 1:]
    return f"The username is {username}\nThe domain is {domain}\nThe extension is {extension}" 

print(email_slicer())