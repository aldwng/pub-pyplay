import pandas as pd

model_file = 'C:/ds/cvr/app_model_502'
lr_coeffs = 'C:/ds/cvr/ctr_502_coeffs.csv'

with open(model_file, encoding='UTF-8') as f:
    lines = f.read().split('\n')


lines = list(filter(None, lines))

seqs = []
for line in lines:
    key, value = line.split('\t')
    if (key.find('&')):
        key = key.split('&')[0]
        key = key.replace('502_', '')
        seqs.append((key, 1, abs(float(value))))

df = pd.DataFrame(data=seqs, 
                  columns=['fid', 'count', 'val']).groupby('fid').agg({'count':'sum', 'val':'sum'})

df['avrg'] = df.apply(lambda row: row['val'] / row['count'], axis=1)

df['abs_avrg'] = df.apply(lambda row: abs(row['avrg']), axis=1)

df = df.drop('bias')

df = df.sort_values(by='abs_avrg', ascending=False)

print(df.to_string)

df.to_csv(lr_coeffs)