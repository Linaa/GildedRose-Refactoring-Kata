# -*- coding: utf-8 -*-



class GildedRose(object):

    MAX_QUALITY = 50
    MIN_QUALITY = 0
    def __init__(self, items):
        self.items = items

    def update_quality_brie(self, item):
        item.sell_in -= 1
        item.quality = min(self.MAX_QUALITY, item.quality +1 )     

    def update_quality_backstage(self, item):
        item.sell_in -= 1
        if item.sell_in >= 10:
            item.quality = min(self.MAX_QUALITY, item.quality +1 ) 
        elif item.sell_in >= 5:
            item.quality = min(self.MAX_QUALITY, item.quality +2 )     
        elif item.sell_in >= 0:
            item.quality = min(self.MAX_QUALITY, item.quality +3 )
        else:
            item.quality = self.MIN_QUALITY    
            

    def update_quality_conjured(self, item):
        item.sell_in -= 1
        if item.sell_in < 0:
            # passed sell-in degrades 4 point per day
            item.quality = max(self.MIN_QUALITY, item.quality -4 )   
        else:
            item.quality = max(self.MIN_QUALITY, item.quality -2 ) 

    def update_quality_standard(self, item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = max(self.MIN_QUALITY, item.quality -2 )   
        else:
            item.quality = max(self.MIN_QUALITY, item.quality -1 ) 

        
    def update_quality(self):
        for item in self.items:
            if item.name == item.BRIE:
                self.update_quality_brie(item)
            elif item.name == item.BACKSTAGE:
                self.update_quality_backstage(item)
            elif item.name == item.CONJURED:
                self.update_quality_conjured(item)        
            elif item.name != item.SULFURAS:
                self.update_quality_standard(item)
            # for SULFURAS do nothing!    




class Item:
    SULFURAS = "Sulfuras, Hand of Ragnaros"
    BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
    BRIE = "Aged Brie"
    CONJURED = "Conjured Mana Cake"
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
