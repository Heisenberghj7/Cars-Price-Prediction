import scrapy
import json

class Brands_links(scrapy.Spider):
    name = "brands_links"
    start_urls=["https://www.wandaloo.com/neuf/"]

    def parse(self, response):
        for link in response.css(" div#brand > div.col11 > ul > li > a::attr(href)").getall():
            yield {
                'brand_link': link
            }


class Brands_Gamme(scrapy.Spider):
    name = "brands_gamme"

    with open('1-brands_links.json', 'r') as f:
        data= json.load(f)
    
    start_urls=[item['brand_link'] for item in data]

    def parse(self, response):
            names =response.css("div.col11 > ul > li > div.col-xs-12.col-sm-8 > h3 > a::text").extract()
            links = response.css("div.col11 > ul > li > div.col-xs-12.col-sm-8 > h3 > a::attr(href)").extract()
            yield { 
                    'brand_name':response.url.split('/')[-2],
                    'Gamme names': names,
                    'Gamme links': links
                }

class Gamme_versions(scrapy.Spider):
    name = "gamme_versions"

    with open('2-gammes.json', 'r') as f:
        data= json.load(f)
    
    start_urls=[link for item in data for link in item['Gamme links']]

    def parse(self, response):
            yield { 
                    'gamme name':response.url.split('neuf')[-1],
                    'gamme_versions':response.css("div.col11 > ul > li > div:nth-of-type(1)> p > a::attr(href)").extract()
                }

class Fiche(scrapy.Spider):
    name = "fiche_technique"

    with open('3-gamme_versions.json', 'r') as f:
        data= json.load(f)
    
    start_urls=[link for item in data for link in item['gamme_versions']]
    def parse(self, response):
        values=[]
        price=''
        promo=''
        more_info=""
        lis= response.css("div.col-left > div.cell > ul > li")
        infos=response.css("p#morefiche::text").extract()
        for info in infos:
            more_info+=info
        for li in lis: 
            if li.css("p.value > img::attr(src)").extract_first()== None:
                values.append(li.css("p.value::text").extract_first())
            else:
                values.append(li.css("p.value > img::attr(src)").extract_first())

        if response.css("div.col-sm-7.col-xs-12.details > p.prix > span:nth-of-type(2)::text").extract_first() =='promo':
           price= response.css("div.col-sm-7.col-xs-12.details > p.prix > span:nth-of-type(1)::text").extract_first()
           promo= response.css("div.col-sm-7.col-xs-12.details > p.promo-detail > span::text").extract_first()
        else: 
           price = response.css("div.col-sm-7.col-xs-12.details > p.prix::text").extract_first()
       
        yield { 
            'name':response.css("div.col-sm-7.col-xs-12 > h1::text").extract_first() + response.css("div.col-sm-7.col-xs-12 > h3::text").extract_first(),
            'price':price,
            'promo':promo,
            'params':response.css("div.col-left > div.cell > ul > li > p.param::text ").getall(),
            'values': values,
            'More_Info':more_info
                }