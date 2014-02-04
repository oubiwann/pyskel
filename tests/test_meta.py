import unittest

from skellib import meta


class MetaTestCase(unittest.TestCase):
    """
    """
    def test_display_name(self):
        self.assertEqual(meta.display_name, "Skeleton Library")
