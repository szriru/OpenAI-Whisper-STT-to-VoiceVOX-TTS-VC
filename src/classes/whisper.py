import whisper
import json
import os
import torch  

isCuda = torch.device("cuda" if torch.cuda.is_available() else "cpu") 
class Whisper:
    def __init__(self, modelname="small", device =isCuda) -> None:
        self.modelname = modelname
        self.device = device
        self.model = whisper.load_model(self.modelname, device=device)
    
    def ToText(self, filename="./audio/recorded_audio.wav") -> str:
        result = self.model.transcribe(filename)
        return result
        
        