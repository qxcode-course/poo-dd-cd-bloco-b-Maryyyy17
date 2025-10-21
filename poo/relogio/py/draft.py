class Relogio :
    def __init__(self,hora : int, min: int, seg: int) :
        self.__hora = 0
        self.__min = 0
        self.__seg = 0
        self.set_hora(hora)
        self.set_min(min)
        self.set_seg(seg)
        
    def __str__(self) -> str :
        return f"{self.__hora:02}:{self.__min:02}:{self.__seg:02}"

    def set_hora(self, valor : int) -> None :
        
        if valor > 23 or valor < 0 :
            print("fail: hora invalida")
            return 
        self.__hora = valor

    def set_min(self,valor : int) -> None :
        
        if valor > 59 or valor < 0 :
            print("fail: minuto invalido")
            return
        self.__min = valor
        
    def set_seg(self, valor : int) -> None :
        if valor > 59 or valor < 0 :
            print("fail: segundo invalido")
            return
        self.__seg = valor
         
    def get_hour(self) -> int:
        return self.__hora

    def get_min(self) -> int :
        return self.__min

    def get_seg(self) -> int :
        return self.__seg
    
    def next_second(self):
        self.__seg += 1
        if self.__seg > 59:
            self.__seg = 0
            self.__min += 1
            if self.__min > 59:
                self.__min = 0
                self.__hora += 1
                if self.__hora > 23:
                    self.__hora = 0

def main() :
    clock = Relogio(00,00,00)
    while True :
        line = input()
        print("$" + line)
        args = line.split(" ")
        if args[0] == "end" :
            break
        elif args [0] == "init" :
            hora = int(args[1])
            min = int(args[2])
            seg = int(args[3])
            clock = Relogio(hora, min, seg)

        elif args[0] == "set" :
            hora = int(args[1])
            min = int(args[2])
            seg = int(args[3])
            clock.set_hora(hora)
            clock.set_min(min)
            clock.set_seg(seg)

        elif args[0] == "show" :
            print(clock)
        elif args[0] == "next" :
            clock.next_second()

        else :
            print("input inválido")
main()
            


            

    

        
