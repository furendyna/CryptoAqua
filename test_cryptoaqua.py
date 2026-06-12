# test_cryptoaqua.py
"""
Tests for CryptoAqua module.
"""

import unittest
from cryptoaqua import CryptoAqua

class TestCryptoAqua(unittest.TestCase):
    """Test cases for CryptoAqua class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoAqua()
        self.assertIsInstance(instance, CryptoAqua)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoAqua()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
