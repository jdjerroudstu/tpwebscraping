
import scrapy
from legendsscraper.items import LegendItem

class LegendsSpider(scrapy.Spider):
    name = "legends"
    allowed_domains = ["leagueoflegends.fandom.com"]
    start_urls = ["https://leagueoflegends.fandom.com/wiki/Champion#List_of_champions"]

    base_url = "https://leagueoflegends.fandom.com"

    def parse(self, response):
        # parcours de la liste des champions
        for champion in response.css('ul.champion_roster li'):
            relative_link = champion.css('a::attr(href)').get()
            full_url = self.base_url + relative_link

            # creation de l'item avec les informations déjà disponibles
            item = LegendItem()
            item['name'] = champion.css('span::attr(data-champion)').get()
            item['role'] = champion.css('span::attr(data-role)').get()
            item['type'] = champion.css('span::attr(data-type)').get()
            item['image_url'] = champion.css('img::attr(data-src)').get()

            #passer l'item et le full_url pour récupérer les détails
            yield scrapy.Request(url=full_url, callback=self.parse_champion_details, meta={'item': item})

    def parse_champion_details(self, response):
        # récupérer l'item passé via meta
        item = response.meta['item']

        #s statistiques dans les balises span
        try:
            move_speed = response.xpath('//div[@data-source="ms"]//span/text()').get()
            attack_range = response.xpath('//div[@data-source="range"]//span/text()').get()

            # ajout des valeurs dans l'item
            item['move_speed'] = move_speed.strip() if move_speed else "Unknown"
            item['attack_range'] = attack_range.strip() if attack_range else "Unknown"
        except Exception as e:
            self.logger.error(f"Error parsing champion details: {e}")
            item['move_speed'] = "Error"
            item['attack_range'] = "Error"

        # logs pour vérifier les données extraites
        self.logger.info(f"Parsed champion: {item['name']}")
        self.logger.info(f"Move Speed: {item['move_speed']}, Attack Range: {item['attack_range']}")
        yield item
