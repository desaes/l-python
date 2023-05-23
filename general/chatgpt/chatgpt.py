import openai
import argparse
import json
import io
import os
import platform

class ChatGPT:
    def __init__(self, api_key, context_uuid, model="gpt-3.5-turbo"):
        self.path = os.path.join('tmp','chatgpt','messages')
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        self.api_key = api_key
        self.context_uuid = context_uuid
        self.messages = []
        if self.context_uuid:
            self.messages = self.read_messages()
        self.model = model
        openai.api_key = api_key
        

    def update_message(self, role, content):
        self.messages.append({"role": role, "content": content})
        if self.context_uuid:
            self.save_messages()
        
    def save_messages(self):
        if self.context_uuid:
            with io.open(f'{os.path.join(self.path, self.context_uuid)}', 'w', encoding='utf-8') as f:
                f.write(json.dumps(self.messages, ensure_ascii=False))
                
    def read_messages(self):
        if os.path.isfile(f'{os.path.join(self.path, self.context_uuid)}'):
            with io.open(f'{os.path.join(self.path, self.context_uuid)}', 'r', encoding='utf-8') as f:
                return json.loads(f.read())
        return []

    def get_answer(self, temperature=1, max_tokens=2048, top_p=1, frequency_penalty=0, presence_penalty=0):
        answer = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages
        )
        return answer['choices'][0]['message']['content']

    def ask(self):
        model_answer = self.get_answer()
        self.update_message("assistant", model_answer)
        return model_answer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Example",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("api-key", help="api-key")
    parser.add_argument("messages", help="messages")
    parser.add_argument("-u", "--context-uuid", help="context uuid")
    parser.add_argument("-m", "--model", help="chatgpt model")

    args = parser.parse_args()
    config = vars(args)
    print(config)
    print(config['messages'])
    print(config['api-key'])


    chatgpt = ChatGPT(api_key = config['api-key'], context_uuid=config['context_uuid'], model=config['model'])
    messages = config['messages'].split(';')
    for message in messages:
        role, content = message.split('&')
        chatgpt.update_message(role, content)
    print(chatgpt.ask())

