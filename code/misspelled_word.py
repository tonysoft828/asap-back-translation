import matplotlib.pyplot as plt
import codecs
import pandas as pd
import nltk
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dataset-file', dest='dataset_file', default="../data/training_set_rel3.tsv", help='Input TSV dataset file')
parser.add_argument('-g', '--glove-file', dest='glove_file', default="../embeddings/glove.6B.100d.txt", help='Input txt glove file')
parser.add_argument('-b', '--back-translation-file', dest='back_translation_file', default="../bt-essays/03.ch-en/ee.txt", help='Input txt back-translation essays file')
args = parser.parse_args()

dictionary = []


# return number of misspelled words and number of words
def oov_num(essay):
    words = nltk.word_tokenize(essay.lower())
    cnt = 0
    all_cnt = 0
    for word in words:
        if word not in dictionary:
            for letter in word:
                if '1' <= letter <= '9':        # identities
                    break
            else:
                cnt += 1
        all_cnt += 1
    return cnt, all_cnt


with codecs.open(args.glove_file, 'r', encoding='utf8') as emb_file:
    for line in emb_file:
        tokens = line.split()
        dictionary.append(tokens[0])


total_pd = pd.read_csv(args.dataset_file, sep="\t", header=0, encoding="utf-8", engine='c')
bt_file = open(args.back_translation_file, "r", encoding="utf-8")

essays = total_pd['essay'].values

d_cnt, d_all_cnt = [0] * 9, [0] * 9
b_cnt, b_all_cnt = [0] * 9, [0] * 9

i = 0
for line in bt_file:
    line = line.replace("\n", "")

    essay_set = total_pd['essay_set'].values[i]

    temp = oov_num(essays[i])
    d_cnt[essay_set] += temp[0]
    d_all_cnt[essay_set] += temp[1]

    temp = oov_num(line)
    b_cnt[essay_set] += temp[0]
    b_all_cnt[essay_set] += temp[1]

    i += 1


plt.subplots(constrained_layout=True)

plt.subplot(1, 2, 1)
plt.xlabel("prompt")
plt.ylabel("number of misspelled words")
plt.plot(range(1, 9), d_cnt[1:], color='g', label="original")
plt.plot(range(1, 9), b_cnt[1:], color='b', label="back-translation")
plt.legend()

plt.subplot(1, 2, 2)
plt.xlabel("prompt")
plt.ylabel("number of words")
plt.plot(range(1, 9), d_all_cnt[1:], color='g', label="original")
plt.plot(range(1, 9), b_all_cnt[1:], color='b', label="back-translation")

plt.legend()
plt.show()