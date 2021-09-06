# Truthy vs Falsy

user_name = bool('gunasekhar')
password = bool(1234)

if user_name and password:
    print("Logged into the website")
else:
    print("wrong username or password")