"""Example using add_url_rule."""
from flask import Flask


app = Flask(__name__)


def german():
    return "Willkommen"


def రేమకు_స్వాగతం():
    """swagatham in telugu language."""
    app.add_url_rule('/german', None, german)
    return "రేమకు స్వాగతం"


def நல்வரவு():
    """swagatham in tamil language."""
    return "நல்வரவு"


def ಸುಸ್ವಾಗತ():
    """swagatham in kannada language."""
    return "ಸುಸ್ವಾಗತ"


if __name__ == '__main__':
    rules = {
        'telugu': రేమకు_స్వాగతం,
        'tamil': நல்வரவு,
        'kannada': ಸುಸ್ವಾಗತ
    }
    for rule, func in rules.items():
        print(rule, func)
        app.add_url_rule('/' + rule, None, func)
    app.run()