from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN" "8867636200:AAHC0dWdhWrkVUWzg0eUALsW0eTdsQRUB48")

MONGO_URL = getenv("mongodb+srv://yash827830_db_user:DyLsRtr2W1iLL8SK@yash.yprhxeh.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID", 8203857803))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+b9RbWnTQ4PFiNjZl")