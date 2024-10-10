# in Python zip is nothing to do with archives or compression

def main():
    '''We use zip to combine unrelatetd structures into a single structure '''
    days_l = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    fruits_t = ('Banana', 'Orange', 'Kiwi', 'Durian')
    drinks_s = {'Coffee', 'Tea', 'Water', 'Calpico'}

    # zip lets us cmbine any iterable structures together
    z = zip(days_l, fruits_t, drinks_s)
    print( z, type(z) )
    for day, fruit, drink in z:
        print(f'On {day} I ate {fruit} with {drink}')

if __name__ == '__main__':
    main()