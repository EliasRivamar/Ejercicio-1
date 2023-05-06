class Email:
    __idcuenta = ""
    __dominio = ""
    __tipodominio = ""
    __contra = 0

    def __init__(self, idcuenta, dominio, tipodominio, contra):
        self.__idcuenta = idcuenta
        self.__dominio = dominio
        self.__tipodominio = tipodominio
        self.__contra = contra

    def crearCuenta(self):
        p = False
        if len(self.__idcuenta) == 0:
            print("---ERROR DE IDCUENTA---")
        elif not str(self.__dominio) == "gmail" or str(self.__dominio) == "hotmail":
            print("---ERROR DE DOMINIO---")
        elif len(self.__tipodominio) > 3 and len(self.__tipodominio) <= 1:
            print("---ERROR DE TIPO DE DOMINIO---")
        else:
            p = True
        return p

    def verificarContra(self):
        contrasena = input("Ingrese la contraseña actual: ")
        if contrasena == self.__contra:
            nuevaContra = input("Ingrese la nueva contraseña: ")
            self.__contra = nuevaContra
        else:
            print("----Contraseña Incorrecta----")

    def getDominio(self):
        return str(self.__dominio)

    def retornaremail(self):
        return str(self.__idcuenta+"@"+self.__dominio+"."+self.__tipodominio)

    def __str__(self):
        return str(self.__idcuenta+"@"+self.__dominio+"."+self.__tipodominio+" "+self.__contra+" ")
