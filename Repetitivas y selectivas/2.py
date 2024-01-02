password1 = input("ingrese su contraseña: ")
password2 = input("confirme su contraseña: ")
for i in range(2):
    if password2==password1:
        break
    if password2 != password1:
        password2 = input("confirme su contraseña: ")
while password2!=password1:
    print("vuelva a intentarlo mas tarde")
    break