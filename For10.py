def main(ismlar):
    """
    Kichik harflar bilan yozilgan ismlar ro'yxati berilgan. Har bir ismni bosh harf bilan boshlab, yangi ro'yxat qaytaring. for siklidan foydalaning.
    Argumentlar:
        ismlar(list): ismlar
    Qaytaradi:
        list: natija ro'yxati
    """
    ls=[]
    for i in ismlar:
        ls.append(i.capitalize())
    return ls
print(main(["allamurod", "akmal", "dilshod"]))
