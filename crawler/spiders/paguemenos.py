import json
import locale
from datetime import datetime
from urllib.parse import urlencode

from crawler.custom_settings.paguemenos_settings import settings
from scrapy.http import Request
from scrapy.spiders import SitemapSpider

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


class PagueMenosSpider(SitemapSpider):
    name = 'paguemenos_crawl'
    allowed_domains = ['www.paguemenos.com.br']
    sitemap_urls = ['https://www.paguemenos.com.br/sitemap.xml']

    sitemap_follow = [
        r'[\w\d./:]+(category)[\w\d.-]+'
    ]

    custom_settings = settings()

    def parse(self, response):
        try:
            page = response.meta['page']
        except Exception:
            page = 1

        json_page = response.xpath(
            '//script[@type="application/ld+json"]/text()').get()

        if json_page is not None:
            json_blob = json.loads(json_page)
            for item in json_blob['itemListElement']:
                url_product = item['item']["@id"]
                priceCurrency = item['item']['offers']['priceCurrency']
                query_json = {
                    "__pickRuntime": 'page,queryData,contentResponse,route'}
                json_product = url_product + '?' + urlencode(query_json)
                yield Request(url=json_product, callback=self.parse_product,
                              meta={"url_product": url_product,
                                    "priceCurrency": priceCurrency})

            urlPage = response.url
            urlPage = urlPage.split('?')[0]

            page += 1
            dict_page = {"page": page}
            next_page = urlPage + '?' + urlencode(dict_page)
            yield Request(url=next_page, callback=self.parse,
                          meta={'page': page})

    def parse_product(self, response, **kwargs):
        url_product = response.meta['url_product']
        priceCurrency = response.meta['priceCurrency']
        data_product = response.text
        json_blob = json.loads(data_product)

        data_items_bulk = json_blob["queryData"][0]["data"]
        data_items_bulk = json.loads(data_items_bulk)
        data_items = data_items_bulk["product"]["items"][0]

        try:
            ean = data_items["ean"]
        except Exception:
            ean = None

        try:
            name = data_items["nameComplete"]
        except Exception:
            name = data_items["name"]

        try:
            price = data_items["sellers"][0]["commertialOffer"]["Price"]
            price = locale.atof(price)
        except Exception:
            price = data_items["sellers"][0]["commertialOffer"]["Price"]

        sku = data_items_bulk["product"]["productId"]
        seller = data_items["sellers"][0]["sellerName"]
        PriceValidUntil = (data_items["sellers"][0]["commertialOffer"]
                           ["PriceValidUntil"])
        imageUrl = [link["imageUrl"] for link in data_items["images"]]
        productUrl = url_product
        categories = data_items_bulk["product"]["categories"]
        brand = data_items_bulk["product"]["brand"]
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        yield {
            "ean": ean,
            "name": name,
            "price": price,
            "priceCurrency": priceCurrency,
            "brand": brand,
            "sku": sku,
            "categories": categories,
            "seller": seller,
            "imageUrl": imageUrl,
            "productUrl": productUrl,
            "priceValidUntil": PriceValidUntil,
            "created_at": created_at,
        }
