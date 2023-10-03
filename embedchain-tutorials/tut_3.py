from dotenv import load_dotenv
from embedchain import Llama2App

if __name__ == '__main__':
    load_dotenv()
    bot = Llama2App()
    bot.add("https://en.wikipedia.org/wiki/Elon_Musk")
    bot.add("https://www.forbes.com/profile/elon-musk")

    response = bot.query('Give me compaines names owned by Elon Mask?')
    print(response)
