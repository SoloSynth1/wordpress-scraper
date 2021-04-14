import csv
import os
from multiprocessing import Pool
import argparse

from legacy_main import crawl

threads = 5


def multiple_crawl(jobs):
    flattened_jobs = map(lambda x: (x['url'], x['output_dir']), jobs)
    with Pool(threads) as p:
        p.starmap(crawl, flattened_jobs)


def parse(csv_path: str):
    if os.path.exists(csv_path):
        with open(csv_path, 'r') as f:
            csvreader = csv.DictReader(f, delimiter=',', quotechar='"')
            return list(csvreader)
    else:
        raise FileNotFoundError()


def main(csv_file):
    jobs = parse(csv_file)
    multiple_crawl(jobs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--csvfile', default="./legacy/scripts/crawled_list.csv")
    args = parser.parse_args()
    main(args.csvfile)
