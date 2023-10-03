from dotenv import load_dotenv
from embedchain import App


if __name__ == '__main__':
    load_dotenv()
    bot = App()


    bot.add("https://www.youtube.com/watch?v=3qHkcs3kG44")

    response = bot.query('Give me summary:')

    print(response)