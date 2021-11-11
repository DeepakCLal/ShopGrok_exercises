import scrapy
import re

class aldi_items(scrapy.Spider):
    name = 'sgkitems'
    # URL's to scrape - All the URL's given manually since they are small in number else the URL's could be scraped using their href tag and the result could be used in the start_urls
    start_urls = ['https://www.aldi.com.au/en/groceries/super-savers/','https://www.aldi.com.au/en/groceries/price-reductions/','https://www.aldi.com.au/en/groceries/new-to-aldi/','https://www.aldi.com.au/en/groceries/limited-time-only/','https://www.aldi.com.au/en/groceries/baby/nappies-and-wipes/','https://www.aldi.com.au/en/groceries/baby/nappies-and-wipes/','https://www.aldi.com.au/en/groceries/baby/baby-food/','https://www.aldi.com.au/en/groceries/beauty/','https://www.aldi.com.au/en/groceries/freezer/','https://www.aldi.com.au/en/groceries/health/','https://www.aldi.com.au/en/groceries/laundry-household/laundry/','https://www.aldi.com.au/en/groceries/laundry-household/household/','https://www.aldi.com.au/en/groceries/liquor/wine/','https://www.aldi.com.au/en/groceries/liquor/beer-cider/','https://www.aldi.com.au/en/groceries/liquor/champagne-sparkling/','https://www.aldi.com.au/en/groceries/liquor/spirits/','https://www.aldi.com.au/en/groceries/pantry/olive-oil/','https://www.aldi.com.au/en/groceries/pantry/chocolate/','https://www.aldi.com.au/en/groceries/pantry/coffee/']

    def parse(self, response):
        for alitms in response.css('a.box--wrapper.ym-gl.ym-g25'):
            yield{
                'Product_title': alitms.css('div.box--description--header::text').get().lstrip().rstrip(),
                'Product_image': alitms.css('img').attrib['src'],
                'Packsize': alitms.css('div.box--price span.box--baseprice::text').get() if alitms.css('div.box--price span.box--amount::text').get() == '$11.98 per kg' else alitms.css('div.box--price span.box--amount::text').get() if alitms.css('div.box--price span.box--amount::text').get() not in ['', None] else str(re.findall('[0-9].*',str(re.findall('[0-9]*ml|[0-9]*ml[0-9]*mg|[0-9]*g|[0-9]*kg|[0-9]*L|[0-9]*pk', alitms.css('div.box--description--header::text').get().lstrip().rstrip())))).replace(',','/').replace(']','').replace('[','').replace("'","").replace('"',''),
                'Price': str(alitms.css('div.box--price span.box--value::text').get()) + str(alitms.css('div.box--price span.box--decimal::text').get()) if alitms.css('div.box--price span.box--decimal::text').get() != None else str(alitms.css('div.box--price span.box--value::text').get()) + 'c' if alitms.css('div.box--price span.box--value::text').get() != None else '',
                'Price_per_unit': alitms.css('div.box--price span.box--baseprice::text').get() if alitms.css('div.box--price span.box--baseprice::text').get() != '500g' else alitms.css('div.box--price span.box--amount::text').get(),
            }
