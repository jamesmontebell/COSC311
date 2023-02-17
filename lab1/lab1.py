words = {}
with open('SciencePaper.txt', 'r') as file:
    new_line = file.readline()
    tokens = []
    for line in file:
        tokens = line.upper().replace(',','').replace(';','').replace('(','').replace(')','')\
        .replace('!','').replace('?','').replace('.','').split()
        for word in tokens:
            try:
                words[word] += 1
            except:
                words[word] = 1
                
print("There are " + str(len(words.keys())) + " words in the document")


summer = words['SUMMERFELT']
waste = words['WASTEWATER']
green = words['GREENHOUSE']
salmon = words['SALMON']


words_reverse = {}
for word,count in words.items():
    try:
        words_reverse[count].append(word)
    except:
        words_reverse[count] = [word]
keys = sorted(words_reverse, reverse=True)

print("The 10 words that appear the most are: ")
i = 0
for key in keys:
    if i > 9:
        break
    print(words_reverse[key])
    i += 1
    
print("Summefelt: " + str(summer) + ", Wastewater: " + str(waste) + ", Greenhouse: "+ str(green) + ", Salmon: " +str(salmon))

one = []
two = []
five = []
ten = []

for word in words_reverse[1]:
    one.append(word)
    
for word in words_reverse[2]:
    two.append(word)
    
for word in words_reverse[5]:
    five.append(word)
    
for word in words_reverse[10]:
    ten.append(word)
    
## have to print to a new file because output is too big to copy or screenshot
with open('task2.1.txt', 'w') as new_file:
    print(str(one), file = new_file)

print("2: "+ '\n' + str(two))

print("5: "+ '\n' + str(five))

print("10: " + '\n'+ str(ten))


avg_len = [sum([len(word) for word in value]) / len(value) for value in words_reverse.values()]
appearances = list(words_reverse.keys())

import matplotlib.pyplot as plt 
plt.bar(appearances, avg_len)

    

        