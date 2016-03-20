import fermat_test

digits = open('pi.txt', 'r').read()

for i in range(len(digits)) :
    num = int(digits[i:i+10])
    if fermat_test.fermat_test(num) :
        print i
        print num
        break
