import pyaudio
import wave
import threading
import os

class AudioRecorder:
    def __init__(self):
        self.frames = []
        self.is_recording = False

    def record_audio(self):
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=2, rate=44100, input=True, frames_per_buffer=1024)
        print("\nListening...")
        
        while self.is_recording:
            data = stream.read(1024)
            self.frames.append(data)

        stream.stop_stream()
        stream.close()
        p.terminate()

    def save_audio(self):
        filename = "audio.wav"
        wf = wave.open(filename, 'wb')
        wf.setnchannels(2)
        wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(self.frames))
        wf.close()

        # Get file size
        file_size = os.path.getsize(filename)
        print(f"File size: {file_size/1000000} MB")

        # Get audio length
        with wave.open(filename, 'rb') as f:
            frames = f.getnframes()
            rate = f.getframerate()
            length = frames / float(rate)
            print(f"Audio length: {length:.2f} seconds")

    def start(self):
        input("Press Enter to start recording...")
        self.is_recording = True
        self.t = threading.Thread(target=self.record_audio)
        self.t.start()

    def stop(self):
        input("Press Enter again to stop recording...")
        self.is_recording = False
        self.t.join()
        self.save_audio()
        print("Audio saved as audio.wav.")

if __name__ == "__main__":
    recorder = AudioRecorder()
    recorder.start()
    recorder.stop()
