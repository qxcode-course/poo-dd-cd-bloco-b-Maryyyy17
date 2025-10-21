class Camisa :
    def __init__ (self) :
        self.__tamanho : str = "()"

    def __str__(self) -> str :
        return f"size: {self.__tamanho}"

    def set_Camisa(self, tam: str) -> None :
        if tam != "P" and tam != "M" and tam !="G" and tam != "PP" and tam != "GG" and tam != "XG" :
            print ("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
            return
        self.__tamanho = f"({tam})"

    def get_Camisa(self) :
        return self.__tamanho
    
def main () :
        Blouse = Camisa()
        while Blouse.get_Camisa() :
            line = input()
            print("$" + line)
            args = line.split(" ")
            if args[0] == "end" :
                break
            elif args[0] == "show" :
                print(Blouse)
            elif args[0] == "size" :
                tam = str(args[1])
                Blouse.set_Camisa(tam)

main()