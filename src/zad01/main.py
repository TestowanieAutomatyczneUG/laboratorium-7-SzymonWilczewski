class Pangram:
    def isPangram(self, string):
        if type(string) is not str:
            raise ValueError("Wrong value")
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for char in alphabet:
            if char not in string.lower():
                return False
        return True
