import random

def rand_x_digit_num(x, leading_zeroes=True):
    """Return an X digit number, leading_zeroes returns a string, otherwise int"""
    if not leading_zeroes:
        # wrap with str() for uniform results
        return random.randint(10**(x-1), 10**x-1)  
    else:
        if x > 6000:
            return ''.join([str(random.randint(0, 9)) for i in xrange(x)])
        else:
            return '{0:0{x}d}'.format(random.randint(0, 10**x-1), x=x)
    

def is_turkish_id(x):
    if len(str(x)) != 11:
        return False
    str_id = str(x)
   
    #ilk 10 rakam toplamı mod 10 esit mi 11. hanedeki rakam kontrolu
    lst_id = [int(n) for n in str_id if n.isdigit()]
    if lst_id[0] == 0:
        return False
    
    #ilk 10 rakam toplami
    first_10_sum = sum(lst_id[:10])
    if first_10_sum % 10 != lst_id[-1]:
        return False
    
    total_odds = sum(lst_id[0::2][:-1])
    total_evens = sum(lst_id[1::2][:-1])

    is_10 = (total_odds * 7 +  total_evens * 9) % 10 == lst_id[9]
    is_11 = (total_odds * 8) % 10 == lst_id[-1]
    
    if not is_10 or not is_11:
        return False
    else:
        return True

def tcuret(n):
    i = 0    
    while True:
        rnd11 = rand_x_digit_num(11)
        if is_turkish_id(rnd11) == True and i < n:
            #print(rnd11, " gecerli bir tckimlik numarasi")
            yield rnd11
            i = i + 1
        if i >= n:
            break
        
        
def main():
    
    '''
    str_adet = input("Kaç adet TC üretilsin?")
    i = 0
    
    while True:
        rnd11 = rand_x_digit_num(11)
        #print("Rastgele sayi:", rnd11, " icin tckimlik kontrolu yapiliyor...")
        if is_turkish_id(rnd11) == True and i < int(str_adet):
            print(rnd11, " gecerli bir tckimlik numarasi")
            i = i + 1
        elif i >= int(str_adet):
            break
    '''
    str_adet = input("Kaç adet TC üretilsin?")
    for tc in tcuret(int(str_adet)):
        print("TC: ", tc)


if __name__ == "__main__":
    main()
