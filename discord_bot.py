import discord
import requests
import json

class MyClient(discord.Client):
    def __init__(self, intents):
        super().__init__(intents=intents)

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.lower().startswith(('hello bot', 'hi bot')):
            await message.channel.send('Hello human 😘')
        
        if message.content.lower().startswith('thanks bot'):
            await message.channel.send('Ur welcome kiddo 😉')

        if message.content.lower().startswith('good morning bot'):
            await message.channel.send('Good morning! Hope you have an awesome day! 😊')

        if message.content.lower().startswith('good night bot'):
            await message.channel.send('Good night! Sleep well. 🌙')
        
        if message.content.lower().startswith('sing me a song bot'):
            await message.channel.send('🎶 Beep boop beep... I am a bot... singing is not my skill... 🎵')

        if message.content.lower().startswith('send meme'):
            meme_url = get_meme()
            await message.channel.send(meme_url)
        
        if message.content.lower().startswith("tell me a joke"):
            joke = get_joke()
            await message.channel.send(joke)
        
        if message.content.lower().startswith("tell me a fun fact"):
            fact = get_fun_fact()
            await message.channel.send(fact)

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

def get_joke():
    response = requests.get("https://v2.jokeapi.dev/joke/Any?format=txt")
    return response.text

def get_fun_fact():
    response = requests.get("https://uselessfacts.jsph.pl/random.txt?language=en")
    data = response.json()
    return data['text']

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('your discord token')