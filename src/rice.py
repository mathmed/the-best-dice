
import random

class Dice:
    def __init__(self):
        print("\n\n****************************************************")
        print("************** WELCOME TO BEST DICE ****************")
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
            print("result = "+str(cont)+": "+str(round((i/1000000)*100,2))+"%")
            cont+=1

        print("\n\nresults mult\n")
        cont = 0
        for i in array_mult:
            print("result = "+str(cont)+": "+str(round((i/1000000)*100,2))+"%")
            cont+=1

        faces = int(len(array_mult)/2)
        cont_mult = 0
        for i in range (faces, len(array_mult)):
            cont_mult+=round((array_mult[i]/1000000)*100,2)
        cont_sum = 0
        for i in range(faces, len(array_sum)):
            cont_sum+=round((array_sum[i]/1000000)*100,2)


        print("\nchance to take a number above "+str(faces)+" with added dice: "+str(round(cont_sum,2))+"%")
        print("\nchance to take a number below "+str(faces)+" with added dice: "+str(round(100-cont_sum, 2))+"%\n")
        print("\nchance to take a number above "+str(faces)+" with dice multiplied by 2: "+str(round(cont_mult,2))+"%")
        print("\nchance to take a number below "+str(faces)+" with dice multiplied by 2: "+str(round(100-cont_mult,2))+"%")

        if(cont_sum > cont_mult):
            print("\nthe best choice is to play dices added\n")
        elif(cont_mult > cont_sum):
            print("\nthe best choice is to play dice multiplied by 2\n")
        else:
            print("\nthe choice does not matter\n")

c = Dice()
