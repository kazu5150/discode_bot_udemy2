import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from openai import OpenAI
import base64
from io import BytesIO

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

@bot.command(name='generate', aliases=['画像生成'])
async def generate_image(ctx, *, prompt: str):
    """画像生成コマンド"""
    try:
        # 処理中のメッセージを送信
        await ctx.send(f'「{prompt}」の画像を生成中...')
        
        # gpt-image-1を使用して画像を生成
        response = client.images.generate(
            model="gpt-image-1",
            prompt=prompt
        )
        
        # 生成された画像のbase64データを取得
        image_base64 = response.data[0].b64_json
        image_bytes = base64.b64decode(image_base64)
        
        # BytesIOオブジェクトを作成
        image_data = BytesIO(image_bytes)
        
        # Discord.pyのFileオブジェクトを作成
        file = discord.File(image_data, filename='generated_image.png')
        
        # 画像をDiscordに送信
        await ctx.send(f'「{prompt}」の画像を生成しました！', file=file)
        
    except Exception as e:
        print(f'画像生成エラー: {e}')
        await ctx.send('申し訳ありません。画像の生成中にエラーが発生しました。')

@bot.event
async def on_message(message):
    # Bot自身のメッセージには反応しない
    if message.author == bot.user:
        return
    
    # デバッグ用：受信したメッセージをログに出力
    print(f'受信: {message.author}: {message.content}')
    
    # コマンド処理を有効にする
    await bot.process_commands(message)

# Botを起動
bot.run(os.getenv('DISCORD_BOT_TOKEN'))