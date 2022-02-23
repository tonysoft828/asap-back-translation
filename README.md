# asap-back-translation
Back-translation essays using Chinese and French from ASAP dataset

## Improving Performance of Automated Essay Scoring by using back-translation essays and adjusted scores



- bt_essays

  ​	translated essays and back-translation essays. As the amount of data that Google Translator can process at one time is limited, the original essays were divided into 8 equal-sized parts for translation.

  ​	*03.ch-en/ee.txt* is the final back-translation essays using Chinese

  ​	*05.fr-en/ee.txt* is the final back-translation essays using Chinese



- data

  ​	tsv files generated using back-translation essays and adjusted scores.



- cv

  ​	cross-validation partitions same as in https://github.com/nusnlp/nea

  ​	sample directory includes three cv data : ori, ch, fr. These three cv data are used for model training

  

- embeddings

  ​	*glove.6B.100d.txt* is used to find misspelled words in data. We just keep the word in every line to reduce the size.



- code

  ​	*create_bt_ch.py, create_bt_fr.py* : enerated back-translation tsv file 

  ​	*create_bt_cv.py* : generate cv data using back-translation tsv file

  ​	*misspelled_word.py* : plot the number of misspelled words in data

  ​	*score_distribution.py* : plot the score distribution of each prompt.
