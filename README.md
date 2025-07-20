# Discord Bot

シンプルなDiscord Botです。メッセージに対して「こんにちは」と返信します。

## セットアップ

1. 依存関係のインストール
```bash
pip install -r requirements.txt
```

2. 環境変数の設定
`.env.example`を`.env`にコピーして、Discord BotトークンをDISCORD_BOT_TOKENに設定してください。

```bash
cp .env.example .env
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

- すべてのメッセージに対して「こんにちは」と返信

## 必要な権限

- メッセージの読み取り
- メッセージの送信
- Message Content Intent（必須）