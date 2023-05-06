rom Email import Email
from ManejadorEmail import ManejadorEmail


if __name__ == '__main__':
    me = ManejadorEmail()
# INCISO 1
    nombre = input("Ingrese el nombre de una persona: ")
    idcuenta = input("Ingrese el id de su email: ")
    dominio = input("Ingrese el dominio de su Email: ")
    tipodominio = input("Ingrese el tipo de dominio de su email: ")
    contra = input("Ingrese la contraseña de su email: ")
    unEmail = Email(idcuenta, dominio, tipodominio, contra)
    print(f"Estimado {nombre} te enviaremos tus mensajes a la direccion {Email.retornaremail(unEmail)}")
# INCISO 2
    Email.verificarContra(unEmail)
# INCISO 3
# INCISIO 4 A
    me.testEmails()
    print(str(me))
# INCISO 4 B
    dom = input("Ingrese un dominio a buscar: ")
    print(f"La cantidad de Mails con ese dominio son: {me.identificarDom(dom)}")
