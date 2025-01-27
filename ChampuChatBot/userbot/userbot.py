import asyncio
from os import getenv
from config import OWNER_ID
from dotenv import load_dotenv
from pyrogram import Client
import config

class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="ChampuAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=False,
            plugins=dict(root="ChampuChatBot.idchatbot"),
        )
        

    async def start(self):
        print(f"Starting Id chatbot...")

        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("V2ddos")
                await self.one.join_chat("CreativeYdv")
                await self.one.join_chat("Music_4_Sukoon")
                await self.one.join_chat("NYCreation_Chatzone")

            except:
                pass
            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
     
            print(f"Id-Chatbot Started as {self.one.me.first_name}")
            
        

    async def stop(self):
        LOGGER(__name__).info(f"Stopping Id-Chatbot...")
        try:
            if config.STRING1:
                await self.one.stop()
        except:
            pass
