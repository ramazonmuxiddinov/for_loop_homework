def main(ismlar):
    """
    ilar ro'yxati berilgan. "A" harfi bilan boshlanadigan ilarni yangi ro'yxatga yig'ib qaytaring. for siklidan foydalaning.
    Argumentlar:
        ilar(list): ilar
    Qaytaradi:
        list: natija ro'yxati
    """
    ls=[]
    for i in ismlar:
        if i[0]=="A": 
            ls.append(i)
    return ls
print(main(["Allamurod", "Dilshod", "Akmal", "Sardor"]))
