# LongSumm
A Shared Task at [EMNLP 2020](https://2020.emnlp.org) that focuses on generating long summaries for scientific documents. LongSumm is one of three shared tasks conducted as part of: [1st Workshop on Scholarly Document Processing](https://ornlcda.github.io/SDProc/)

# LongSumm - Overview

Most of the work on scientific document summarization focuses on generating relatively short summaries (abstract like). While such a length constraint can be sufficient for summarizing news articles, it is far from sufficient for summarizing scientific work. In fact, such a short summary resembles more to an abstract than to a summary that aims to cover all the salient information conveyed in a given text. Writing such summaries requires expertise and a deep understanding in a scientific domain, as can be found in some researchers blogs.

The LongSumm task opted to leverage blogs created by researchers in the NLP and Machine learning communities and use these summaries as reference summaries to compare the submissions against.  

The corpus for this task includes a training set that consists of 1705 extractive summaries, and around 700 abstractive summaries of NLP and Machine Learning scientific papers. These are drawn from papers based on video talks from associated conferences (Lev et al. 2019 TalkSumm) and from blogs created by NLP and ML researchers. In addition, we create a test set of abstractive summaries. Each submission is judged against one reference summary (gold summary) on ROUGE and should not exceed 600 words.

The [1st Workshop on Scholarly Document Processing](https://ornlcda.github.io/SDProc/) will include two additional shared tasks: 
-  [Scisumm](https://github.com/WING-NUS/scisumm-corpus) - focuses on automatic paper summarization on a new corpus of research papers in Computational Linguistics (CL) domain
- LaySumm - focuses on enabling systems to automatically generate lay summaries. A lay summary explains, succinctly and without using technical jargon, what the overall scope, goal and potential impact of a scientific paper is.



# LongSumm - Data and Instructions
You are invited to participate in the LongSumm Shared Task at [SDP@EMNLP 2020](https://2020.emnlp.org). This repository contains a dataset and instructions how to participate in the task.

## Training Data
The training data is composed of abstractive and extractive summaries.


### Abstractive Summaries:
The abstractive summaries are of different domains of CS including ML, NLP, AI, vision, storage, etc.

The training data contains 700 abstractive summaries that can be found at data/abstractive/cluster. The folder contains clusters of summaries with length varied between 100-1500 words. Each sub-folder clusters into bins of size 100 words.  (i.e., summary of 541 words will appear in the corresponding cluster of 500-600). We used the Python [NLTK](https://www.nltk.org) library to count number of words and to segment summary text into sentences.  

***We release the data in two cycles, today (Feb 15, 2020) we release the first 249 summaries***

The format of a summary is a JSON file with the following entries:
| Entry | Description |
| --- | --- |
| id | Record id (unique) |
| blog_id | The id of the blog |
| summary | An array of the sentences of the summary|
| author_id | The id of the author|
| pdf_url | The link to the original paper|
| author_full_name | The author full name|
| source_website | the website in which the original blog appears|


Example: 
```json
{
  "id": "79792577",
  "blog_id": "4d803bc021f579d4aa3b24cec5b994",
  "summary": [
    "Task of translating natural language queries into regular expressions ...",
    "Proposes a methodology for collecting a large corpus of regular expressions ...",
    "Reports performance gain of 19.6% over state-of-the-art models.",
    "Architecture  LSTM based sequence to sequence neural network (with attention) Six layers ...",
    "Attention over encoder layer.",
    "...."
  ],
  "author_id": "shugan",
  "pdf_url": "http://arxiv.org/pdf/1608.03000v1",
  "author_full_name": "Shagun Sodhani",
  "source_website": "https://github.com/shagunsodhani/papers-I-read"
}
```


Each papers' summary should be linked the corresponding text of the original paper. Due to copyright will not publish the original papers, here are the suggested steps to fully construct the dataset:

* Extract PDF - to download the PDF of each paper, one can use the following script : [downloader.py](https://github.com/guyfe/LongSumm/blob/master/scripts/downloader.py). The output of this scripts is the papers PDFs by their IDs, under the out_folder.
   
   **_Notice - some of the papers may require a subscription (e.g., ACM). If you do not have the permission the script won't be able to download the paper._**

  The script accepts as input 3 parameters : 
    - `clusters_dir`  - path to the directory that contains the summaries
    - `out_folder` - path to the output directory where you want all the PDFs
    - `num_processes` - the script has an option to run in a multiprocess fashion. Default=1, we recommend to use more in order to decrease the downloading time. 

  
  `python downloader.py --clusters_dir=/path/to/input/dir/with/clusters --out_folder=/path/to/output/dir/for/PDF --num_processors=3`



* Extract Text of the PDF- given papers in pdf format, we recommend to use [science-parse](https://github.com/allenai/science-parse) to convert them to structured json files. 

  At the end of this step, you should have for each summary, a corresponding JSON file of the original text from the paper as extracted by [science-parse](https://github.com/allenai/science-parse).




### Extractive Summaries

The extractive summaries are based on the TalkSumm ([Lev et al. 2019](https://arxiv.org/abs/1906.01351)) dataset. The dataset contains 1705 automatically-generated noisy extractive summaries of scientific papers from the NLP and Machine Learning domain based on video talks from associated conferences (e.g., ACL, NAACL, ICML) 
Summaries can be found under data/extractive/. Each summary provides the top-30 sentences, which are on average around 990 words. 
The format of each summary file is as follows:
- Each line contains: sentence index (in original paper), sentence score (i.e. duration), then the sentence itself. The fields are tab-separated.
- The order of the sentences is according to their order in the paper.
- Link to the reference paper.


If you wish to create extractive summaries of a paper that doesn't not exist in the dataset, you will need to follow the instructions from: [https://github.com/levguy/talksumm](https://github.com/levguy/talksumm)


## Test Data (Blind)
To be released on July 1, 2020


## Evaluation
The intrinsic evaluation will be done by ROUGE, using ROUGE-1, -2, -L and Skipgram metrics. In addition, a randomly selected subset of the summaries will undergo human evaluation.

## Submission
To be announced soon

## Credits
We would like to thank the following blog authors who generosity allowed us to share their summaries as part of this dataset.  

* Shagun Sodhani  [https://github.com/shagunsodhani/papers-I-read](https://github.com/shagunsodhani/papers-I-read)
* Patrick Emami   [https://pemami4911.github.io/index.html](https://pemami4911.github.io/index.html)
* Adrian Colye  [https://blog.acolyer.org/about/](https://blog.acolyer.org/about/)
* Alexander Jung  [https://github.com/aleju/papers](https://github.com/aleju/papers)
* Joseph Paul Cohen  [https://www.shortscience.org/user?name=joecohen](https://www.shortscience.org/user?name=joecohen)
* Hugo Larochelle [https://www.shortscience.org/user?name=hlarochelle](https://www.shortscience.org/user?name=hlarochelle)
<!-- * Amr Sharaf  [https://medium.com/@sharaf](https://medium.com/@sharaf) -->


## License
-  Abstractive summaries:
    - ShortScience summaries are released under [Attribution-NonCommercial-ShareAlike 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
    - all other summaries are released under the CDLA-Sharing license [https://cdla.io/sharing-1-0/](https://cdla.io/sharing-1-0/)
- Extractive summaries - released under [Attribution-NonCommercial-ShareAlike 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

## Disclaimer
The data was copied from the above mentioned blogs as-is. IBM is not responsible for the content of the data, nor for any claim related to the data (including claims related to alleged intellectual property or privacy breach).

## Contacts

For further information about this dataset please contact the organizers of the shared task:

* [Michal Shmueli-Scheuer - IBM Research AI](https://researcher.watson.ibm.com/researcher/view.php?person=il-SHMUELI)
* [Guy Feigenblat - IBM Research AI](https://researcher.watson.ibm.com/researcher/view.php?person=il-GUYF)

