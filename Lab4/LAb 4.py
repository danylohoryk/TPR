import pandas as pd
df = pd.read_csv('ratings.csv')

names = ['Audi', 'Volkswagen', 'Skoda', 'BMW','Mercedes','Opel']
def fun(row,name):
    return row['Вага']*row[name]
list_=[]
for i in range(len(names)):
    list_.append(round(sum(df.apply(fun,name=names[i], axis = 1)),2))
result = list(zip(names,list_))

result_df = pd.DataFrame(result,columns=['Автомобіль','Оцінка'])
result_df = result_df.sort_values('Оцінка',ascending = False)
print(result_df)