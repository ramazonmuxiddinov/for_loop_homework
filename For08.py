def main(n):
    """
    n soni berilgan. 1 + 1/2 + 1/3 + … + 1/n yig'indisini hisoblang va 2 xona aniqlikda yaxlitlab qaytaring. for siklidan foydalaning.
    Argumentlar:
        n(int): son
    Qaytaradi:
        float: yig'indi
    """
    ls = 0
    for i in range(1,n+1):
        ls+=1/i
    return round(ls,2)
print(main(4))
