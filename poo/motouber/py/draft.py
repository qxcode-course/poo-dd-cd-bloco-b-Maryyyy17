class Person :
    def __init__(self, name : str, money : int):
        self.__name : str = name
        self.__money : int = money

    def __str__(self) -> str:
        return f"{self.__name}:{self.__money}"
    
    def setMoney(self, money : int) -> None:
        return self.__money == money
    
    def getName (self) -> str:
        return self.__name
    
    def getMoney(self) -> int:
        return self.__money
    

class MotoUber:
    def __init__(self) :
        self.__valor : int = 0
        self.__motorista : Person = None
        self.__passageiro : Person = None

    def __str__(self) :
        if self.__motorista == None and self.__passageiro == None :
            return f"Cost: {self.__valor}, Driver: None, Passenger: None"
        if self.__motorista == None :
            return f"Cost: {self.__valor}, Driver: None, Passenger: {self.__passageiro.__str__()}"
        if self.__passageiro == None :
            return f"Cost: {self.__valor}, Driver: {self.__motorista.__str__()}, Passenger: None"
       
        
    def setDriver(self, driver : Person) :
        if self.__motorista is not None :
            print("fail: already has a driver")
            return False
        self.__motorista = driver
        print(f"{self.__motorista}")
        return True
        
    def setPassenger(self, passageiro : Person) :
        if self.__motorista is None :
            print("fail: theres no driver")
            return False
        self.__passageiro = passageiro
        print(f"{self.__passageiro}")
        return True
        
    def getDriver(self) -> Person | None :
        return self.__motorista
    
    def getPassenger(self) -> Person | None :
        return self.__passageiro
    
    def corrida(self, distance : int) :
        self.__valor += distance
        if distance > self.__passageiro.getMoney() :
            print("fail: Passenger does not have enough money")
            self.__passageiro.setMoney(0)
        else :
            self.__passageiro.setMoney(self.__passageiro.getMoney() - distance)
            self.__motorista.setMoney(self.__motorista.getMoney() + distance)

    def leave(self) -> Person | None :
        if self.__passageiro != None :
            print(self.__passageiro)
            self.__passageiro = None
        else :
            print("no passenger")

def main() :
    taxi = MotoUber()
    while True :
        line = input()
        print("$" + line)
        args = line.split(" ")
        if args[0] == "end" :
            break
        elif args[0] == "show" :
            print(taxi)
        elif args[0] == "setDriver" :
            nome = (args[1])
            dinheiro = int(args[2])
            taxi.setDriver(nome, dinheiro)
            
        elif args[0] == "setPass" :
            nome = (args[1])
            dinheiro = int(args[2])
            taxi.setPassenger(Person(nome, dinheiro))
            
        elif args[0] == "drive" :
            valor = int(args[1])
            taxi.corrida(valor)
        elif args[0] == "leavePass" :
            taxi.leave()

main()


        
    