class serviceman:
    def __init__(self, name2="noinfo", type2="noinfo", rank2="noinfo"):
        self.name2 = name2
        self.type2 = type2
        self.rank2 = rank2
default = serviceman()
print("vvedite znachenie po ymolchaniuy")
default.name2 = input()
print("vvedite znachenie po ymolchaniuy")
default.type2 = input()
print("vvedite znachenie po ymolchaniuy")
default.rank2 = input()

peregryjenniy = serviceman("Ivanov Ivan Ivanovich", "VDV", "Capitan")

print("peregryjenniy: ", peregryjenniy.name2, peregryjenniy.type2, peregryjenniy.rank2)
print("po ymolchaniuy: ",default.name2, default.type2, default.rank2)
