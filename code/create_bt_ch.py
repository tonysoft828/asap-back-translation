# Argument
import argparse

# Read tsv
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dataset-file', dest='dataset_file', default="../data/training_set_rel3.tsv", help='Input TSV dataset file')
parser.add_argument('-b', '--back-translation-file', dest='back_translation_file', default="../bt-essays/03.ch-en/ee.txt", help='Input txt back-translation essays file')
parser.add_argument('-o', '--output-file', dest='output_file', default="../data/training_bt_ch.tsv", help='Output TSV file')

args = parser.parse_args()

score_ranges = {
    1: (2, 12), 2: (1, 6), 3: (0, 3), 4: (0, 3), 5: (0, 4), 6: (0, 4), 7: (0, 30), 8: (0, 60)
}

total_pd = pd.read_csv(args.dataset_file, sep="\t", header=0, encoding="utf-8", engine='c')
bt_file = open(args.back_translation_file, "r", encoding="UTF-8")
essays = total_pd['essay'].values

i = 0
for line in bt_file:
    line = line.replace("\n", "")

    essay_set = total_pd['essay_set'].values[i]
    score = total_pd['domain1_score'].values[i]
    min_score = score_ranges[essay_set][0]
    max_score = score_ranges[essay_set][1]

    if essay_set == 7:
        if score > 16:
            total_pd['domain1_score'].values[i] = max(min_score, score - 1)

    if essay_set == 8:
        if score > 40:
            total_pd['domain1_score'].values[i] = max(min_score, score - 1)
        else:
            total_pd['domain1_score'].values[i] = max(min_score, score - 1)

    essays[i] = line
    i += 1

bt_file.close()

total_pd = total_pd[:i]
total_pd.to_csv(args.output_file, sep="\t", index=False, encoding="UTF-8")
