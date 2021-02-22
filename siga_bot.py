import os
import pathlib
import time
from datetime import datetime

import discord
from discord.ext import commands

from SharedLibrary import *

bot = commands.Bot(command_prefix=os.getenv('PREFIX'), help_command=None)


@bot.command(name='help', aliases=['h', 'ajuda'])
async def help(ctx):
    embed = discord.Embed(title="Olá, Posso ajudar?", colour=discord.Colour(0xff0000),
                          description="Meu nome é SigaBot. Fui criado para facilitar a vida dos alunos com o acesso ao SIGA - UFRJ")

    embed.set_footer(icon_url=discord_utils.bot_icon,
                     text="Usado às {} Horário de Brasília | © {} {} .".format(datetime.now().strftime("%H:%M"),
                                                                               bot.user.name,
                                                                               datetime.now().strftime("%Y")))

    embed.add_field(name="📜 **document<Login> <Senha> <Tipo do Documento>**", value="Acessa o siga para você e envia no privado o seu documento.",
                    inline=False)

    await ctx.send(embed=embed)


if __name__ == '__main__':
    for cog_file in pathlib.Path('Cogs').glob('*.py'):
        try:
            cog_file = str(cog_file).replace(".py", "")
            cog_file = str(cog_file).replace("/", ".")
            bot.load_extension(cog_file)
        except Exception as ex:
            exception = '{}: {}'.format(type(ex).__name__, ex)
            print('Falha ao carregar a extensão {}\n{}'.format(cog_file, exception))


bot.run(os.getenv('TOKEN'))
