import os
import requests
import argparse
from multiprocessing import Pool
from tqdm import tqdm
import csv
import json



OUTPUT_DIR = '/path/to/out/folder'


def url_response(url):
    name, url = url
    name = str(name)
    if not os.path.isfile(os.path.join(OUTPUT_DIR, name + ".pdf")):
        try:
            r = requests.get(url, stream = True)
            with open(os.path.join(OUTPUT_DIR,name+".pdf"), 'wb') as f:
                for ch in r:
                    f.write(ch)
        except requests.ConnectionError as e:
            print("  Failed to open: "+ url)

def set_globdir_to_new(out_dir):
        global OUTPUT_DIR
        OUTPUT_DIR = out_dir

def main(args):
    urls_dict = {}

    set_globdir_to_new(args.out_folder)

    for subdir, dirs, files in os.walk(args.clusters_dir):
        for file in files:
            # print os.path.join(subdir, file)
            filepath = subdir + os.sep + file

            if filepath.endswith(".json"):
                with open(filepath, 'r') as in_f:
                    summ_info = json.load(in_f)
                    urls_dict[summ_info['id']] = summ_info['pdf_url']
            else:
                print(filepath)
                continue


    os.makedirs(args.out_folder, exist_ok=True)
    with Pool(int(args.num_processes)) as p:
        urls_and_names = list(urls_dict.items())
        list(tqdm(p.imap(url_response, urls_and_names), total=len(urls_dict)))

    print('Finished!')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Given URL of a paper, this script download the PDFs of the paper'
    )

    parser.add_argument('--clusters_dir', help='link to the folder that contains the summaries')
    parser.add_argument('--out_folder', help='output folder')
    parser.add_argument('--num_processes', default=1, help='number of processes to use')

    args = parser.parse_args()
    main(args)
