user_login = "adam"
user_password = "Qwerty123456"

login = input("Login: ")
password = input("Password: ")

if (login == user_login) and (password == user_password):
    print("Добро пожаловать")
else:
    print("Неверный логин или пароль")

crit1 = "red"
crit2 = "lock"
colour = input("Colour: ")
feature = input("Feature: ")
if (colour == crit1) or (feature == crit2):
        print("Покупаю рюкзак")
else:
        print("Ничего не подошло")