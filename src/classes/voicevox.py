import requests

class Voicevox:
    def __init__(self, speaker=3, voicevox_url="http://localhost:50021"):
        self.speaker = speaker
        self.voicevox_url = voicevox_url

    def text2Speech(self, text: str):
        url = f"{self.voicevox_url}/audio_query?text={text}&speaker={self.speaker}"
        headers = {"accept": "application/json"}

        r = requests.post(url, headers=headers)
        print(r.json()['kana'])

        url = f"{self.voicevox_url}/synthesis?speaker={self.speaker}&enable_interrogative_upspeak=true"
        headers = {
            "accept": "audio/wav",
            "Content-Type": "application/json"
        }
        payload = r.json()
        r = requests.post(url, json=payload, headers=headers)

        with open("./audio/output.wav", "wb") as f:
            f.write(r.content)