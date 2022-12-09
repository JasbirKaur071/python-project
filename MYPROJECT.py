#Email Slicer is just a simple tool that will take multiple email address as an input and slice to produce the username
#and the domain associated with it.The email must be divided into two strings by using the @ separator.

def email_slicer(email):
    username,_, domain=email.strip().partition("@")
    return f"Your username is {username} and domain is {domain.upper()}"

#main function--acts as point of execution for the program
if __name__=="__main__": 
    email = input('Please enter your email address: ')
    print(email_slicer(email))

#STRIP-this is used to remove the characters from the beginning or end of the string for the characters that are passed
# as parameters to the strip.
#partition-search the specified string, and splits the string into a tuple containing three elements.
#f means formatted string literals these string may contain replacement fields, which are expressions delimited by curly braces{}

 