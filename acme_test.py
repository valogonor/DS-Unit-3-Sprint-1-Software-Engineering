#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    """Test default product weight being 20."""
    def test_default_product_weight(self):
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealability_default(self):
        prod = Product('Test Product')
        self.assertEqual(prod.stealability(), "Kinda stealable.")

    def test_stealability_weight100(self):
        prod = Product('Test Product', weight=100)
        self.assertEqual(prod.stealability(), "Not so stealable...")

    def test_stealability_weight5(self):
        prod = Product('Test Product', weight=5)
        self.assertEqual(prod.stealability(), "Very stealable!")

    def test_flammability_default(self):
        prod = Product('Test Product')
        self.assertEqual(prod.explode(), "...boom!")

    def test_flammability_weight100(self):
        prod = Product('Test Product', weight=100)
        self.assertEqual(prod.explode(), "...BABOOM!!")

    def test_flammability_weight5(self):
        prod = Product('Test Product', weight=5)
        self.assertEqual(prod.explode(), "...fizzle.")


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        products = generate_products()
        names = []
        for i in products:
            names.append(i.name)
        for i in names:
            words = i.split()
            self.assertIn(words[0], ADJECTIVES)
            self.assertIn(words[1], NOUNS)


if __name__ == '__main__':
    unittest.main()
