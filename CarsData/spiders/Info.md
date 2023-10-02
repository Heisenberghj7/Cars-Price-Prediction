## Brands links

brands= response.css(" div#brand > div.col11 > ul > li > a::attr(href)").getall()

gammes_names = response.css("div.col11 > ul > li > div.col-xs-12.col-sm-8 > h3 > a::text").extract()

gammes_links= response.css("div.col11 > ul > li > div.col-xs-12.col-sm-8 > h3 > a::attr(href)").extract()

gammes_varsions= response.css("div.col11 > ul > li > div:nth-of-type(1) > p > a::attr(href)").extract()

## fiche_technique_items

full_name = response.css("div.col-sm-7.col-xs-12 > h1::text").extract_first() + response.css("div.col-sm-7.col-xs-12 > h3::text").extract_first()

price= response.css("div.col-sm-7.col-xs-12.details > p.prix > span:nth-of-type(1)::text").extract_first()
promo= response.css("div.col-sm-7.col-xs-12.details > p.promo-detail > strong:nth-of-type(2)::text").extract_first()

promo_test= response.css("div.col-sm-7.col-xs-12.details > p.prix > span:nth-of-type(2)::text").extract_first() =='promo'

price = response.css("div.col-sm-7.col-xs-12.details > p.prix::text").extract_first()

params =response.css("div.col-left > div.cell > ul > li > p.param::text ").getall()
lis= response.css("div.col-left > div.cell > ul > li")
values=[]
for li in lis: 
    if li.css("p.value > img::attr(src)").extract_first()== None:
         values.append(li.css("p.value::text").extract_first())
    else:
         values.append(li.css("p.value > img::attr(src)").extract_first())
        
