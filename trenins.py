def rezultats(sk1, sk2):
    if sk1<6 and sk2<6:
        rez = sk1*sk2
    else:
        rez = sk1+sk2
    return rez

for skaitlis in range(1, 11, 2):        #range  - funkcija, kas skaita skaitļus
    for otrs in range(2, 11, 2):
        print("pirmais skaitlis:", skaitlis,"otrais skaitlis:", otrs, "rezultāts:", rezultats(skaitlis, otrs))

skaitlis1 = 7
skaitlis2 = 4

print("pirmais skaitlis:", skaitlis1)
print("otrais skaitlis:", skaitlis2)
print("rezultats:", rezultats(skaitlis1, skaitlis2))


saraksts1 = [1, 7, 5, 9, 35, 2]
saraksts2 = [4, 2, 2, 39, 6, 4]

for skaititajs in range(len(saraksts1)):
    print("pirmais skaitlis:", saraksts1[skaititajs],"otrais skaitlis:", saraksts2[skaititajs],"rezultāts:", rezultats(skaitlis, otrs))

skaitlu_pari = [[2,5][4,6][3,4][7,8]]

print("--------------------")

for 1 in range(len(skaitlu_pari))

print("--------------------")

for elements in skaitlu_pari[:-1]:
    print("pirmais skaitlis:", elements[0], "otrais skaitlis:", elements[1], "rezultāts:", rezultats(elements[0], elements[1]))