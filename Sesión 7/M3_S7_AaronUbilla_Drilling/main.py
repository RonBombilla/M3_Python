lista = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]

for i in lista:
    if i[0] != 0:
        for j in i:
            if j != 0:
                print(j)
        print('-----------')
