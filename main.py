import argparse

from wpscraper.session import DefaultCrawlSession

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    args = parser.parse_args()

    session = DefaultCrawlSession(args.url)
    session.execute()
