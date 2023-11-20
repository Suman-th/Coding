def Romantoint(S):

    roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500}

    res = 0

    for i in range(len(S)):
        if i>0 and roman_dict[S[i]] > roman_dict[S[i-1]]:
            res += roman_dict[S[i]] - 2*roman_dict[S[i-1]]
        else:
            res += roman_dict[S[i]]
    return res

S = str(input())
print(Romantoint(S))