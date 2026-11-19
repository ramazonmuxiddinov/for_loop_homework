def main(n):
    """
    Allamurodda n ta har xil kitob bor. Ularni javonga necha xil tartibda terish mumkinligini (n!) hisoblab qaytaring. math modulidan foydalanmang. for siklidan foydalaning.
    Argumentlar:
        n(int): kitoblar soni
    Qaytaradi:
        int: natija
    """
    f=1
    for i in range(1,n+1):
        f*= i
    return f
print(main(5))
