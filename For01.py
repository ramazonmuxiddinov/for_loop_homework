def main(n):
    """
    n soni berilgan. 0 dan n gacha (n ham kiradi) bo'lgan sonlarni ro'yxat ko'rinishida qaytaring. for siklidan foydalaning.
    Argumentlar:
        n(int): son
    Qaytaradi:
        list: natija ro'yxati
    """
    ls=[]
    for i in range(0,n+1):
        ls.append(i)
    return ls
print(main(5))
print(main(0))

