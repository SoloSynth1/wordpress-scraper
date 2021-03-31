# wordpress-scraper

## Description

Simple, easy-to-use scraper to scrape data from WordPress JSON API

## Requirements

 - Python 3.7+

## Installation

```bash
pip install -r requirements.txt
```

## How to use

### Basic

Just run `crawl.py` with the sites URL supplied:

```bash
python3 crawl.py https://your.website.here
```

This will crawl the site using `DefaultCrawlSession`, which attempts to crawl all `posts`, `categories` & `tags` from the site.

The crawled JSON files will be stored in the directory `./data/<domain-name>`.

Most of the time, This will suffice when scraping sites that are 1. not required to sign in & 2. JSON API paths not blocked.


### Advanced
For advanced usage and customizations you may want to look at `wpscraper/session.py` for actual crawling procedures, and make your own `CrawlSession`.

## Upcoming Features

- [x] Rewrite/Refactor
- [x] MongoDB Connector
- [ ] Async session
- [ ] Authentication Module
