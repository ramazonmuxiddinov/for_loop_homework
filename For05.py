def main(a, b):
    """
    a va b sonlari berilgan (a < b). b dan a gacha (ikkalasi ham kiradi) kamayish tartibida sonlarni ro'yxat ko'rinishida qaytaring. for siklidan foydalaning.
    Argumentlar:
        a(int): kichik son
        b(int): katta son
    Qaytaradi:
        list: natija ro'yxati
    """
    ls=[]
    for i in range(b,a-1,-1):
        ls.append(i)
    return ls
print(main(1,5))
