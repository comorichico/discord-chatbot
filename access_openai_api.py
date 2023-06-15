import openai
import os
from dotenv import load_dotenv

class access_openai_api:

    def generate_response(prompt, content):
        try:
            # OpenAI ChatGPT(gpt-3.5-turbo)APIを使用して応答を生成
            load_dotenv()
            openai.api_key = os.environ["OPENAI_API_KEY"]

            messages = []
            print(prompt.character_no)
            messages = prompt.default_prompt[prompt.character_no] + prompt.prompt
            messages.append({"role": "user", "content": content})
            print(messages)

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            return response['choices'][0]['message']['content']
        
        except Exception as e:
            print(str(e))
            response = "現在OpenAIのAPIサーバー側で"
            response += "問題が発生しているようです。"
            response += "しばらく時間を置いてから"
            response += "やり直してほしいです。申し訳ないです。"
            # エラーが発生した場合は、エラーメッセージを返す
            return response