def minion_game(string):
#identifying what a vowel is (v = vowels, c = consonants)
    vList = set(['a','e','i','o','u','A','E','I','O','U'])
#initializing vowel and consonant count
    c = 0
    v = 0
    n = len(string)
#iterating based on the string given and its length
    for i, l in enumerate(string):
#if l is a vowel, add to vowel count 
        if l in vList:
            v += n-i
#otherwise, l is not a vowel–add to consonant count
        else:
            c += n-i
#when vowel count and consonant count is equal, neither win-draw
    if v == c:
        print("Draw")
#otherwise, when vowel count greater than consonant count, kevin wins
    elif v > c:
        print("Kevin {}".format(v))
#otherwise, when consonant count greater than vowel count, stuart wins
    else:
        print("Stuart {}".format(c))
        
if __name__ == '__main__':
    s = input()
    minion_game(s)
