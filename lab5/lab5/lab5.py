import random
import pickle # Importiruem modul' pickle dlya serializacii i deserializacii ob"ektov

class serviceman:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.rank = ""
        self.nameArr = ["Ivanov Ivan Ivanovich", "Petrov Petr Petrovich", "Nikolaev Nikolay Nikolaevich", "Pavlov Pavel Pavlovich"]
        self.typeArr = ["VDV","VVS","VMF","RVSN","KGB","OMON"]
        self.rankArr = ["Capitan","Praporshik","Ryadovoy","Polkovnik","Podpolkovnik","Leytenant"]
        self.name = self.nameArr[random.randint(0, len(self.nameArr) - 1)]
        self.type = self.typeArr[random.randint(0, len(self.typeArr) - 1)]
        self.rank = self.rankArr[random.randint(0, len(self.rankArr) - 1)]


class queues:
    def __init__(self, n=1):
        self.n = n
        self.Queues = [serviceman() for _ in range(n)]

    def GetRes(self):
        for i in range(self.n):
            print(f"name: {self.Queues[i].name} \ntype: {self.Queues[i].type} \nrank: {self.Queues[i].rank}")

if __name__ == "__main__":
    print("count of elements:")
    n = int(input())
    q2 = queues(n)
    q2.GetRes()
    # serialization
    with open("File_queue.txt", "wb") as fs:            #otkryvaem ili sozdaem, esli net, fajl dlya zapisi
        pickle.dump(q2, fs)
        print("\nObject has been serialized")
    q1 = queues()
    # dserialization
    with open("File_queue.txt", "rb") as fs:
        q1 = pickle.load(fs)    #Deserializuem ob"ekt iz fajla i sohranyaem ego v q1
        print("Object has been deserialized \n")
    q1.GetRes()
    fs.close()


