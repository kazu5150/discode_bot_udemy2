# Discord Bot

OpenAI APIを使用してAIと会話ができるDiscord Botです。

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

- OpenAI APIを使用してメッセージに対してAIが返信
- GPT-3.5-turboモデルを使用
- 日本語での自然な会話が可能

## 必要な権限

- メッセージの読み取り
- メッセージの送信
- Message Content Intent（必須）