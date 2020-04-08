# RSS_Feed_Reader
This scraper scrapes the techcrunch website and scrapes info like title of the article , its author and the date.
## Start a scrapy project
```
scrapy startproject RSS_feed_reader
```

## Create a spider
```
scrapy genspider techcrunch techcrunch.com/startups/
```
After coding the spider add small code in settings.py to generate a csv file.

## Execute
Finally execute the spider.
```
scrapy crawl techcrunch
```
A csv file will be created containing the desired information.
