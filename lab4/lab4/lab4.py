import random  

class serviceman:
    def __init__(self): 
        self.namemassive = ["Ivanov Ivan Ivanovich","Petrov Petr Petrovich","Nikolaev Nikolay Nikolaevich","Pavlov Pavel Pavlovich"]
        self.typemassive = ["VDV","VVS","VMF","RVSN"]
        self.rankmassive = ["Capitan","Praporshik","Ryadovoy","Polkovnik","Podpolkovnik","Leytenant"]
        self.name4 = random.choice(self.namemassive)  
        self.type4 = random.choice(self.typemassive)
        self.rank4 = random.choice(self.rankmassive)

class queues:
    def __init__(self, k):  
        self.queues = [serviceman() for _ in range(k)]  
    
    def __getitem__(self, pos):  
        if pos >= 0 and pos < 30:  
            return self.queues[pos] 
        else:
            raise IndexError("indexerror") 
    
    def __setitem__(self, pos, value):  
        self.queues[pos] = value 

countofelements = int(input("vvedite kolichestvo elementov: "))  
a = queues(countofelements)  
for i in range(countofelements):  
    print(f"name: {a[i].name4}\n type: {a[i].type4}\n rank: {a[i].rank4}\n")