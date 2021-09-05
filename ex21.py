# Setting up env using python-dotenv

import os

from dotenv import load_dotenv

load_dotenv()



password=os.getenv("PASSWORD")
print(password)