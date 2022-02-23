# Argument
import argparse

# Read tsv
import pandas as pd

# Plot
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dataset-file', dest='dataset_file', default="../data/training_set_rel3.tsv", help='Input TSV dataset file')
args = parser.parse_args()

score_ranges = {
    1: (2, 12), 2: (1, 6), 3: (0, 3), 4: (0, 3), 5: (0, 4), 6: (0, 4), 7: (0, 30), 8: (0, 60)
}

total_pd = pd.read_csv(args.dataset_file, sep="\t", header=0, encoding="utf-8", engine='c')
essays = total_pd['essay'].values

mark = dict()
for i in score_ranges.keys():
    mark[i] = [0] * (score_ranges[i][1] + 1)

for i in range(len(total_pd)):
    essay_set = total_pd['essay_set'].values[i]
    score = total_pd['domain1_score'].values[i]
    mark[essay_set][score] += 1

plt.subplots(constrained_layout=True)

for i in range(1, 9):
    plt.subplot(2, 4, i)
    plt.title("Prompt %d" % i)
    plt.xlabel("score")
    plt.ylabel("number of essays")
    plt.plot(range(score_ranges[i][0], score_ranges[i][1] + 1), mark[i][score_ranges[i][0]:])
plt.show()
