import random
import time

class Mat_plata:
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
        self.Queues = [Mat_plata() for _ in range(n)]

    def GetRes(self):
        for i in range(self.n):
            print(f"name: {self.Queues[i].name} \ntype: {self.Queues[i].type} \nrank: {self.Queues[i].rank}")

    def GetArr(self):
        trapArr = [["" for _ in range(3)] for _ in range(self.n)]
        for i in range(self.n):
            trapArr[i][0] = self.Queues[i].name
            trapArr[i][1] = self.Queues[i].type
            trapArr[i][2] = self.Queues[i].rank
        return trapArr

class Sorts:
    @staticmethod
    def PryamVbIborSort(arr, str):
        curtime = time.perf_counter()
        k = 0
        if str == "name" or str == "0":
            k = 0
        elif str == "type" or str == "1":
            k = 1
        elif str == "rank" or str == "2":
            k = 2
        for i in range(len(arr) - 1):
            nushIndex = i
            for j in range(i + 1, len(arr)):
                if arr[j][k] < arr[nushIndex][k]:
                    for p in range(3):
                        g = arr[nushIndex][p]
                        arr[nushIndex][p] = arr[j][p]
                        arr[j][p] = g
        curtime = time.perf_counter() - curtime
##        for i in range(len(arr)):
##            print(f"name: {arr[i][0]} \ntype: {arr[i][1]} \nrank: {arr[i][2]}")
##        print("\n")
        print("{:35} {:6} ms".format(f"PryamVbIborSort {k}", "%.4f" % (curtime*1000)))

    @staticmethod
    def PyzirkiSort(arr, str):
        curtime = time.perf_counter()
        k = 0
        if str == "name" or str == "0":
            k = 0
        elif str == "type" or str == "1":
            k = 1
        elif str == "rank" or str == "2":
            k = 2
        b = True
        while b:
            b = False
            for j in range(len(arr) - 1):
                if arr[j][k] < arr[j + 1][k]:
                    for p in range(3):
                        g = arr[j + 1][p]
                        arr[j + 1][p] = arr[j][p]
                        arr[j][p] = g
                    b = True
        curtime = time.perf_counter() - curtime
##        for i in range(len(arr)):
##            print(f"name: {arr[i][0]} \ntype: {arr[i][1]} \nrank: {arr[i][2]}")
##        print("\n")
        print("{:35} {:6} ms".format(f"PyzirkiSort {k}", "%.4f" % (curtime*1000)))

    @staticmethod
    def PryamVkluchSort(arr, str):
        curtime = time.perf_counter()
        k = 0
        if str == "name" or str == "0":
            k = 0
        elif str == "type" or str == "1":
            k = 1
        elif str == "rank" or str == "2":
            k = 2
        for i in range(1, len(arr)):
            current = [arr[i][0], arr[i][1], arr[i][2]]
            j = i - 1
            while j >= 0 and arr[j][k] < current[k]:
                for p in range(3):
                    arr[j + 1][p] = arr[j][p]
                j -= 1
            for r in range(3):
                arr[j + 1][r] = current[r]
        curtime = time.perf_counter() - curtime
##        for i in range(len(arr)):
##            print(f"name: {arr[i][0]} \ntype: {arr[i][1]} \nrank: {arr[i][2]}")
##        print("\n")
        print("{:35} {:6} ms".format(f"PryamVkluchSort {k}", "%.4f" % (curtime*1000)))

    @staticmethod
    def ShakerSort(arr, str):
        curtime = time.perf_counter()
        k = 0
        if str == "name" or str == "0":
            k = 0
        elif str == "type" or str == "1":
            k = 1
        elif str == "rank" or str == "2":
            k = 2
        b = True
        while b:
            b = False
            for j in range(len(arr) - 1):
                if arr[j][k] > arr[j + 1][k]:
                    for p in range(3):
                        g = arr[j + 1][p]
                        arr[j + 1][p] = arr[j][p]
                        arr[j][p] = g
                    b = True
            if not b:
                break
            b = False
            for j in range(len(arr) - 2, -1, -1):
                if arr[j][k] > arr[j + 1][k]:
                    for p in range(3):
                        g = arr[j + 1][p]
                        arr[j + 1][p] = arr[j][p]
                        arr[j][p] = g
                    b = True
        curtime = time.perf_counter() - curtime
##        for i in range(len(arr)):
##            print(f"name: {arr[i][0]} \ntype: {arr[i][1]} \nrank: {arr[i][2]}")
##        print("\n")
        print("{:35} {:6} ms".format(f"ShakerSort {k}", "%.4f" % (curtime*1000)))

    @staticmethod
    def MetodShellaSort(arr, str):
        curtime = time.perf_counter()
        k = 0
        if str == "name" or str == "0":
            k = 0
        elif str == "type" or str == "1":
            k = 1
        elif str == "rank" or str == "2":
            k = 2
        gap = len(arr)
        while gap > 0:
            for i in range(gap, len(arr)):
                current = [arr[i][0], arr[i][1], arr[i][2]]
                j = i
                while j >= gap and arr[j - gap][k] > arr[j][k]:
                    for p in range(3):
                        temp = arr[j][p]
                        arr[j][p] = arr[j - gap][p]
                        arr[j - gap][p] = temp
                    j -= gap
            gap //= 2
        curtime = (time.perf_counter() - curtime)
##        for i in range(len(arr)):
##            print(f"name: {arr[i][0]} \ntype: {arr[i][1]} \nrank: {arr[i][2]}")
##        print("\n")
        print("{:35} {:6} ms\n".format(f"MetodShellaSort {k}", "%.4f" % (curtime*1000)))

class Executer:
    @staticmethod
    def Main():
        print(f"count of elements")
        n = int(input())
        q2 = queues(n)
        q2.GetRes()
        print("\nmain Arr -----|-----\n")
        trap = q2.GetArr()
        for i in range(3):
            Sorts.PryamVbIborSort(trap, str(i))   # 1
            Sorts.PyzirkiSort(trap, str(i))       # 2
            Sorts.PryamVkluchSort(trap, str(i))   # 3
            Sorts.ShakerSort(trap, str(i))        # 4
            Sorts.MetodShellaSort(trap, str(i))   # 5 

if __name__ == "__main__":
    Executer.Main()



