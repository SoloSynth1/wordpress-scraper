import csv
import os
from multiprocessing import Pool

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


def main():
    jobs = parse("./legacy/scripts/crawled_list.csv")
    multiple_crawl(jobs)


if __name__ == "__main__":
    main()
