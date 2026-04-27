from dotenv import load_dotenv
import os

load_dotenv()

COMMON_PASSWORD = os.getenv("COMMON_PASSWORD")
NEW_PASSWORD = os.getenv("NEW_PASSWORD")