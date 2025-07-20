import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込み
load_dotenv()

# Botの初期設定
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} としてログインしました')

@bot.event
async def on_message(message):
    # Bot自身のメッセージには反応しない
    if message.author == bot.user:
        return
    
    # デバッグ用：受信したメッセージをログに出力
    print(f'受信: {message.author}: {message.content}')
    
    # すべてのメッセージに対して"こんにちは"と返信
    await message.channel.send('こんにちは')
    
    # コマンド処理を有効にする
    await bot.process_commands(message)

# Botを起動
bot.run(os.getenv('DISCORD_BOT_TOKEN'))