import argparse

from crawler import BasicJSONCrawlerManager

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("output_dir")
    args = parser.parse_args()
    manager = BasicJSONCrawlerManager(args.url, args.output_dir)
    manager.crawl()
