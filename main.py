import argparse

from crawler import BasicJSONCrawlerManager

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("output_dir")
    parser.add_argument("--crawl_rate")
    args = parser.parse_args()
    if args.crawl_rate:
        manager = BasicJSONCrawlerManager(args.url, args.output_dir, int(args.crawl_rate))
    else:
        manager = BasicJSONCrawlerManager(args.url, args.output_dir)
    manager.crawl()
