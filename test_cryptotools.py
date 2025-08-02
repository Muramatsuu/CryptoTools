# test_cryptotools.py
"""
Tests for CryptoTools module.
"""

import unittest
from cryptotools import CryptoTools

class TestCryptoTools(unittest.TestCase):
    """Test cases for CryptoTools class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoTools()
        self.assertIsInstance(instance, CryptoTools)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoTools()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
