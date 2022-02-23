import codecs

f = open("glove.6B.100d.txt", "w", encoding='utf8')

with codecs.open("glove.6B.100d_ori.txt", 'r', encoding='utf8') as emb_file:
    for line in emb_file:
        tokens = line.split()
        f.write(tokens[0] + "\n")

f.close()