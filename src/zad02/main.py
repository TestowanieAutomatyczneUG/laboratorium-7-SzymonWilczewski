import re


class Password:
    def ValidPassword(self, password):
        if ' ' in password:
            raise ValueError
        return bool(re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$', password))
