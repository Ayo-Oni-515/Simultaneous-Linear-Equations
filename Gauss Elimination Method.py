question_1 = [[1, 2, -1, 3.1], [-3, 1, 1, 1.4], [-1, -1, 4, 7.3]]
question_2 = [[-2, 3, -1, -0.6], [3, 1, -2, -3.30], [1, 2, 1, 1.9]]
question_3 = [[2, -3, -1, -3.7], [-3, 3, -1, -1.0], [4, -2, 3, 4.4]]
question_4 = [[3, 2, -4, -5.9], [7, -4, 3, -5.7], [-2, 2, 5, -6.3]]
question_5 = [[4, -2, 6, -2, 11], [-3, 2, 2, -4, -9.9], [1, 5, -2, -2, 3.3], [2, 1, -3, 1, -5.5]]
question_6 = [[3, 3, -2, 7.6], [2, -4, 1, 1.4], [-1, -2, 5, -6.3]]
question_7 = [[2, -4, 6, 1.4], [3, 1, -3, -9.8], [-1, 2, -3, -0.7]]
question_8 = [[5, -3, -1, 20.3], [2, 2, -3, -4.0], [-3, -4, 5, 9.6]]
question_9 = [[2, -3, -1, 5.2], [-3, -1, -4, 3.9], [5, 3, -4, -11.3]]
question_10 = [[2, -3, -1, 1, 11.7], [-3, 1, 2, -1, -11.5], [-1, -2, 3, 5, -0.4], [3, 3, -1, 1, 3.6]]
#Declaraton Of The Gaussian-Elimination Function.
def gaussian(var):
    if len(var) == 3:
        multiplier1 = var[1][0] / var[0][0]   
        for i in range(0, len(var) + 1):
            new = multiplier1 * var[0][i]
            var[1][i] = var[1][i] - new
        if var[1][1] == 0 or var[1][2] == 0:
            print("MATH ERROR")
            return
        multiplier2 = var[2][0] / var[0][0]
        for i in range(0, len(var) + 1):
            new = multiplier2 * var[0][i]
            var[2][i] = var[2][i] - new
        if var[2][1] == 0 or var[2][2] == 0:
            print("MATH ERROR")
            return
        multiplier3 = var[2][1] / var[1][1] 
        for i in range(0, len(var) + 1):
            new = multiplier3 * var[1][i]
            var[2][i] = var[2][i] - new
        if var[2][2] == 0:
            print("MATH ERROR")
            return
        if var[2][2] == 0 or var[1][1] == 0 or var[0][0] == 0:
            print("MATH ERROR")
            return
        else:
            x3 = var[2][3] / var[2][2]                                              #Computation of results: Back Substitution. 
            x2 = (var[1][3] - (var[1][2] * x3)) / var[1][1]                         #Computation of results: Back Substitution.
            x1 = (var[0][3] - (var[0][2] * x3) - (var[0][1] * x2)) / var[0][0]      #Computation of results: Back Substitution.
            x1 = round(x1, 3)                                                       #Rounding up results.
            x2 = round(x2, 3)                                                       #Rounding up results.
            x3 = round(x3, 3)                                                       #Rounding up results.
            print("x1 =", x1," ", "x2 =", x2," ", "x3 =", x3)
            return
    elif len(var) == 4:
        multiplier1 = var[1][0] / var[0][0]   
        for i in range(0, len(var) + 1):
            new = multiplier1 * var[0][i]
            var[1][i] = var[1][i] - new
        if var[1][1] == 0 or var[1][2] == 0 or var[1][3] == 0:
            print("MATH ERROR")
            return
        multiplier2 = var[2][0] / var[0][0]
        for i in range(0, len(var) + 1):
            new = multiplier2 * var[0][i]
            var[2][i] = var[2][i] - new
        if var[2][1] == 0 or var[2][2] == 0 or var[2][3] == 0:
            print("MATH ERROR")
            return
        multiplier3 = var[3][0] / var[0][0]
        for i in range(0, len(var) + 1):
            new = multiplier3 * var[0][i]
            var[3][i] = var[3][i] - new
        if var[3][1] == 0 or var[3][2] == 0 or var[3][3] == 0:
            print("MATH ERROR")
            return
        multiplier4 = var[3][1] / var[2][1] 
        for i in range(0, len(var) + 1):
            new = multiplier4 * var[2][i]
            var[3][i] = var[3][i] - new
        if var[3][2] == 0 or var[3][3] == 0:
            print("MATH ERROR")
            return
        multiplier5 = var[2][1] / var[1][1] 
        for i in range(0, len(var) + 1):
            new = multiplier5 * var[1][i]
            var[2][i] = var[2][i] - new
        if var[2][2] == 0 or var[2][3] == 0:
            print("MATH ERROR")
            return
        multiplier6 = var[3][2] / var[2][2]
        for i in range(0, len(var) + 1):
            new = multiplier6 * var[2][i]
            var[3][i] = var[3][i] - new
        if var[3][3] == 0:
            print("MATH ERROR")
            return
        if var[3][3] == 0 or var[2][2] == 0 or var[1][1] == 0 or var[0][0] == 0:
            print("MATH ERROR")
            return
        else:
            x4 = var[3][4] / var[3][3]                                                               #Computation of results: Back Substitution.  
            x3 = (var[2][4] - (var[2][3] * x4)) / var[2][2]                                          #Computation of results: Back Substitution. 
            x2 = (var[1][4] - (var[1][2] * x3) - (var[1][3] * x4)) / var[1][1]                       #Computation of results: Back Substitution.
            x1 = (var[0][4] - (var[0][1] * x2) - (var[0][2] * x3) - (var[0][3] * x4)) / var[0][0]    #Computation of results: Back Substitution.
            x1 = round(x1, 3)                                                                        #Rounding Up results.
            x2 = round(x2, 3)                                                                        #Rounding Up results.
            x3 = round(x3, 3)                                                                        #Rounding Up results.
            x4 = round(x4, 3)                                                                        #Rounding Up results.
            print("x1 =", x1," ", "x2 =", x2," ", "x3 =", x3," ", "x4 =", x4)
        return
import time
gaussian(question_1)
time.sleep(1)
gaussian(question_2)
time.sleep(1)
gaussian(question_3)
time.sleep(1)
gaussian(question_4)
time.sleep(1)
gaussian(question_5)
time.sleep(1)
gaussian(question_6)
time.sleep(1)
gaussian(question_7)
time.sleep(1)
gaussian(question_8)
time.sleep(1)
gaussian(question_9)
time.sleep(1)
gaussian(question_10)
time.sleep(1)