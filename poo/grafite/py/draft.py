
class Lead :
    def __init__(self, thickness : float, hardness : str, size : int):
        self.__thickness : float = thickness
        self.__hardness : str = hardness
        self.__size : int = size 

    def __str__(self) -> str :
        return f"[{self.__thickness}:{self.__hardness}:{self.__size}]"

    def usagePerSheet(self) -> int :
        grosso = self.__hardness
        if grosso == "HB" :
            return self.__thickness(1)
        if grosso == "2B" :
            return self.__thickness(2)
        if grosso == "4B" :
            return self.__thickness(4)
        if grosso == "6B" :
            return self.__thickness(6)
        
    def setSize(self, size : int) -> None :
        self.__size = size

    def getHardness(self) -> str:
        return self.__hardness
    
    def getThickness(self) -> float :
        return self.__thickness
    
    def getSize(self) -> int :
        return self.__size
        
class Grafite :
    def __init__(self, tip : float) :
        self.__tip : float = tip
        self.__lead : Lead = None

    def __str__(self) -> str :
        if self.__lead == None:
            return f"calibre: {self.__tip}, grafite: {"null"}"
        return f"calibre: {self.__tip}, grafite: {self.__lead.__str__()}"
        
    def hasGraffite(self) -> bool:
        if self.__lead is not None :
            print("nao tem grafite")
            return False
        else :
            return True
        
    def insert(self, lead : Lead) -> bool:
        if self.__lead is not None :
            print("nao tem grafite")
            return False
        else :
            self.__tip(lead)
            return True
        
    def remove(self) -> Lead | None :
        if self.__lead is None :
            print("fail: sem grafite")
            return None
        else :
            remover = self.__lead
            self.__lead = None
            return remover

    def writePage(self) -> None :
        if self.__lead is None :
            print("fail: sem grafite")
            return 
        
        usar = self.__lead.usagePerSheet()
        tamanho = self.__lead.getSize()

        if tamanho <= 10 :
            print("fail: tamanho insuficiente")
            return
        
        if tamanho - usar < 10 :
            escrever = tamanho -10
            self.__lead.setSize(10)
            print(f"fail: folha incompleta")
            return
        
        self.__lead.setSize(tamanho-usar)
            
def main():
    lapiseira = Grafite
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")
        if args[0] == "end" :
            break
        if args[0] == "show" :
            print(lapiseira)
        if args[0] == "init" :
            ponta = float(args[1])
            lapiseira = Grafite(ponta)
        if args[0] == "insert":
            thick = float(args[1])
            hard = str(args[2])
            siz = int(args[3])
            lapiseira.insert(Lead(thick, hard, siz))
        if args[0] == "remove":
            if lapiseira is not None:
                lapiseira.remove()
        if args[0] == "write":
            if lapiseira is not None:
                lapiseira.writePage()

main()