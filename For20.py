def main(n):
    """
    n soni berilgan. n qatorli yulduzchali piramidani satrlar ro'yxati ko'rinishida qaytaring: i-qatorda (1 dan boshlab) n − i ta bo'sh joy va 2·i − 1 ta * bo'lsin. for siklidan foydalaning.
    Argumentlar:
        n(int): qatorlar soni
    Qaytaradi:
        list: natija ro'yxati
    """
    piramida=[]
    for i in range(1,n+1):
        bosh_joy=" "*(n-i)
        yulduz="*"*(2*i-1)
        piramida.append(bosh_joy+yulduz)
    return piramida
print(main(3))
