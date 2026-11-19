def main(n):
    """
    n soni berilgan (n ≥ 2). Fibonachchi ketma-ketligining dastlabki n ta hadini ro'yxat ko'rinishida qaytaring (0, 1, 1, 2, 3, ...). for siklidan foydalaning.
    Argumentlar:
        n(int): hadlar soni
    Qaytaradi:
        list: natija ro'yxati
    """
    
    f1=0
    f2=1
    ls = [f1, f2]
    for i in range(0,n-2):
        f3 = f1+f2
        f1=f2
        f2=f3
        ls.append(f3)
    return ls
        
        
    
print(main(10))
