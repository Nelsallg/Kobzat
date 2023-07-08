import os

class GetData:
    def intents(filename:str = 'intents.json')->str:
        """Load intents files"""
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(BASE_DIR, filename)

    def trainnedModel(foldername:str = 'chatbox_model')->str:
        """Load trainned model"""
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(BASE_DIR, foldername)