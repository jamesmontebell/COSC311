def tree(outlook, humidity, wind):
    if(outlook == 'rain'):
        if(wind == 'strong'):
            print('no')
        else:
            print('yes')
    elif(outlook == 'overcast'):
        print('yes')
    else:   
        if(humidity == 'high'):
            print('no')
        else:
            print('yes')
            
tree('sunny', 'high', 'weak')
tree('overcas', 'normal', 'strong')
tree('rain', 'high', 'strong')