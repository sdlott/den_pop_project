import numpy

if __name__ == '__main__':
    # 17 Flavors
    flavors = ('Orange Gatorade','Fruit Punch Gatorade', 'Black Cherry Kickstart','Code Red','Dr. Pepper',
               'Mountain Dew','Pepsi','Fruit Punch Hi-C','Pink Lemonade Hi-C','Powerade',
               'Lemonade','Red Cream Soda','Cherry Coke','Rootbeer','Orange Fanta','Sprite','Coke')
    fourths = (25, 50, 75)
    thirds = (33, 66)

    '''
    cases: 
    33, 33, 33
    33, 66
    25, 25, 25, 25
    25, 25, 50
    25, 75
    50, 50
    '''
    cases = numpy.random.randint(6)

    flavor1 = numpy.random.randint(0, 18)
    flavor2 = numpy.random.randint(0, 18)
    flavor3 = numpy.random.randint(0, 18)
    flavor4 = numpy.random.randint(0, 18)
    # case where pop is in thirds
    if(cases == 0):
        {
            print(thirds[0], "%", flavors[flavor1], "", thirds[0], "%", flavors[flavor2], "",
                  thirds[0], "%", flavors[flavor3])
        }
    # case where pop is in fourths
    elif(cases == 1):
        {
            print(thirds[0], "%", flavors[flavor1], "", thirds[1], "%", flavors[flavor2])
        }
    elif (cases == 2):
        {
            print(fourths[0], "%", flavors[flavor1], "", fourths[0], "%", flavors[flavor2], "",
                  fourths[0], "%", flavors[flavor3], "", fourths[0], "%", flavors[flavor4])
        }
    elif (cases == 3):
        {
            print(fourths[0], "%", flavors[flavor1], "", fourths[0], "%", flavors[flavor2], "",
                  fourths[1], "%", flavors[flavor3])
        }
    elif (cases == 4):
        {
            print(fourths[0], "%", flavors[flavor1], "", fourths[2], "%", flavors[flavor2])
        }
    else:
        {
            print(fourths[1], "%", flavors[flavor1], "", fourths[1], "%", flavors[flavor2])
        }