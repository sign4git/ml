from data_manager import DataManager

print("Welcome to The Flight Club!!!")
print("We find the best flight deals and email you.")
f_name = input("What is your first name?\n")
l_name = input("What is your last name?\n")
email = input("What is your email?\n")
confirm_email = input("Please enter your email again.\n")

data_manager = DataManager()
data_manager.user_data

if email == confirm_email:
    data_manager.post_users_data(f_name=f_name, l_name=l_name, email=email)
    print("Success!! Your email has been added. Look forward to exciting flight deals")
