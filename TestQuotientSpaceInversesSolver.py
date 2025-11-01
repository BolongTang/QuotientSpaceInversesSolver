from unittest import main, TestCase
from QuotientSpaceInversesSolver import parse, find_unit_group, find_orders_and_inverses_for_units

class TestQSSolver(TestCase):
    def test_parse1(self):
        self.assertEqual(16, parse('Z/16Z'))
        
    def test_parse2(self):
        self.assertEqual(2, parse('Z/2Z'))
        
    def test_parse3(self):
        self.assertEqual(250, parse('Z/250Z'))
    
    def test_find_unit_group1(self):
        self.assertEqual({1, 3, 5, 7, 9, 11, 13, 15}, find_unit_group(16))
        
    def test_find_unit_group2(self):
        self.assertEqual({1}, find_unit_group(2))
        
    def test_find_unit_group3(self):
        self.assertEqual({1, 2, 3, 4, 5, 6}, find_unit_group(7))
        
    def test_find_orders_and_inverses_for_units1(self):
        self.assertEqual(({1:1, 3:4, 5:4, 7:2, 9:2, 11:4, 13:4, 15:2}, {1:1, 3:11, 5:13, 7:7, 9:9, 11:3, 13:5, 15:15}), find_orders_and_inverses_for_units({1, 3, 5, 7, 9, 11, 13, 15}, 16))
        
if __name__ == "__main__":
    main()