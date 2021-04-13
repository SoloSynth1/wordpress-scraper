import argparse
from legacy.crawler import crawler
from legacy import common_header, common_crawl


def crawl(url, output_dir, crawl_rate=25):
    wpc = crawler.WordPressCrawler(url, common_header, output_dir, crawl_rate)
    common_crawl(wpc)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("output_dir")
    parser.add_argument("--crawl_rate", default=25)
    args = parser.parse_args()
    if args.crawl_rate:
        crawl(args.url, args.output_dir, int(args.crawl_rate))
    else:
        crawl(args.url, args.output_dir)
