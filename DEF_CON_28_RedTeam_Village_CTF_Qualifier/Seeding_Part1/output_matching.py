import random

seed_list = [2,20,48,66,69]
seed_dict = { 2 : 'vlmvdmioiddevvea', 20 : 'edveoaillmseiems', 48 : 'esrrissmediadise', 66 : 'eiirmasidieealed', 69 : 'oadiroesrmoeiiao' }
base_str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key_sz_list = list(range(10,20))

def get_rand_str(key,length):
    rtn = ''.join(random.choice(key) for i in range(length))
    return rtn

def find_occurrences(s, ch):
        return [i for i, letter in enumerate(s) if letter == ch]

def try_match(seed, try_str, key_sz ):
    match_str = seed_dict[seed]
    #note random_str will be the same length as the match_str, 16
    uniq_chars = set(try_str)
    this_try = ''.join('*'*key_sz)
    for a in uniq_chars:
        index_list = find_occurrences( try_str, a )
        prev = '*'
        for b in index_list:
            p = base_str.find(a)
            this_try = this_try[0:p]+match_str[b]+this_try[p+1:]

            if prev != match_str[b] and prev != '*':
                #mismatch
                return 'fail'
            prev = match_str[b]
    print( 'no mismatches for seed '+str(seed)+' with key length '+str(key_sz)+'.\n'+str(try_str)+' -> \n'+str(this_try)+'  =~ \n'+str(match_str)+'\n' )
    return 'success '+str(this_try)


for s in seed_list:
    for key_sz in key_sz_list:
        key = base_str[0:key_sz]
        a = ''
        random.seed(s)
        for i in range(4):
            a = get_rand_str(key,16)
        try_match(s, a, key_sz)

