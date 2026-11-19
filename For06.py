def main(a, b):
    """
    a va b sonlari berilgan (a < b). a dan b gacha (ikkalasi ham kiradi) bo'lgan barcha sonlar yig'indisini qaytaring. for siklidan foydalaning.
    Argumentlar:
        a(int): boshi
        b(int): oxiri
    Qaytaradi:
        int: natija
    """
    ls=0
    for i in range(a,b+1):
        ls+=i
    return ls
print(main(1,100))