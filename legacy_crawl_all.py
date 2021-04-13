import csv
import os

from legacy_main import crawl


def parse(csv_path: str):
    if os.path.exists(csv_path):
        with open(csv_path, 'r') as f:
            csvreader = csv.DictReader(f, delimiter=',', quotechar='"')
            for row in csvreader:
                crawl(row['url'], row['output_dir'])
    else:
        raise FileNotFoundError()


def main():
    parse("./legacy/scripts/crawled_list.csv")


if __name__ == "__main__":
    main()
