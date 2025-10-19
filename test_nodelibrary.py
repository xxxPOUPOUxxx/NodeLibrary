# test_nodelibrary.py
"""
Tests for NodeLibrary module.
"""

import unittest
from nodelibrary import NodeLibrary

class TestNodeLibrary(unittest.TestCase):
    """Test cases for NodeLibrary class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NodeLibrary()
        self.assertIsInstance(instance, NodeLibrary)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NodeLibrary()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
