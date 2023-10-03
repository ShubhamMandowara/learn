import os
from embedchain import App
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    bot = App()

    bot.add("https://en.wikipedia.org/wiki/Elon_Musk")
    bot.add("https://www.forbes.com/profile/elon-musk")

    response = bot.query('How many compaines Elon Mask have it?')
    print(response)
