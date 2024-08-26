import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# 1. Создаем новый DataFrame с нулями
one_hot = pd.DataFrame(np.zeros((len(data), 2)), columns=['human', 'robot'])

# 2. Заполняем столбцы в соответствии с исходными данными
for i, row in data.iterrows():
    if row['whoAmI'] == 'human':
        one_hot.loc[i, 'human'] = 1
    else:
        one_hot.loc[i, 'robot'] = 1

print(one_hot)
