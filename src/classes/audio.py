import pyaudio
import wave
from typing import List, Union

def append_unique(lst, element):
    if element not in lst:
        lst.append(element)

# Make it possible to use same pyAudio instance as one.
class SharedPyaudio:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = pyaudio.PyAudio()
        return cls.instance

class AudioPlayer:
    def __init__(self, output_device_indices: Union[List[int], List[None]]=[]):
        self.p = SharedPyaudio.get_instance()
        self.output_device_indices = output_device_indices
        default_device = self.p.get_default_output_device_info()['index']
        append_unique(output_device_indices, default_device)
        self.streams = [None] * len(output_device_indices)

    def play_all(self, filename):
        wf = wave.open(filename, 'rb')
        for stream_idx, output_device_index in enumerate(self.output_device_indices):      
            self.open_stream(
                output_device_index=output_device_index,
                stream_idx=stream_idx,
                wf=wf
                )
        chunk = 1024
        data = wf.readframes(chunk)
        while data != b'':
            for stream in self.streams:
              stream.write(data)
            data = wf.readframes(chunk)
        self.close_all_stream()

    def open_stream(self,output_device_index, stream_idx, wf):
        self.streams[stream_idx] = self.p.open(
            format=self.p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True,
            output_device_index=output_device_index)
        
    def close_all_stream(self):
        for stream in self.streams:
            self.close_stream(stream)

    def close_stream(self, stream):
        if stream is not None:
            stream.stop_stream()
            stream.close()
            stream = None

    def terminate(self):
        self.close_stream()
        self.p.terminate()

class Recorder:
    def __init__(self) -> None:
        # Set parameters for recording
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024

        # Create PyAudio object
        self.p = SharedPyaudio.get_instance()

        # Create array to save
        self.frames = []
        
    def openStream(self) -> None:
        self.stream = self.p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)
        
    def stopRecording(self) -> None:
        self.stream.stop_stream()
        self.stream.close()

    def saveAsWav(self, filename="./audio/recorded_audio.wav") -> None:
        # save recorded audio as .wav file
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        self.frames = []

        print("Audio saved as recorded_audio.wav.")