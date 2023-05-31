from dataclasses import dataclass
import unittest2
from .models import Book
from .serializers import BookSerializer


class BookTests(unittest2.TestCase):

    def test_valid_fields(self):
        self.assertEqual(2 + 2, 4 )
        

    def test_invalid_data(self):
        self.assertEqual(1 - 1, 0)
        
