import scrapy
import json
import requests
from anime_scrapping.items import AnimeScrappingItem
class AnimeSpider(scrapy.Spider):
    name = 'anime'
    start_urls = ['https://nontonanime.cc/wp-json/apk/list']
    def parse(self, response):
        
        jsonresponse = json.loads(response.body)
        for i in range(len(jsonresponse)):
            urls = jsonresponse[i]['url']
            url = response.urljoin(urls)
            yield scrapy.Request(url=url, callback=self.parse_list_anime, errback=self.errback)

    def errback(self,failure):
        print(failure)

    def parse_list_anime(self, response):
        items = AnimeScrappingItem()
        jsonresponse = json.loads(response.body)
        genres = []
        episodes = []
        for k in range(len(jsonresponse[0]['genre'])):
            genres.append({"name": jsonresponse[0]['genre'][k]['name']})

        items['title'] = jsonresponse[0]['title']
        items['image'] = jsonresponse[0]['cover']
        items['duration'] = jsonresponse[0]['duration']
        items['release'] = jsonresponse[0]['released']
        items['rating'] = jsonresponse[0]['score']
        items['genre'] = genres
        items['description'] = jsonresponse[0]['synopsis']

        for i in range(len(jsonresponse[0]['data'])):
            url = jsonresponse[0]['data'][i]['url']
            episodes.append({"episode": jsonresponse[0]['data'][i]['episode'], "video": self.parse_vid(url)})

        items['episode'] = episodes

        yield items


    def parse_vid(self, data):
        response = requests.get(data)
        jsonresponse = json.loads(response.content)

        return jsonresponse['player'][0]['url']