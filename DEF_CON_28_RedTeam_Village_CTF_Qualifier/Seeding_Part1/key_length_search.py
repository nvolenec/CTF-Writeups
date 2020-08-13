import random

def get_rand_str(key,length):
    rtn = ''.join(random.choice(key) for i in range(length))
    return rtn

base_str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

seed_list = [2,20,48,66,69]
key_sz_list = list(range(10,20))

for s in seed_list:
    print( 'seed is '+str(s) )
    for key_sz in key_sz_list:
        key = base_str[0:key_sz]
        a = ''
        random.seed(s)
        for i in range(4):
            a = get_rand_str(key,16)
        print( str(key_sz) + ':  ' + str(a) )


