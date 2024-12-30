class serviceman:
    def __init__(self, name3="noinfo", type3="noinfo", rank3="noinfo"): 
        self.name3 = name3
        self.type3 = type3
        self.rank3 = rank3
        
    def vozvratdannih(self): 
        return f"serviceman:(roditel)\nname3: {self.name3}\ntype3: {self.type3}\nrank3: {self.rank3}\n"

class servicemannaslednik(serviceman):
    def __init__(self, name3="noinfo", type3="noinfo", rank3="noinfo",age3=0 ):
        super().__init__(name3, type3, rank3)
        self.age3 = age3

    def vozvratdannih(self): 
        return f"serviceman:(naslednik)\nname3: {self.name3}\ntype3: {self.type3}\nrank3: {self.rank3}\nage3: {self.age3}\n"

roditel = serviceman("Ivanov Ivan Ivanovich", "VDV", "Capitan")
naslednik = servicemannaslednik("Petrov Petr Petrovich", "VVS", "Praporshik", 34)

print(roditel.vozvratdannih())
print(naslednik.vozvratdannih())
