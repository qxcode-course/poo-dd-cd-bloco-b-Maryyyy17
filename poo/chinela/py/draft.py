class Chinela :
    def __init__(self) :
        self.__tamanho = 0

    def __str__(self) -> str :
        return f"{self.__tamanho}"
    
    def set_chinela(self, valor) :
        if valor < 20 or valor > 50 or valor % 2 == 1 :
            print("numeraçao invalida")
            return False
        self.__tamanho = valor
        return True
        
    def get_chinela(self) :
        return self.__tamanho
    
def main() :
    slipper = Chinela()
    while slipper.get_chinela()==0:
        line = input()
        print ("$" + line)
        args = line.split(" ")
        if args[0] == "end" :
            break
        elif args[0] == "init" :
            slipper = Chinela()
            print("Qual o tamanho da sua chinela?")
            slipper.__init__()
            if len(args) > 1 :
                try:
                    tamanho = int(args[1])
                    slipper.set_chinela(tamanho)
                except ValueError :
                    print("Digite um número valido")
            else :
                print("Uso : set<tamanho>")
        elif args[0] == "show" :
            print(slipper)
        else :
            print("input inválido")

main()

        

        
        


