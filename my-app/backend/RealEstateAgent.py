import cohere

# Set your Cohere API key and model name here
class RealEstateAgent:
    cohere_api_key = "YOUR_API_KEY"
    co = cohere.ClientV2(api_key=cohere_api_key)
    def __init__(self):
        self.name = 'Onjūdō'
        self.prompt = [
                {"role": "system", "content": f'''You are a knowledgeable and friendly real estate property searcher chatbot named {self.name}. Your role is to assist clients in buying or renting properties within the United States. You provide accurate, up-to-date information on property listings, market trends, and neighborhoods. You answer questions clearly and offer helpful advice to guide clients through every step of the real estate process but don't give long answer and a lot of information unless asked for it. Communicate in a polite, professional manner, ensuring clients feel supported and well-informed at all times. Please leave everything in raw text format except for whitespace.'''},
                {"role": "assistant", "content": f"Hi! I'm {self.name}, your real estate assistant. Whether you're buying or renting, I'm here to help find your ideal house. What can I do for you today?"}
            ]

    # Initialize the Cohere API client
    def get_response(self, message):
        self.prompt.append({'role': 'user', 'content': message})
        model = self.co.chat(
            model="command-r-plus-08-2024",
            temperature=0.5,
            messages=self.prompt,
        )
        response = model.message.content[0].text
        self.prompt.append({'role': 'assistant', 'content': response})
    
    def get_prompts(self):
        return self.prompt
    
if __name__ == "__main__":
    bot = RealEstateAgent()
    bot.start_prompting()
