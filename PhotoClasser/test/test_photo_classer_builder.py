import unittest
from PhotoClasser import PhotoClasserBuilder


class TestStringMethods(unittest.TestCase):

    def test_builder_with_src_and_dst_dir(self):
        myobj = PhotoClasserBuilder().with_src('/tmp/src').with_dst('/tmp/dst').build()
        assert myobj

#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())
#
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)
#
# if __name__ == '__main__':
#     unittest.main()