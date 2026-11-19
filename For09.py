def main(narx):
    """
    Allamurod bozordan olma olmoqchi. 1 kg olma narxi berilgan. 1 dan 10 kg gacha olmaning narxlarini ro'yxat ko'rinishida qaytaring. for siklidan foydalaning.
    Argumentlar:
        narx(int): 1 kg narxi
    Qaytaradi:
        list: natija ro'yxati
    """
    ls=[]
    for i in range(1,11):
        ls.append(narx*i)
    return ls
print(main(12000))
