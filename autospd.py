# -*- coding: utf-8 -*-
import scrapy
from auto.items import AutoItem
from scrapy.http import Request

class AutospdSpider(scrapy.Spider):
    name = 'autospd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cid4002203.html',
                  ]
    def parse(self, response):
        item=AutoItem()
        #通过Xpath表达式分别提取名称，价格，链接，评论数等
        item["name"]=response.xpath("//a[@class='pic']/@title").extract()
        #print("正在爬取"+str(item["name"])+"商品")
        item["price"]=response.xpath("//span[@class='price_n']/text()").extract()
        item["link"]=response.xpath("//a[@class='pic']/@href").extract()
        item["comnum"]=response.xpath("//a[@dd_name='单品评论']/text()").extract()
        yield item
        for i in range(1,3):
            print("正在爬取第"+str(i)+"页")
            url="http://category.dangdang.com/pg"+str(i)+"-cid4002203.html"
            #通过yield返回Request，并指定要爬取的网址和回调参数，实现自动爬取
            yield Request(url, callback=self.parse)
            
            
