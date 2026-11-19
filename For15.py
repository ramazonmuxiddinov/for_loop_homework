def main(oylik, oylar, foiz):
    """
    Allamurod har oy oxirida jamg'armaga bir xil summa qo'yadi, jamg'armaga esa har oy foiz qo'shiladi. Oylik qo'yilma, oylar soni va oylik foiz berilgan. Har oy: summa = summa · (100 + foiz) / 100 + oylik. Yakuniy summani 2 xona aniqlikda yaxlitlab qaytaring. for siklidan foydalaning.
    Argumentlar:
        oylik(int): oylik qo'yilma
        oylar(int): oylar soni
        foiz(int): oylik foiz
    Qaytaradi:
        float: yakuniy summa
    """
    sum=0
    for i in range(oylar):
        sum=sum*(100+foiz)/100+oylik
    return round(sum,2)
print(main(1000000,3,2))

