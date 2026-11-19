def main(ballar):
    """
    Allamurodning test ballari ro'yxati berilgan. Har bir ballni bahoga aylantirib, ils ro'yxatini qaytaring: 86–100 → 5, 71–85 → 4, 56–70 → 3, qolganlari → 2. for siklidan foydalaning.
    Argumentlar:
        ballar(list): ballar
    Qaytaradi:
        list: natija ro'yxati
    """
    ls=[]
    for ball in ballar:
        if ball>=86:
            ls.append(5)
        elif ball>=71:
            ls.append(4)
        elif ball>=56:
            ls.append(3)
        else:
            ls.append(2)
    return ls
print(main([87, 92, 78, 60, 40]))
