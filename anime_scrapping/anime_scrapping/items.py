# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimeScrappingItem(scrapy.Item):
    title = scrapy.Field()
    image = scrapy.Field()
    duration = scrapy.Field()
    release = scrapy.Field()
    rating = scrapy.Field()
    genre = scrapy.Field()
    description = scrapy.Field()
    episode = scrapy.Field()