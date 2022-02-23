import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dataset-file', dest='dataset_file', default="../data/training_set_rel3.tsv", help='Input TSV dataset file')
parser.add_argument('-b', '--back-translation-file', dest='back_translation_file', default="../data/training_bt_fr.tsv", help='Input TSV back-translation data file')
parser.add_argument('-c', '--cv-partition-path', dest='cv_partition_path', default="../cv", help='Input TSV back-translation data file')
args = parser.parse_args()

total_pd = pd.read_csv(args.dataset_file, sep="\t", header=0, encoding="utf-8", engine='c')
trans_pd = pd.read_csv(args.back_translation_file, sep="\t", header=0, encoding="utf-8", engine='c')

for fold_idx in range(0, 5):
    for dataset_type in ['dev', 'test', 'train']:
        input_filename = f'{args.cv_partition_path}/fold_%d/%s_ids.txt' % (fold_idx, dataset_type)
        new_pd = pd.DataFrame()
        with open(input_filename) as f:
            for line in f:
                if dataset_type == 'test':
                    new_pd = pd.concat([new_pd,
                                        total_pd[total_pd.essay_id == int(line)],
                                        ])
                else:
                    new_pd = pd.concat([new_pd,
                                        total_pd[total_pd.essay_id == int(line)],
                                        trans_pd[trans_pd.essay_id == int(line)]
                                        ])

        output_filename = f'{args.cv_partition_path}/fold_%d/%s.tsv' % (fold_idx, dataset_type)
        new_pd.to_csv(output_filename, sep="\t", index=False)
