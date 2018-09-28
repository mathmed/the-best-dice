
import random

class Rices:
    def __init__(self):
        print("\n\n****************************************************")
        print("************** WELCOME TO BEST RICE ****************")
        print("****************************************************\n\n")

        self.main()

    def main(self):
        
        # Seting the informations
        dices_ = int(input("Tell the amount of dice you will test:"))
        faces_ = int(input("Tell me how many faces the dice has:"))

        array_sum = self.calc_sum(dices_, faces_)
        array_mult = self.calc_mult(dices_, faces_)
        self.analyze(array_sum, array_mult)

    def calc_sum(self, dices_, faces_):
        
        max_sum = dices_*faces_
        array = self.fill(max_sum+1)

        for i in range(1, 1000000):
            _num = 0
            for j in range(0, dices_):
                _num += random.randint(1, faces_)
            array[_num] = array[_num]+1

        return array
        
    def calc_mult(self, dices_, faces_):
        
        max_sum = dices_*faces_
        array = self.fill(max_sum+1)

        for i in range(0, 1000000):
            _num = 2*(random.randint(1, faces_))                
            array[_num] = array[_num]+1

        return array
        
    def fill(self, max_sum):
        array = []
        for i in range(0, max_sum):
            array.append(0)
        return array

    def analyze(self, array_sum, array_mult):

        print("\n\nresults sum\n")
        cont = 0
        for i in array_sum:
            print("result = "+str(cont)+": "+str(round((i/1000000)*10,2))+"%")
            cont+=1

        print("\n\nresults mult\n")
        cont = 0
        for i in array_mult:
            print("result = "+str(cont)+": "+str(round((i/1000000)*10,2))+"%")
            cont+=1

c = Rices()
