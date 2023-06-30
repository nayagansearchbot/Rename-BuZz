import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "28836709
")

API_HASH = os.environ.get("API_HASH", "7141c6095cd69aa0278daa12faa0cbad")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6360912718:AAFZyAHK4mYrtZvbRd2_xYlPKt1wnxobhjQ") 

FORCE_SUB = os.environ.get("FORCE_SUB", "@TamilMob_BuZz") 

DB_NAME = os.environ.get("DB_NAME","moviebuzz")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://movibuzz203:movibuzz203@cluster0.iezk1yg.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '512649808').split()]

PORT = os.environ.get("PORT", "8080")
