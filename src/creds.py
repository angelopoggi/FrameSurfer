import os
from dotenv import load_dotenv,find_dotenv

class Creds:
    def __init__(self):
        self.load_variables()
    def load_variables(self):
        env_file = find_dotenv()
        try:
            load_dotenv(env_file)
        except Exception as e:
            print(e)
    def unsplash_creds(self):
        unsplash_creds = os.environ['UNSPLASH_KEY']
        return unsplash_creds

