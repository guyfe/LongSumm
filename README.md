# LongSumm
A Shared Task at [EMNLP 2020](https://2020.emnlp.org) that focuses on generating long summaries for scientific documents. LongSumm is one of three shared tasks conducted as part of: [1st Workshop on Scholarly Document Processing](https://ornlcda.github.io/SDProc/). 

# LongSumm - Motivation

Most of the work on scientific document summarization focuses on generating relatively short summaries (250 words or less). While such a length constraint can be sufficient for summarizing news articles, it is far from sufficient for summarizing scientific work. In fact, such a short summary resembles more to an abstract than to a summary that aims to cover all the salient information conveyed in a given text. Writing such summaries requires expertise and a deep understanding in a scientific domain, as can be found in some researchers blogs.

The LongSumm task opted to leverage blogs created by researchers in the NLP and Machine learning communities and use these summaries as reference summaries to compare the submissions against.  

The corpus for this task includes a training set that consists of 1705 extractive summaries, and around 700 abstractive summaries of NLP and Machine Learning scientific papers. These are drawn from papers based on video talks from associated conferences (Lev et al. 2019 TalkSumm) and from blogs created by NLP and ML researchers. In addition, we create a test set of abstractive summaries. Each submission is judged against one reference summary (gold summary) on ROUGE and should not exceed 600 words.


# LongSumm - Data and Instructions

This repository contains a dataset and explanation for LongSumm task.

## Training Data
The training data is composed of abstractive and extractive summaries.


### Abstractive Summaries:
The abstractive summaries are of different domains of CS including ML, NLP, AI, vision, storage, etc.


The training data contains 700 abstractive summaries that can be found at data/abstractive/cluster. The folder contains clusters of summaries with length varied between 100-1500 words. Each sub-folder clusters into bins of size 100 words.  (i.e., summary of 541 words will appear in the corresponding cluster of 500-600). We used the Python [NLTK](https://www.nltk.org) libaray to count nummer of words and to segment summary text into sentences.  

The format of a summary is a JSON file with the following entries:
| Entry | Description |
| --- | --- |
| `blog_id` | The id (unique) of the blog |
| `summary` | An array of the sentences of the summary|
| `author_id` | The id of the author|
| `pdf_url` | The link to the original paper|
| `author_full_name` | The author full name|
| `source_website` | the website in which the original blog appears|


Example: 
```json
{
  "blog_id": "4d803bc021f579d4aa3b24cec5b994", 
  "summary": ["Task of translating natural language queries into regular expressions without using domain specific
               knowledge.", 
             "Proposes a methodology for collecting a large corpus of regular expressions to natural language pairs.", 
             "Reports performance gain of 19.6% over state-of-the-art models.", 
             "Architecture  LSTM based sequence to sequence neural network (with attention)
              Six layers  One-word embedding layer Two encoder layers  Two decoder layers  
              One dense output layer.", 
             "Attention over encoder layer.", 
             "...."], 
  "author_id": "shugan", 
  "pdf_url": "http://arxiv.org/pdf/1608.03000v1", 
  "author_full_name": "Shagun Sodhani",
  "source_website": "https://github.com/shagunsodhani/papers-I-read"
}
```


Each papers' summary should be linked the corresponding text of the original paper. Due to copyright will not publish the original papers, here are the suggested steps to fully construct the dataset:


* Download the file URL_2_summ.txt  (data/URL_2_summ.txt). The file URL_2_summ.txt is a tab delimited file which maps a URL to summary id.


Example:
```
id1        https://arxiv.org/pdf/1611.09830
```

* Extract PDF - to get the PDF of the paper, use the script downloader.py. It gets as input 3 parameters:
urls_file  - path to the URL_2_summ.txt file
out_folder - path to the output directory where you want all the PDFs.
num_processes - the script has an option to run in a multiprocess fashion. Default=1, we recommend to use more in order to decrease the downloading time. 
*Notice - some of the papers may require a subscription (e.g., ACM). If you do not have the permission the script won't be able to download the paper.*


`python downloader.py --urls_file=/path/to/input/file/with/mapping --out_folder=/path/to/output/dir/for/PDF --num_processors=3`


The output of this scripts is the papers PDFs by their IDs, under the out_folder.


* Extract Text of the PDF- given papers in pdf format, we used science-parse to convert them to structured json files. 




At the end of this step, you should have for each summary, a corresponding JSON file of the original text from the paper as extracted by science-parse




### Extractive Summaries:


The extractive summaries are based on the TalkSumm (Lev et al. 2019, https://arxiv.org/abs/1906.01351) dataset. The dataset contains 1705 automatically-generated noisy extractive summaries of scientific papers from the NLP and Machine Learning domain based on video talks from associated conferences (e.g., ACL, NAACL, ICML) 
Summaries can be found under data/extractive/. Each summary provides the top-30 sentences, which are on average around 990 words. 
The format of each summary file is as follows:
Each line contains: sentence index (in original paper), sentence score (i.e. duration), then the sentence itself. The fields are tab-separated.
The order of the sentences is according to their order in the paper.
Link to the reference paper.


If you wish to create extractive summaries of a paper that is not exists in the dataset, you will need to follow the instructions from: https://github.com/levguy/talksumm




## Test Data:




## Evaluation:

## Submission:

## Credits
We would like to thank the following blog authors who generosity allowed us to share their summaries as part of this dataset.  

* Shagun Sodhani  [https://github.com/shagunsodhani/papers-I-read](https://github.com/shagunsodhani/papers-I-read)
* Patrick Emami   [https://pemami4911.github.io/index.html](https://pemami4911.github.io/index.html)
* Amr Sharaf  [https://medium.com/@sharaf](https://medium.com/@sharaf)
* Adrian Colye  [https://blog.acolyer.org/about/](https://blog.acolyer.org/about/)
* Alexander Jung  [https://github.com/aleju/papers](https://github.com/aleju/papers)


## Task Organizers:

* [Michal Shmueli-Scheuer - IBM Research AI](https://researcher.watson.ibm.com/researcher/view.php?person=il-SHMUELI)
* [Guy Feigenblat - IBM Research AI](https://researcher.watson.ibm.com/researcher/view.php?person=il-GUYF)


