import snappy

path = 'C:/ds/sohu/uprofile.snappy'
compressed = open(path, 'rb').read()

decompressor = snappy.hadoop_snappy.StreamDecompressor()

print(decompressor.decompress(compressed))

# print(snappy.uncompress(compressed)
#       .decode(encoding='utf-8', errors="ignore"))