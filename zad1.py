from math import log2, floor, factorial
from fileinput import close

class Code():

    # Binomial coefficient callculator 
    def binomial(self, n, k):
        if k < 0 or k > n:
            return 0
        if k == 0 or k == n:
            return 1
        binom = 1
        for i in range(min(k, n - k)):
            binom = binom * (n - i) // (i + 1)
        return binom

    def __init__(self, codewords):
        n = len(codewords[0])
        for a in codewords:
            if n != len(a):
                raise ValueError("Kod nije blok kod")
            for b in a:
                if b != '0' and b != '1':
                    raise ValueError("kod nije binaran")
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
        print("Može otkriti: " + str(distance - 1) + " , a ispraviti: " + str(floor((distance - 1) / 2)))
        return

    def n_k(self):
        if(not self.isLinear()):
            print("Kod nije linearan pa ne možemo govoriti o n,k oznaci")
            return
        length = len(self.codewords)
        n = len(self.codewords[0])
        print("n = " + str(n) + ", k = " + str(log2(length)))
        return

    def perfect(self):
        m = len(self.codewords)
        n = len(self.codewords[0])
        distance = self.distance()
        t = floor((distance - 1) / 2)
        nazivnik = 0
        for i in range(t + 1):
            nazivnik += self.binomial(n, i)
        if(nazivnik == 0):
            return False
        if m == (2**n)/nazivnik:
            return True
        else:
            return False


file = input("Unesite ime datoteke sa kodnim riječima: ")

try:
    with open(file) as f_obj:
        codewords = f_obj.read().splitlines()

    code = Code(codewords)

    print("n i k zadanog koda K su: ")
    code.n_k()
    print("Udaljenost d(K) koda K je: " + str(code.distance()))
    print("Sposobnost  koda  da  otkrije  i  ispravi pogrešku: ")
    code.find_or_correct()
    perf = code.perfect()
    if(perf):
        print("Je li zadani kôd perfektan?: " + "JE!")
    else:
        print("Je li zadani kôd perfektan?: " + "NIJE!")
    lin = code.isLinear()
    if(lin):
        print("Je li zadani kôd linearan?: " + "JE!")
    else:
        print("Je li zadani kôd linearan?: " + "NIJE!")
    f_obj.close()
except FileNotFoundError as a:
    msg = "Ne mogu naći datoteku {0}.".format(file)
    print(msg)
except IOError as a:
    msg = "IOError - pogrešan put"
    print(msg)
except OSError as a:
    msg = "IOError - pogrešan put"
    print(msg)
except ValueError as a:
    msg = str(a)
    print(msg)
finally:
    input("Pritisnite enter za kraj programa")
