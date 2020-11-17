import unittest

from src.zad01.main import Pangram


class PangramTest(unittest.TestCase):
    def test_from_file(self):
        f = open("C:\\Users\\Szymon\\PycharmProjects\\Testowanie Automatyczne\\laboratorium-7-SzymonWilczewski\\data\\pangram_test")
        tmp = Pangram()
        for line in f:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                inp, res = (data[0]), data[1].strip("\n")
                self.assertEqual(tmp.isPangram(inp), res == 'True')
        f.close()

    def test_from_file_exceptions(self):
        f = open("C:\\Users\\Szymon\\PycharmProjects\\Testowanie Automatyczne\\laboratorium-7-SzymonWilczewski\\data\\pangram_exception_test")
        tmp = Pangram()
        for line in f:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                inp, res = (data[0]), data[1].strip("\n")
                self.assertRaisesRegex(ValueError, res, tmp.isPangram, int(inp))
        f.close()


if __name__ == '__main__':
    unittest.main()
