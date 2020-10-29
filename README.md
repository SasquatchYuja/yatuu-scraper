# yatuu-scraper

Scrapy-scraper fetching [Erika](https://yatuu.fr/erika-et-les-princes-en-detresse-page-1-a-4)'s content on [Yatuu](https://yatuu.fr)'s blog

Currently the two first volumes can be retrieved.

## How to use
```sh
mkvirtualenv yatuu
python -m pip install -r requirements.txt

./fetchAll
deactivate

evince ./out/*.pdf
```

## NB
[1] This scraper has been done for offline reading only, please consider visiting https://yatuu.fr and [supporting](https://fr.tipeee.com/yatuu) the author if you like her work, as well as buying the books, which have all pages in color.

[2] Eventhough the regex is ugly it is still not perfect, some images are fetched but shouldn't. I don't think any is missing, but just in case ALL images' URLs that are found in crawled pages are saved into a file, so that you can download them later if needed.
