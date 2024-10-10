# in Python zip is nothing to do with archives or compression

def main():
    '''We use zip to combine unrelatetd structures into a single structure '''
    days_l = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    fruits_t = ('Banana', 'Orange', 'Kiwi')

    # zip lets us cmbine any iterable structures together
    z = zip(days_l, fruits_t)
    print( z, type(z) )

if __name__ == '__main__':
    main()