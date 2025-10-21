class Person:
    def __init__(self, name : str, age: int) :
        self.__name : str = ""
        self.__age: int = 0

    def toString(self) -> str :
        return f"{self.__name}:{self.__age}"
    
    def getName(self)-> None:
        return self._name
    
    def getAge(self) -> None :
        return self.__age

class Moto :
    def __init__(self) :
        self.__power: int = 1
        self.__time: int = 0
        self.__person: Person

    def __str__(self) :
        return f"power: {self.__power}, time:{self.__time}, person: {self.__person}"
    
    def enter(self, nome: str, idade: int)

    def insert(self,pessoa:Person) -> bool :
        if pessoa == True :
            print("fail: busy motocycle")
            return False
        else:
            pessoa +=1
            return True



    def drive (self,tempo : int, idade : int) :
        if self.__person == 0 :
            print("nao há passageiros")
            return
        if self.__time == 0 :
            print("compre tempo primeiro")
            return
        if idade > 10 :
            print("too old to drive")
            return
        if 

    
    def leave(self) -> None :
        if self.__person == 1 :
            self.__person -= 1
        else :
            print("nao há ninguem na moto")

    def buy(self, tempo : int) -> None :
        self.__time += tempo 
        if self.__time

    def honk(self) :
