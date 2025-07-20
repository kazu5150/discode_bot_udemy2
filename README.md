# Discord Bot

OpenAI APIを使用してAI画像生成ができるDiscord Botです。

## セットアップ

1. 依存関係のインストール
```bash
pip install -r requirements.txt
```

2. 環境変数の設定
`.env`ファイルを作成して、以下の環境変数を設定してください：

```
DISCORD_BOT_TOKEN=your_discord_bot_token_here
OPENAI_API_KEY=your_openai_api_key_here
```

3. Discord Developer Portalでの設定
- [Discord Developer Portal](https://discord.com/developers/applications/)でアプリケーションを作成
- Bot設定でMessage Content Intentを有効化
- BotトークンをコピーしてDISCORD_BOT_TOKENに設定

4. Botの起動
```bash
python bot.py
```

## 機能

- `!generate [プロンプト]` または `!画像生成 [プロンプト]` コマンドでAI画像を生成
- gpt-image-1モデルを使用して高品質な画像を生成
- 生成された画像はDiscordチャンネルに直接投稿

## 使用例

```
!generate 夕日が沈む美しい海岸線
!画像生成 宇宙に浮かぶ未来都市
```

## 必要な権限

- メッセージの読み取り
- メッセージの送信
- ファイルの添付（画像送信用）
- Message Content Intent（必須）