import pandas as pd

file = pd.read_csv('Horyk_lab1.csv')
file = file.drop('cases', axis='columns')
columns = list(file)

valdValues = []
maxValues = []
a = 0.5
gurvicValues = {}
laplassValues1 = {}
laplassValues2 = {}
p = [0.5, 0.35, 0.15]

for i in columns:
    valdValues.append(file[i].min())
    maxValues.append(file[i].max())
    gurvicValues[i] = max(file[i]) * 0.5 + min(file[i]) * (1 - a)
    for j in range(len(file[i])):
        if i not in laplassValues1:
            laplassValues1[i] = 0
        laplassValues1[i] += round(file[i][j] / len(columns), 2)
        if i not in laplassValues2:
            laplassValues2[i] = 0
        laplassValues2[i] += round(file[i][j] * p[j], 2)

gurvicValues = list(gurvicValues.values())
laplassValues1 = list(laplassValues1.values())
laplassValues2 = list(laplassValues2.values())

print('Критерій Вальда\n{0}\nНайкращим з найгірших є: {1}\n'.format(valdValues, max(valdValues)))
print('Максимальний\n{0}\nНайкращим з найкращих є: {1}\n'.format(maxValues, max(maxValues)))
print('Гурвіца\n{0}\nНайкращий є: {1}\n'.format(gurvicValues, max(gurvicValues)))
print('Лапласса при рівномірних умовах\n{0}\nНайкращий є: {1}\n'.format(laplassValues1, max(laplassValues1)))
print('Лапласса при p1=0.5, p2=0.35, p3=0.15\n{0}\nНайкращий є: {1}\n'.format(laplassValues2, max(laplassValues2)))

results = pd.DataFrame(list(zip(valdValues, maxValues, gurvicValues, laplassValues1, laplassValues2)),
                       columns=['Vald', 'Maximum', 'Gurvic', 'Laplass', 'Laplass2'], index=columns)
print(results)
