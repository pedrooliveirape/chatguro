from horoscopo import verificar_signo


class Usuario:

    def __init__(self, nome, dia_nasc, mes_nasc, ano_nasc):
        self.__nome = nome
        self.__dia_nasc = dia_nasc
        self.__mes_nasc = mes_nasc
        self.__ano_nasc = ano_nasc
        self.__signo = verificar_signo(dia_nasc, mes_nasc)

    @property
    def signo(self):
        return self.__signo



