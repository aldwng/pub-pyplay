import snappy

path = 'C:/ds/sohu/m508.snappy'
compressed = open(path, 'rb').read()

decompressor = snappy.hadoop_snappy.StreamDecompressor()

txt = decompressor.decompress(compressed).decode()

lines = txt.splitlines()
for ls in lines:
    # ls = l.decode
    if ("seed" in ls):
        print(ls)

