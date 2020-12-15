import pandas as pd

file = open('Horyk_lab2.csv', 'r')
tableList = list(map(float, file.readline().split(',')))
file.close()

m1, d1, p1, d2, p2, m2, d21, p21, d22, p22, p33, p34, p31, p32 = tableList
A = -m1 + 5 * (p1 * d1 + p2 * d2)
B = -m2 + 5 * (p21 * d21 + p22 * d22)
Ca = p33 * (-m1 + 4 * (p31 * d1 + p32 * d2)) + p34 * 0
Cb = p33 * (-m2 + 4 * (p31 * d21 + p32 * d22)) + p34 * 0
results = pd.DataFrame(list(zip(['Варіант А', 'Варіант Б', 'Варіант Ва', 'Варіант Вб'], [A, B, Ca, Cb])))
results.columns = ['Стратегія', 'Очікуваний дохід']
print(results)
print('Найкращим є: {0}'.format(results['Очікуваний дохід'].max()))
