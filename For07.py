def main(n):
    """
    n soni berilgan. 1 dan n gacha (n ham kiradi) bo'lgan toq sonlar yig'indisini qaytaring. for siklidan foydalaning.
    Argumentlar:
        n(int): son
    Qaytaradi:
        int: natija
    """
    ls=0
    for i in range(1,n+1):
        if i%2!=0:
            ls+=i
    return ls
print(main(10))
