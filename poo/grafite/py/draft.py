
class Lead :
    def __init__(self, thickness : float, hardness : str, size : int):
        self.__thickness : float = thickness
        self.__hardness : str = hardness
        self.__size : int = size 

    def __toString__(self) -> str :
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
    def __init__(self,)