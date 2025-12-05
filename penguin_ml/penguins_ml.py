import pickle

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

penguin_df = pd.read_csv('penguins.csv')
penguin_df.dropna(inplace=True)
output = penguin_df['species']
features = penguin_df[[
    'island', 'bill_length_mm', 'bill_depth_mm', 
    'flipper_length_mm', 'body_mass_g', 'sex'
]]
features = pd.get_dummies(features)
output, uniques = pd.factorize(output)
x_train, x_test, y_train, y_test = train_test_split(features, output, test_size=.8)
rfc = RandomForestClassifier(random_state=17)
rfc.fit(x_train.values, y_train)
y_pred = rfc.predict(x_test.values)
score = accuracy_score(y_pred, y_test)
print(f'Accuracy score = {score}')

with open('rfc_model.pickle', 'wb') as rfc_file:
    pickle.dump(rfc, rfc_file)
with open('output.pickle', 'wb') as output_file:
    pickle.dump(uniques, output_file)

# print('Output:')
# print(output.head())
# print('features:')
# print(features.head())
