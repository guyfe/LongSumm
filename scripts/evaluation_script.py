import os.path
import json
import sys
import re
try:
    os.system("pip install rouge-score")
except:
    print("An exception occurred rouge-score")

import numpy as np
from rouge_score import rouge_scorer


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


def evaluate(test_annotation_file, user_submission_file, phase_codename, **kwargs):
    #print(kwargs["submission_metadata"])
    output = {}
    if phase_codename == "dev":
        print(" phase_codename "+ phase_codename + " isn't supported", file=sys.stderr)

    elif phase_codename == "test":
        print("Evaluating for Test Phase")
        output["result"] = []
        output["result"].append({"test_split": evaluate_rouge(test_annotation_file, user_submission_file)})

        # To display the results in the result file
        output["submission_result"] = output["result"][0]
        print("Completed evaluation for Test Phase with " + str(output))
    return output


if __name__ == "__main__":
    # execute only if run as a script
    evaluate('../annotations/test_annotations_testsplit.json', '../annotations/test_submission_testsplit.json')