def main(n):
    """
    n soni berilgan. Uning 1 dan 10 gacha ko'paytirish jadvalini "n x i = natija" ko'rinishidagi satrlar ro'yxati sifatida qaytaring. for siklidan foydalaning.
    Argumentlar:
        n(int): son
    Qaytaradi:
        list: natija ro'yxati
    """
    ls=[]
    for i in range(1,11):
        ls.append(f"{n}x{i}={n*i}")
    return ls
print(main(7))
