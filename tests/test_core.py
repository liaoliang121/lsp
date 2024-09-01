import unittest
from src.core import LSPServer
class TestLSPServer(unittest.TestCase):
    def test_init(self):
        server = LSPServer({})
        self.assertIsNotNone(server)
# Update at 2024-09-01T15:18:19
