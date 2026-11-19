def main(n):
    """
    n soni berilgan. 0 dan n gacha (n ham kiradi) bo'lgan sonlarni bo'sh joy bilan ajratilgan satr ko'rinishida qaytaring. for siklidan foydalaning.
    Argumentlar:
        n(int): son
    Qaytaradi:
        str: natija satri
    """
    ls=""
    for i in range(n+1):
       ls+=str(i)+" "
    return f""}"
print(main(3))
