# -*- coding: utf-8 -*-
import scrapy
from scrapy_demo.qsbk.qsbk.items import QsbkItem
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList

class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    base_domain = "https://www.qiushibaike.com"

    def parse(self, response):
        # print("+"*30)
        # print(response)
        # print(type(response))
        # print("+"*30)
        duanzidivs = response.xpath("//div[@id='content-left']/div")
        # print("="*30)
        # print(type(contentLeft))
        # print("="*30)
        # items = []
        for duanzidiv in duanzidivs:
            #Selector
            author = duanzidiv.xpath(".//h2/text()").get().strip()
            content = duanzidiv.xpath(".//div[@class='content']//text()").getall()
            content = "".join(content).split()
            # print(author)
            # print(content)
            # duanzi = {"author":author,"content":content}
            # yield duanzi
            item = QsbkItem(author=author,content=content)
            yield item
            # items.append(item)
        # return items
        next_url = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
        if not next_url:
            return
        else:
            yield scrapy.Request(self.base_domain+next_url,callback=self.parse)
