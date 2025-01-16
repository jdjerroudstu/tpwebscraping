import scrapy

class LegendItem(scrapy.Item):
    name = scrapy.Field()
    role = scrapy.Field()
    type = scrapy.Field()
    image_url = scrapy.Field()
    move_speed = scrapy.Field()
    attack_range = scrapy.Field()
    # crit_damage = scrapy.Field()

