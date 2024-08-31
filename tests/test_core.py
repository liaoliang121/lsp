import unittest
from src.core import LSPServer
class TestLSPServer(unittest.TestCase):
    def test_init(self):
        server = LSPServer({})
        self.assertIsNotNone(server)
