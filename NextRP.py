import discord # Подключаем библиотеку
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

link = 'https://status.nextrp.ru/'
response = requests.get(link).text
soup = BeautifulSoup(response, 'lxml')
block = soup.find('div',"systems-container flex flex-col system-2")
check_server = block.find_all('div', "system-title")
status_server = block.find_all('span', 'sm:inline')


intents = discord.Intents.default() # Подключаем "Разрешения"
intents.message_content = True
# Задаём префикс и интенты
bot = commands.Bot(command_prefix='!', intents=intents)


# С помощью декоратора создаём первую команду
@bot.command()
async def сервинфо(ctx):
    for i in range(0, len(check_server) - 1):
         await ctx.send(check_server[i].text + ' - ' + status_server[i].text)

@bot.command()
async def сервчек(ctx):
    counton = 0
    countoff = 0
    for i in range(0, len(check_server) - 1):
        if status_server[i].text == 'Доступно':
            counton += 1
        elif status_server[i].text == 'Недоступно':
            countoff += 1
        else:
            pass
    await ctx.send('Доступных серверов: {0}; Недоступных серверов: {1}'.format(counton,countoff))

bot.run('')

