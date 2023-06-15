# discord-chatbot
discordで動くチャットボット作るよ！

sample.envのファイル名を.envに書き換えてください

https://discord.com/developers/applications
ここから取得したTOKENを.envのDISCORD_BOT_TOKENに設定します

https://platform.openai.com/account/api-keys
ここから取得したapikeyをOPENAI_API_KEYに設定します

discord_chatbot.pyの中に
「message.channel.id ==」
と書いてる行があるのでそこの数字を使用したいチャンネルIDに置き換えます

Pythonをインストールしていない人はMicrosoft StoreからPython3.11をインストールしてください。

コマンドプロンプト、PowerShell、ターミナルなどで以下のコマンドを実行します。

pip install openai

pip install discord.py

最後にチャットボット本体を起動します

python discord_chatbot.py

これであとはdiscordで指定したテキストチャンネルで会話できるはずです。

おつかれさまでした！
