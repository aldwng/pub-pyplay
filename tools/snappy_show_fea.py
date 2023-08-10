import snappy

path = 'C:/ds/sohu/4t9.snappy'
compressed = open(path, 'rb').read()

decompressor = snappy.hadoop_snappy.StreamDecompressor()

txt = decompressor.decompress(compressed).decode()

lines = txt.splitlines()
for ls in lines:
    # ls = l.decode
    if ("ctr" in ls):
        print(ls)

