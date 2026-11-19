def main(n):
    """
    n soni berilgan. 2 dan n gacha (n ham kiradi) bo'lgan tub sonlarni ro'yxat ko'rinishida qaytaring. for siklidan foydalaning.
    Argumentlar:
        n(int): son
    Qaytaradi:
        list: natija ro'yxati
    """
    tublar=[]
    for num in range(2,n+1):
        tub=True
        for i in range(2,num):
            if num%i==0:
                tub=False
                break
        if tub:
            tublar.append(num)
    return tublar
print(main(20))
