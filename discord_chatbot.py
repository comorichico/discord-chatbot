from dotenv import load_dotenv
import os
import discord
import access_openai_api
import prompt

intents = discord.Intents.all()
client = discord.Client(intents=intents)
prompt= prompt.Prompt()

load_dotenv()

discord_bot_token = os.environ["DISCORD_BOT_TOKEN"]

@client.event
async def on_ready():
    print(f'{client.user.name}がログインしました。')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot:
        return
    
    if message.content == "デフォルト":
        prompt.character_no = prompt.character_default
        await message.channel.send("性格をデフォルトに変更しました。よろしくお願いします。")
        return

    if message.content == "ツンデレ":
        prompt.character_no = prompt.character_tsundere
        await message.channel.send("性格をツンデレに変更したわ。べ、別にあんたのためじゃないんだからねっ！")
        return
    
    if message.content == "俺様":
        prompt.character_no = prompt.character_oresama
        await message.channel.send("性格を俺様に変更した。よろしく頼む。")
        return
    
    if message.content == "お嬢様":
        prompt.character_no = prompt.character_ojousama
        await message.channel.send("性格をお嬢様に変更しましたわ。よろしくお願い致します。")
        return

    if message.channel.id == 1118776764668317696 or \
        message.channel.id == 1118801068474777621 or \
        message.channel.id == 1118801259072335925:
        reply = access_openai_api.access_openai_api.generate_response(prompt, message.content)
        prompt.append_prompt(message.content, reply)
        await message.channel.send(reply[0:1950])

client.run(discord_bot_token)