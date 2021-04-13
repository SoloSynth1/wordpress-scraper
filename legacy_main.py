import argparse
from legacy.crawler import crawler

if __name__ == "__main__":
    from legacy import common_header, common_crawl
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("output_dir")
    parser.add_argument("--crawl_rate", default=25)
    args = parser.parse_args()
    if args.crawl_rate:
        wpc = crawler.WordPressCrawler(args.url, common_header, args.output_dir, int(args.crawl_rate))
    else:
        wpc = crawler.WordPressCrawler(args.url, common_header, args.output_dir)
    common_crawl(wpc)
