import pandas as pd

model_file = 'C:/ds/cvr/fm_model_1009'
lr_coeffs = 'C:/ds/cvr/fm_digits.csv'

with open(model_file, encoding='UTF-8') as f:
    lines = f.read().split('\n')


lines = list(filter(None, lines))

seqs = []
for line in lines:
    elems = line.split('\t')
    key = elems[0]
    last = elems[-1]
    if (key.find('&')):
        key = key.split('&')[0]
        seqs.append((key, 1, last))

df = pd.DataFrame(data=seqs, 
                  columns=['fid', 'count', 'last']).groupby('fid').agg({'count':'sum', 'last':'max'})

df = df.sort_values(by='count', ascending=False)

df = df.drop('0')

print(df.to_string)

df.to_csv(lr_coeffs)