# python is case sensitive small 'a' and capital 'A' are different
enviornment = "DEv"
#enviornment = input("Enter your environment: ") # For user prompt
change_ticket = True
# To ignore case sensitive and it converts given env to upper case to lower and tries to match

enviornment =  enviornment.casefold()

# lower() only does basic lowercase conversion.
# casefold() is designed for case-insensitive comparisons across languages.
if enviornment == "prod":
    change_ticket = False
    print("Please provide a change ticket", change_ticket)
elif enviornment == "dev":
    print("You are logged in with Dev")
else:
    print("check your credentails")