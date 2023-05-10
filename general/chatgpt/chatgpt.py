import openai

class ChatGPT:
    def __init__(self, api_key, model="gpt-3.5-turbo"):
        self.api_key = api_key
        self.messages = []
        self.model = model
        openai.api_key = api_key

    def update_context(self, role, content):
        self.messages.append({"role": role, "content": content})

    def get_response(self, temperature=1, max_tokens=2048, top_p=1, frequency_penalty=0, presence_penalty=0):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages
        )
        return response['choices'][0]['message']['content']

    def ask(self, user_input):
        self.update_context("user", user_input)
        model_response = self.get_response()
        self.update_context("assistant", model_response)
        return model_response
    
chat = ChatGPT(API_KEY)