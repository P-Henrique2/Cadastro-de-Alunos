class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.__nome = nome
        self.__nota1 = nota1
        self.__nota2 = nota2

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_nota1(self, nota1):
        self.__nota1 = nota1

    def get_nota1(self):
        return self.__nota1

    def set_nota2(self, nota2):
        self.__nota2 = nota2

    def get_nota2(self):
        return self.__nota2


    def calcular_media(self):
        return (self.__nota1 + self.__nota2) / 2


    def exibir_informacoes(self):
        media = self.calcular_media()
        print(f"Aluno: {self.get_nome()} | Média: {media:.2f}")



