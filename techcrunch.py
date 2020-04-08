# -*- coding: utf-8 -*-
import scrapy


class TechcrunchSpider(scrapy.Spider):
    name = 'techcrunch'
    allowed_domains = ['techcrunch.com/startups/']
    start_urls = ['https://techcrunch.com/startups/']
    

    def parse(self, response):
    	titles = response.xpath("//h2/a/text()").extract()
    	authors = response.xpath("//span/a/text()").extract()
    	dates = response.xpath("//div/time[@datetime]/text()").extract()

    	for articles in zip(titles,authors,dates):
    		scraped_info = {
    			'Title' : articles[0],
    			'Author' : articles[1],
    			'Date' : articles[2],
    		}


    		yield scraped_info

        
