import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from openai import OpenAI

# .envファイルから環境変数を読み込み
load_dotenv()

# OpenAI クライアントの初期化
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

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
    
    try:
        # OpenAI APIを使用して応答を生成
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "あなたは親切で丁寧な日本語のアシスタントです。"},
                {"role": "user", "content": message.content}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # APIからの応答を取得して送信
        ai_response = response.choices[0].message.content
        await message.channel.send(ai_response)
        
    except Exception as e:
        print(f'エラーが発生しました: {e}')
        await message.channel.send('申し訳ありません。エラーが発生しました。')
    
    # コマンド処理を有効にする
    await bot.process_commands(message)

# Botを起動
bot.run(os.getenv('DISCORD_BOT_TOKEN'))