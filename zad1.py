import math
import scipy.special
import fileinput

class Code():

    def __init__(self, codewords):
        n = len(codewords[0])
        for a in codewords:
            if n != len(a):
                raise ValueError("Kod nije blok kod")
        self.codewords = codewords
    
    def isLinear(self):
        n = len(self.codewords[0])
        zero = n*"0"

        if zero not in self.codewords:
            return False

        for i in range(len(self.codewords)):
            for j in range(i + 1, len(self.codewords)):
                novi = ""
                for k in range(n):
                    if self.codewords[i][k] == self.codewords[j][k]:
                        novi += "0"
                    else:
                        novi += "1"
                if novi not in self.codewords:
                    return False
        return True

    def distance(self):
        distance = 100000000
        if self.isLinear():
            n = len(self.codewords[0])
            zero = n*"0"

            for a in self.codewords:
                if a != zero:
                    count = 0
                    for b in a:
                        if b == "1":
                            count += 1
                    if count < distance:
                        distance = count
        else:
            length = len(self.codewords[0])
            for i in range(len(self.codewords)):
                line1 = self.codewords[i]
                for j in range(i + 1, len(self.codewords)):
                    count = 0
                    line2 = self.codewords[j]
                    for k in range(length):
                        if(line1[k] != line2[k]):
                            count += 1
                    if(count < distance):
                        distance = count
        return distance

    def find_or_correct(self):
        distance = self.distance()
        print("Može otkriti: " + str(distance - 1) + " grešaka, a ispraviti: " + str(math.floor((distance - 1) / 2)) + " grešaka")
        return

    def n_k(self):
        if(not self.isLinear()):
            print("Kod nije linearan pa ne možemo govoriti o n,k oznaci")
            return
        length = len(self.codewords)
        n = len(self.codewords[0])
        print("n = " + str(n) + ", k = " + str(math.log2(length)))
        return

    def perfect(self):
        m = len(self.codewords)
        n = len(self.codewords[0])
        distance = self.distance()
        t = math.floor((distance - 1) / 2)
        nazivnik = 0
        for i in range(t + 1):
            nazivnik += scipy.special.binom(n, i)
        if(nazivnik == 0):
            return False
        if m == (2**n)/nazivnik:
            return True
        else:
            return False

file = input("Unesite ime datoteke sa kodnim riječima: ")

with open(file) as f_obj:
    codewords = f_obj.read().splitlines()

code = Code(codewords)

print("zad1: ")
code.n_k()
print("zad2: " + str(code.distance()))
print("zad3: ")
code.find_or_correct()
print("zad4: " + str(code.perfect()))
print("zad5: " + str(code.isLinear()))

