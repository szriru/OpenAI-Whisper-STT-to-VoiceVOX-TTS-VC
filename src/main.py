from classes.whisper import Whisper
from classes.keyListener import KeyListener
from classes.audio import Recorder
from classes.voicevox import Voicevox
from classes.mouseListener import MouseListener
from classes.audio import AudioPlayer

import os
import yaml
import time

# Load config.yaml
current_dir = os.getcwd()
config_path = os.path.join(current_dir, 'config.yaml')
with open(config_path, 'r', encoding='utf-8') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

# Create Instances
KEYLISTENER = MouseListener(target=config["KEY_TO_SPEAK"]) if type(config["KEY_TO_SPEAK"]) == str else KeyListener(target=config["KEY_TO_SPEAK"])
WHISPER = Whisper(
    modelname=config["WHISPER_MODELNAME"],
    device=config["DEVICE"]
    )
VOICEVOX = Voicevox(
    speaker=config["VOICEVOX_SPEAKER"],
    voicevox_url=config["VOICEVOX_URL"]
    )
AUDIOPLAYER = AudioPlayer(output_device_indices=config["OUTPUT_AUDIO_DEVICE_ID"]) 
RECORDER = Recorder()

if __name__ == "__main__":
    print("Press {0} to start recording...".format(KEYLISTENER.target))

    while True:
        print("Ready")
        RECORDER.openStream()
        while True:
            if KEYLISTENER.target_state:
                print("Recording...")
                break
            # sleep for cpu usage
            time.sleep(0.05)
        
        while KEYLISTENER.target_state:
            data = RECORDER.stream.read(RECORDER.CHUNK)
            RECORDER.frames.append(data)
        else:
            print("Recording stopped.")
            RECORDER.stopRecording()
            RECORDER.saveAsWav()

            result = WHISPER.ToText()
            result = result["text"]

            VOICEVOX.text2Speech(
                text=result
                )

            AUDIOPLAYER.play_all(filename='./audio/output.wav')