def oct(L):
    L = int(L)
    spaces = 0
    stars = 0
    for i in range(L):
        print(' ' * (L - spaces) + '*' * (L + stars))
        if(i == L-1):
            break
        spaces += 1
        stars += 2
    for i in range(L-2):
        print(' ' * (L - spaces) + '*' * (L + stars))
    for i in range(L):
        print(' ' * (L - spaces) + '*' * (L + stars))
        spaces -= 1
        stars -= 2

def main():
    L = ''
    while(True):
         L = input('Enter the length of the octagon: ')
         if(int(L) < 2):
             continue
         else:
             break
    oct(L)
    
main()
        


