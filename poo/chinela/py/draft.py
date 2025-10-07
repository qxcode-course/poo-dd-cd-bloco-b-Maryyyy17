class Chinela :
    def __init__(self) :
        self.__tamanho = 0

    def __str__(self) -> str :
        return f"Qual o seu tamanho da chinela? {self.__tamanho}"
    
    def set_chinela(self, valor) :
        if valor < 20 or valor > 50 and valor % 2 == 1 :
            print("numeraçao invalida")
            return
        
    def get_chinela(self) :
        return self.__tamanho
    
def main() :
    slipper = Chinela()
    while True =
        line = input()
        
        

        
        


