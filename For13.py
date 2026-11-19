def main(n):
    """
    n soni berilgan. 1 dan n gacha (n ham kiradi) bo'lgan, 3 ga yoki 5 ga bo'linadigan sonlar yig'indisini qaytaring. for siklidan foydalaning.
    Argumentlar:
        n(int): son
    Qaytaradi:
        int: natija
    """
    sum=0
    for i in range(1,n+1):
        if i%3==0 or i%5==0:
            sum+=i
    return sum
print(main(10))
