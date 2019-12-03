# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    # - At the end of each day our system lowers both values for every item
    def test_normal_item(self):
        items = [Item("foo", 5, 8)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(7, items[0].quality)    

    # - Once the sell by date has passed, Quality degrades twice as fast
    def test_passed_sell_in_date(self):
        items = [Item("foo", 1, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality) 


    # - The Quality of an item is never negative
    def test_quality_is_never_negative(self):
        items = [Item("foo", 5, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

        gilded_rose.update_quality()
        self.assertEqual(3, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    # "Aged Brie" actually increases in Quality the older it gets    
    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 5, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(2, items[0].quality)


    # The Quality of an item is never more than 50    
    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

        gilded_rose.update_quality()
        self.assertEqual(3, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    # "Sulfuras", being a legendary item, never has to be sold or decreases in Quality 
    def test_sulfuras_legendary_item(self):
        items = [Item("Sulfuras", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(49, items[0].quality)


if __name__ == '__main__':
    unittest.main()
