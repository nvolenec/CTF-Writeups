import random

def get_rand_str(length):
    key = '0123456789'
    rtn = ''.join(random.choice(key) for i in range(length))
    return rtn

seed = 2
random.seed(seed)
get_rand_str(16)
get_rand_str(16)
get_rand_str(16)
a = get_rand_str(16)
print( a )


