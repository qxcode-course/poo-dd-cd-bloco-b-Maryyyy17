class Camisa :
    def __init__ (self) :
        self.__tamanho : str = " "


    def __str__(self) -> str :
        return f"{self.__tamanho}"

    def set_Camisa(self, tam: str) -> None :
        if tam != "P" or tam != "M" or tam !="G" or tam != "PP" or tam != "GG" or tam != "XG" :
            print ("inválido")
            return
        self.__tamanho = tam

    def get_Camisa(self) :
        return self.__tamanho
    
    def main () :
        Blouse = Camisa()
        while Blouse.get_Camisa() == "" :
            print("Digite seu tamanho de roupa")
            tamanho = input()
            Blouse.set_Camisa()