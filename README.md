# wordpress-scraper

## Description

Simple, easy-to-use scraper to scraper data from WordPress JSON API

## Requirements

 - Python 3.7+

## Installation

install all dependencies by running `pip install -r requirements.txt`

## How to use

### Basic

When scraping unprotected sites (not required to sign in & JSON API paths not blocked), `DefaultCrawlSession` will suffice.

The `DefaultCrawlSession` will crawl all `posts`, `categories` & `tags` from the site.


Just run `main.py` with the sites URL supplied:

`python main.py https://your.website.here`

### Advanced
For advanced usage and customizations you may want to look at `wpscraper/session.py` for actual crawling procedures, and make your own `CrawlSession`.

## Upcoming Features

- [x] Rewrite/Refactor
- [ ] MongoDB Connector
- [ ] Async session