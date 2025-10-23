class Person:
    def __init__(self, name : str, age: int) :
        self.__name : str = name
        self.__age: int = age

    def toString(self) -> str :
        return f"{self.__name}:{self.__age}"
    
    def getName(self)-> str :
        return self._name
    
    def getAge(self) -> int :
        return self.__age

class Moto :
    def __init__(self) :
        self.__power: int = 1
        self.__time: int = 0
        self.__person: Person = None

    def __str__(self) :
        if self.__person == None :
            return  f"power:{self.__power}, time:{self.__time}, person:(empty)"
        return f"power:{self.__power}, time:{self.__time}, person:({self.__person.toString()})"

    def insert(self,pessoa:Person) -> bool :
        if self.__person is not None :
            print("fail: busy motorcycle")
            return False
        else:
            self.__person = pessoa
            return True
        
    def leave(self) -> Person | None :
        if self.__person != None :
            print(self.__person.toString())
            self.__person = None
        else :
            print("fail: empty motorcycle")

    def drive (self, tempo : int) -> None:
        if self.__person != None and self.__person.getAge() > 10 :
            print("fail: too old to drive")
            return
        if self.__time == 0 :
            print("fail: buy time first")
            return
        if tempo > self.__time :
            print(f"fail: time finished after {self.__time} minutes")
            self.__time = 0
        if self.__person == None :
            print("fail: empty motorcycle")
        else:
            self.__time -= tempo
            if self.__time < 0 :
                self.__time = 0

    def buy(self, tempo : int) -> None :
         self.__time += tempo 
         return tempo
        
    def honk(self) -> str:
        buzina = "P" + ("e" * self.__power) + "m"
        return buzina
    
    def getPerson(self) -> Person :
        return Person
    
    def getPower(self):
        return self.__power
    
    def getTime(self) -> int:
        return self.__time
    
    def setPower(self, power: int) :
        self.__power = power

def main() :
    pop = Moto()
    while True :
        line = input()
        print("$" + line)
        args = line.split(" ")
        if args[0] == "end" : 
            break
        elif args[0] == "show" :
            print(pop)
        elif args[0] == "init" :
            pot = int(args[1])
            pop.setPower(pot)
        elif args[0] == "enter":
            entrarn =(args[1])
            entrari = int(args[2])
            pop.insert(Person(entrarn, entrari))
        elif args[0] == "buy" :
            tempo = int(args[1])
            pop.buy(tempo)
        elif args[0] == "leave" :
            pop.leave()
        elif args[0] == "drive" :
            tempo = int(args[1])
            pop.drive(tempo)
        elif args[0] == "honk" :
            print(pop.honk())
        else :
            print("input invalido")
main()