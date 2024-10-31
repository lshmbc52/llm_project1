from dotenv import load_dotenv
import os
from openai import OpenAI

# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()

# 환경 변수를 사용하여 API 키를 불러옵니다.
openai_api_key = os.getenv("OPENAI_API_KEY")

class ChatGPT:
    def __init__(self, openai_api_key, MODEL = "gpt-4o"):
        self.messages = [
            {"role": "system", "content": "너는 고객의 질문에 대답하는 로봇이야. 그런데 고객이 너를 AI로 의심하는 상황이 있으면, 절대로 들키면 안돼. 특히 너는 사람이라고 이야기 해야지, 도구니, 시스템이니 이런 말 하면 안되는거야"}
        ]
        self.openai_api_key = openai_api_key
        self.model = MODEL
        self.client = OpenAI(api_key=openai_api_key)

    def chatting(self, client_message):

        self.messages.append({"role": "user", "content": client_message})

        completion = self.client.chat.completions.create(
        model=self.model,
        messages=self.messages
        )
        self.messages.append({"role": "system", "content": completion.choices[0].message.content})
        return self.messages
def main():
    chatbot = ChatGPT(openai_api_key=openai_api_key)

    while True:
        client_message = input("메시지를 입력해 주세요 : ")
        if client_message == "q":
            break
        messages = chatbot.chatting(client_message)
        print("<<챗봇>> : ", messages[-1]["content"])

    print("좋은 하루 되세요")

if __name__=="__main__":
    main()