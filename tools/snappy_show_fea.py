import snappy

path = 'C:/ds/sohu/model.snappy'
compressed = open(path, 'rb').read()

decompressor = snappy.hadoop_snappy.StreamDecompressor()

txt = decompressor.decompress(compressed).decode()

lines = txt.splitlines()
for ls in lines:
    # ls = l.decode
    if ("adslotctr" in ls):
        print(ls)

