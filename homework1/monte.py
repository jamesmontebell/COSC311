from random import randint
import pandas as pd

def main():
    n = input('Enter the number of times to roll the dice: ')
    n = int(n)
    list = []
    
    for i in range(n):
        list.append(randint(1, 6) + randint(1, 6))
        
    res = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    for val in list:
        res[val] += 1
   
    prob = []
    for i in range(2, 13):
        prob.append(round((res[i] / n), 2))
        
        
    df = pd.DataFrame({'Total': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 'Probability': prob})
    print(df)
              
main()