def main(a, b):
    """
    a va b sonlari berilgan (a < b). a dan b gacha (ikkalasi ham kiradi) bo'lgan sonlarni ro'yxat ko'rinishida qaytaring. for siklidan foydalaning.
    Argumentlar:
        a(int): boshi
        b(int): oxiri
    Qaytaradi:
        list: natija ro'yxati
    """
    ls=[]
    for i in range(a,b+1):
        ls.append(i)
    return ls
print(main(2020,2026))
