import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
lb = LabelBinarizer()
one_hot_data = lb.fit_transform(data['whoAmI'])
one_hot_df = pd.DataFrame(one_hot_data, columns=lb.classes_)
data_one_hot = pd.concat([data, one_hot_df], axis=1)
print(data_one_hot.head())