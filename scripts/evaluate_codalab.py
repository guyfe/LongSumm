#!/usr/bin/env python
import os.path
import sys
import re
import json

try:
    # installing dependencies
    os.system("pip install rouge-score")
except Exception as e:
    print("Error occurred while installing dependencies ", e)
    exit()

import numpy as np
from rouge_score import rouge_scorer

input_dir = sys.argv[1]
output_dir = sys.argv[2]

submit_dir = os.path.join(input_dir, 'res')
truth_dir = os.path.join(input_dir, 'ref')

if not os.path.isdir(submit_dir):
    print(f"{submit_dir} doesn't exist")


def impose_max_length(summary_text, max_tokens=600):
    #same tokenization as in rouge_score
    #https://github.com/google-research/google-research/blob/26a130831ee903cb97b7d04e71f227bbe24960b2/rouge/tokenize.py
    text = summary_text.lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    tokens = re.split(r"\s+", text)
    tokens = [x for x in tokens if re.match(r"^[a-z0-9]+$", x)]
    tokens = tokens[0:min(max_tokens, len(tokens))]
    return " ".join(tokens)


def evaluate_rouge(test_annotation_file, user_submission_file):
    metrics = ['rouge1', 'rouge2', 'rougeL']
    with open(test_annotation_file) as f1:
        print("open ground truth file " + test_annotation_file)
        ground_truth_data = json.load(f1)
        with open(user_submission_file) as f2:
            submission_data = json.load(f2)
            print("open submission file " + user_submission_file)
            scorer = rouge_scorer.RougeScorer(metrics, use_stemmer=True)
            results = {"rouge1_f":[], "rouge1_r":[], "rouge2_f":[], "rouge2_r":[], "rougeL_f":[], "rougeL_r":[]}
            results_avg = {}

            if len(submission_data) < len(ground_truth_data):
                print("Warning number of papers in submission file is smaller than ground truth file", file=sys.stderr)

            for article_id, ground_truth_summary in ground_truth_data.items():
                submission_summary = submission_data.get(article_id)

                if not submission_summary:
                    print("paper with id '" + str(article_id) + "' wasn't found in submission", file=sys.stderr)
                    raise Exception("article with id '" + str(article_id) + "' wasn't found in submission")

                submission_summary = impose_max_length(submission_summary)
                ground_truth_summary = impose_max_length(ground_truth_summary)

                print("evaluating summary for article with id `"+article_id+"'")
                scores = scorer.score(ground_truth_summary.strip(), submission_summary.strip())
                for metric in metrics:
                    results[metric+"_f"].append(scores[metric].fmeasure)
                    results[metric + "_r"].append(scores[metric].recall)

                for rouge_metric, rouge_scores in results.items():
                    results_avg[rouge_metric] = np.average(rouge_scores)

            return results_avg


if os.path.isdir(submit_dir) and os.path.isdir(truth_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_filename = os.path.join(output_dir, 'scores.txt')
    output_file = open(output_filename, 'w')

    truth_file = os.path.join(truth_dir, "testing.json")
    submission_answer_file = os.path.join(submit_dir, "testing.json")
    if not os.path.exists(submission_answer_file):
        print(
            f"Submission file with name 'testing.json' doesn't exist, please make sure to submit a single zip file that contains 'testing.json'")
        raise Exception(
            f"Submission file with name 'testing.json' doesn't exist, please make sure to submit a single zip file that contains 'testing.json'")

    eval_scores = evaluate_rouge(test_annotation_file=truth_file, user_submission_file=submission_answer_file)
    for metric, metric_score in eval_scores.items():
        output_file.write(f"{metric}:{(metric_score * 100):.2f}\n")
    output_file.close()
