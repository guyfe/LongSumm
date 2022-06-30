# LongSumm
A Shared Task at [COLINNG 2022](https://coling2022.org/) that focuses on generation of long summaries for scientific documents. LongSumm shared task conducted as part of: [3rd Workshop on Scholarly Document Processing](https://ornlcda.github.io/SDProc/).

This is the thrid year of this task, previous reports can be found at [2020](https://aclanthology.org/2020.sdp-1.24/) and [2021](https://aclanthology.org/2021.sdp-1.22/).


### Important announcement (June 30, 2022) :
Evaluation period has started, see [Submission Instructions](#submission-instructions).

### Important announcements (May 4, 2022) :
- See below the timeline for the task.
- If you would like to participate please fill up this [form](https://forms.gle/NBigWpjnJZrPagPJ9)
- \** Check our new shared task [Multi Perspective Scientific Document Summarization- MuP](https://github.com/allenai/mup).


<!-- ### Important announcements (February 25, 2021) : 

-  Based on request form several teams the blind test set runs are now due by March 1, 2021 (AoE): see https://github.com/guyfe/LongSumm#timeline </font>
- Please do not forget to select one of your submissions to appear in the leaderboard. 
- Participant teams are asked to send us an email with the team name and contact details of at least one corresponding author. 
 -->

# LongSumm - Overview

Most of the work on scientific document summarization focuses on generating relatively short summaries. Such a length constraint might be appropriate when summarizing news articles but it is less adequate for scientific work. In fact, such a short summary resembles an abstract and cannot cover all the salient information conveyed in a given scientific text. Writing longer summaries requires expertise and a deep understanding in a scientific domain, as can be found in some researchers blogs.

To address this point, the LongSumm task opted to leverage blog posts created by researchers in the NLP and Machine learning communities that summarize scientific articles and use these posts as reference summaries.  

The corpus for this task includes a training set that consists of 1705 extractive summaries, and 531 abstractive summaries of NLP and Machine Learning scientific papers. The extractive summaries are based on video talks from associated conferences (Lev et al. 2019 TalkSumm) while the abstractive summaries are blog posts created by NLP and ML researchers. In addition, we created a test set of abstractive summaries for testing submissions. Each submission is judged against one reference summary (gold summary) using ROUGE and should not exceed 600 words.

If you use this dataset in your work, please cite our paper:
```
@inproceedings{chandrasekaran-etal-2020-overview-insights,
    title = "Overview and Insights from the Shared Tasks at Scholarly Document Processing 2020: {CL}-{S}ci{S}umm, {L}ay{S}umm and {L}ong{S}umm",
    author = "Chandrasekaran, Muthu Kumar  and
      Feigenblat, Guy  and
      Hovy, Eduard  and
      Ravichander, Abhilasha  and
      Shmueli-Scheuer, Michal  and
      de Waard, Anita",
    booktitle = "Proceedings of the First Workshop on Scholarly Document Processing",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.sdp-1.24",
    doi = "10.18653/v1/2020.sdp-1.24",
    pages = "214--224",
}
```


<!--The [1st Workshop on Scholarly Document Processing](https://ornlcda.github.io/SDProc/) will include two additional shared tasks: 
-  [Scisumm](https://github.com/WING-NUS/scisumm-corpus) - focuses on automatic paper summarization on a new corpus of research papers in Computational Linguistics (CL) domain -->
<!--
- LaySumm - focuses on enabling systems to automatically generate lay summaries. A lay summary explains, succinctly and without using technical jargon, what the overall scope, goal and potential impact of a scientific paper is.-->


# LongSumm - Data and Instructions
You are invited to participate in the LongSumm Shared Task at [SDP@COLINNG 2022](https://coling2022.org/). This repository contains the dataset and instructions on how to participate in the task.

## Training Data
The training data is composed of abstractive and extractive summaries.


### Abstractive Summaries:
The abstractive summaries are from different domains of CS including ML, NLP, AI, vision, storage, etc.

The training data contains around 700 abstractive summaries that can be found at data/abstractive/cluster. The folder contains clusters of summaries with length varying between 100-1500 words. Each sub-folder clusters into bins of size 100 words.  (i.e., summary of 541 words will appear in the corresponding cluster of 500-600). We used the Python [NLTK](https://www.nltk.org) library to count the number of words and to segment summary text into sentences.  

<!--***We release the data in three cycles, today ~~(Feb 15, 2020)~~ (Feb 25, 2020) we release the first ~~249~~ 516 summaries*** -->

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


Each papers' summary should be linked the corresponding text of the original paper. Due to copyright restrictions will not publish the original papers, here are the suggested steps to fully construct the dataset:

* Extract PDF - to download the PDF of each paper, one can use the following script : [downloader.py](https://github.com/guyfe/LongSumm/blob/master/scripts/downloader.py). The output of this scripts is the papers PDFs by their IDs, under the out_folder.
   
   **_Notice - some of the papers may require a subscription (e.g., ACM). If you do not have the permission the script won't be able to download the paper._**

  The script accepts as input 3 parameters : 
    - `clusters_dir`  - path to the directory that contains the summaries
    - `out_folder` - path to the output directory where you want all the PDFs
    - `num_processes` - the script has an option to run in a multiprocess fashion. Default=1, we recommend to use more in order to decrease the downloading time. 
  
  `python downloader.py --clusters_dir=/path/to/input/dir/with/clusters --out_folder=/path/to/output/dir/for/PDF --num_processes=3`



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

There are 22 papers for the test set, as listed below.

| Paper id   | Paper title                                                                                                      | Paper link                                                                                                                           |
|------|------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| 1000 | Unsupervised Part-of-Speech Tagging with Bilingual Graph-Based Projections               | https://www.aclweb.org/anthology/P11-1061.pdf                                                                                          |
| 1001 | RNN Fisher Vectors for Action Recognition and Image Annotation              | https://arxiv.org/pdf/1512.03958.pdf                                                                                        |
| 1002 | TALK SUMM: A Dataset and Scalable Annotation Method for Scientific Paper Summarization Based on Conference Talks | https://arxiv.org/pdf/1906.01351.pdf                                                                                           |
| 1003 | Emotion Detection from Text via Ensemble Classification Using Word Embeddings                                    | https://dl.acm.org/doi/pdf/10.1145/3121050.3121093                                                                             |
| 1004 | Classifying Emotions in Customer Support Dialogues in Social Media                                               | https://www.aclweb.org/anthology/W16-3609.pdf                                                                                  |
| 1005 | MetAdapt: Meta-Learned Task-Adaptive Architecture for Few-Shot Classification                                    | https://arxiv.org/pdf/1912.00412.pdf                                                                                           |
| 1006 | Detecting Egregious Conversations between Customers and Virtual Agents                                           | https://www.aclweb.org/anthology/N18-1163.pdf                                                                                  |
| 1007 | Understanding Convolutional Neural Networks for Text Classification                                              | https://www.aclweb.org/anthology/W18-5408.pdf                                                                                  |
| 1008 | An Editorial Network for Enhanced Document Summarization | https://www.aclweb.org/anthology/D19-5407.pdf
| 1009 | DIMSIM: An Accurate Chinese Phonetic Similarity Algorithm Based on Learned High Dimensional Encoding             | https://www.aclweb.org/anthology/K18-1043.pdf                                                                                  |
| 1010 | Improved Neural Relation Detection for Knowledge Base Question Answering                                         | https://www.aclweb.org/anthology/P17-1053.pdf                                                                                  |
| 1011 | Interactive Dictionary Expansion using Neural Language Models                                                    | http://ceur-ws.org/Vol-2169/paper-02.pdf                                                                                       |
| 1012 | Interpretable and Globally Optimal Prediction for Textual Grounding using Image Concepts                         | https://papers.nips.cc/paper/6787-interpretable-and-globally-optimal-prediction-for-textual-grounding-using-image-concepts.pdf |
| 1013 | Learning Implicit Generative Models by Matching Perceptual Features                                              | https://arxiv.org/pdf/1904.02762.pdf                                                                                           |
| 1014 | Scalable Demand-Aware Recommendation                                                                             | http://papers.nips.cc/paper/6835-scalable-demand-aware-recommendation.pdf                                                      |
| 1015 | Neural Response Generation for Customer Service based on Personality Traits                                      | https://www.aclweb.org/anthology/W17-3541.pdf
| 1016 | A Low Power, High Throughput, Fully Event-Based Stereo System | https://openaccess.thecvf.com/content_cvpr_2018/CameraReady/3791.pdf
| 1017 | Characterization and Learning of Causal Graphs with Latent Variables from Soft Interventions | https://papers.nips.cc/paper/9581-characterization-and-learning-of-causal-graphs-with-latent-variables-from-soft-interventions.pdf
| 1018 | Complex Program Induction for Querying Knowledge Bases in the Absence of Gold Programs | https://www.aclweb.org/anthology/Q19-1012.pdf
| 1019 | Unsupervised Dual-Cascade Learning with Pseudo-Feedback Distillation for Query-based Extractive Summarization | https://arxiv.org/pdf/1811.00436
| 1020 | High quality, lightweight and adaptable TTS using LPCNet | https://arxiv.org/pdf/1905.00590
| 1021 | Sobolev Independence Criterion | https://arxiv.org/pdf/1910.14212.pdf




## Evaluation
The intrinsic evaluation will be done by ROUGE, using ROUGE-1, -2, -L metrics. The average of the ROUGE-F scores obtained against the multiple summaries would be used for final ranking. In addition, a randomly selected subset of the summaries will undergo human evaluation.


## Submission Instructions
We will use [Codalab](https://codalab.lisn.upsaclay.fr/) to evaluate submissions against the hidden test set.

Please follow the below instructions to evaluate and report your team results: 
1. Create a [Codalab](https://codalab.lisn.upsaclay.fr/) account 
2. In the "User Settings" pane, and under "Competition settings", set "Team name" to the name you are using for the shared task (this name will appear in the leaderboard)
3. Create `testing.json` file with your system generated summaries on the test set. The submission should be **a single json file** containing **all generated test set summaries**. The `testing.json` file should have the following format: [Submission Format](#submission-format)
4. Compress the `testing.json` file into `testing.zip` file
5. Login to Codalab, select the competition: [https://codalab.lisn.upsaclay.fr/competitions/5693](https://codalab.lisn.upsaclay.fr/competitions/5693)
6. Select the Participate tab--> [Submit / View Results](https://codalab.lisn.upsaclay.fr/competitions/5693#participate-submit_results). Select the Submit button and choose your local `testing.zip` file (from step 4). The table below the Submit button will show the status of your submission.
7. Once the submission is uploaded and evaluated against the hidden test set the status will change to Finished. You can choose to report your results to the leaderboard or to download the scores to a text file by selecting the `Download output from scoring step` option. 

**Make sure to report the highest obtained score to the leaderboard before the evaluation period ends**

### Submission Format
The submission should be **a single json file** containing all summaries, following the format:

```json
{
"paper_id_1":"summary of paper 1",
"paper_id_2":"summary of the paper 2"
}
```

### Evaluation Script
[Evaluation script](scripts/evaluate_codalab.py)

### Leaderboard
We will use [Codalab](https://codalab.org/) leaderboard to evaluate the quality of the submissions. We will use the following evaluation script:   [https://github.com/guyfe/LongSumm/blob/master/scripts/evaluation_script.py](/scripts/evaluate_codalab.py)

Submission instructions will be updated soon. 

<!-- In order to submit you will need to follow these steps:
1. Create an IBM account at ibm.com (https://tinyurl.com/ydcd6hjg). Please use the email account that you registered to the task.
2. Login to the AI Leaderboard (https://aieval.draco.res.ibm.com/) with your IBM account

AI Leaderboard instructions:
1. Choose "Participate"
2. Choose "Participant Teams" and create a new participant team - use a meaningful name for your group as this is the name that will appear in the leaderboard. 
3. Go to "All Challenges" and find our task "Long Scientific Document Summarization" , and click on "View Details"
4. To submit go the the "Participate" tab, select a team, click on "Next" and accept the Terms & Condisiton. (this step is done only once). In case that you are not able to click on "Next" please press refresh that page (Ctrl+Shift+R or Cmnd+Shift+r)
5. Go to the "Submit" tab, there you can upload the json file, describe the submission, and press "Submit". 
5. To view your submission(s) go to the "My Submissions". There you can see all your submissions, their status (Finished/Failed), links to some logs, and results. Finally in case that you want your submission to appear in the leaderboard you will need to check "Show on leaderboard".
6. Finally, in order to see the leaderboard go to the "Leaderboard" tab.

* Firefox and Chrome browsers are supported
* In any case that you seems not to see submission/results on leaderboard press refresh that page (Ctrl+Shift+R or Cmnd+Shift+r)
 -->
### LongSumm Leaderboard from previous years 
[Previous years leaderboard](https://github.com/guyfe/LongSumm/blob/master/leaderboard-2021.pdf?raw=true)

### Previous Years system Reports  
LongSumm 2021 - [https://aclanthology.org/volumes/2021.sdp-1/](https://aclanthology.org/volumes/2021.sdp-1/)

LongSumm 2020 - [https://aclanthology.org/volumes/2020.sdp-1/](https://aclanthology.org/volumes/2020.sdp-1/)


### Rules
- You can submit up to 25 runs.

### Timeline
- Train & validation set release – May 10, 2022 (registration opens)
- Test set release – July 1, 2022 (registration closes)
- Blind test set runs due – July 15, 2022 (registration closes)
<!-- - Final evaluation results published – August 15, 2022 -->
- All paper submissions due – August 1, 2022
- Notification of acceptance – August 15, 2022
- Camera-ready papers due – September 5, 2022
- Workshop – October 16/17, 2022

### Submission Disclaimer
You should only submit summaries that are part of the test data. Please do not submit any confidential or personal information.
Please see the IBM Terms of use  (https://www.ibm.com/legal)

## Credits
We would like to thank the following blog authors and to [ShortScience.org](https://www.shortscience.org) who genereously allowed us to share the content as part of this dataset.  

* Shagun Sodhani  [https://github.com/shagunsodhani/papers-I-read](https://github.com/shagunsodhani/papers-I-read)
* Patrick Emami   [https://pemami4911.github.io/index.html](https://pemami4911.github.io/index.html)
* Adrian Colyer  [https://blog.acolyer.org/about/](https://blog.acolyer.org/about/)
* Alexander Jung  [https://github.com/aleju/papers](https://github.com/aleju/papers)
* Joseph Paul Cohen  [https://www.shortscience.org/user?name=joecohen](https://www.shortscience.org/user?name=joecohen)
* Hugo Larochelle [https://www.shortscience.org/user?name=hlarochelle](https://www.shortscience.org/user?name=hlarochelle)
* Elvis Saravia [https://github.com/dair-ai/nlp_paper_summaries](https://github.com/dair-ai/nlp_paper_summaries)
<!-- * Amr Sharaf  [https://medium.com/@sharaf](https://medium.com/@sharaf) -->


## License
-  Abstractive summaries:
    - [ShortScience.org](https://www.shortscience.org) summaries are released under [Attribution-NonCommercial-ShareAlike 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
    - all other summaries are released under the CDLA-Sharing license [https://cdla.io/sharing-1-0/](https://cdla.io/sharing-1-0/)
- Extractive summaries - released under [Attribution-NonCommercial-ShareAlike 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

## Disclaimer
The data was copied from the above mentioned blogs as-is. IBM is not responsible for the content of the data, nor for any claim related to the data (including claims related to alleged intellectual property or privacy breach).

## Contacts

For further information about this dataset please contact the organizers of the shared task:

* [Michal Shmueli-Scheuer - IBM Research AI](https://researcher.watson.ibm.com/researcher/view.php?person=il-SHMUELI)
* [Guy Feigenblat - Piiano](https://Piiano.com)

<br><br>
<p style="display:inline">

<img itemprop="image" class="avatar flex-shrink-0 mb-3 mr-3 mb-md-0 mr-md-4" src="https://avatars.githubusercontent.com/u/22341564?s=200&amp;v=4" width="100" height="100" alt="IBMResearch"> &nbsp; &nbsp; &nbsp; 

 <a href="https://piiano.com/">
 <img width="241" height="76" src="https://piiano.com/wp-content/uploads/2021/09/Piiano-logo.svg" class="attachment-full size-full entered lazyloaded" alt="Piiano logo" data-lazy-src="https://piiano.com/wp-content/uploads/2021/09/Piiano-logo.svg" data-ll-status="loaded" alt="Piiano">
 </p>
 </a>
 
