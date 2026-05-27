import runpod
from TTS.api import TTS

model = None

def load_model():
    global model
    if model is None:
        model = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cuda")
    return model

def handler(event):
    text = event.get("input", {}).get("text", "Hello, this is XTTS.")
    speaker_wav = event.get("input", {}).get("speaker_wav", None)

    tts = load_model()

    wav = tts.tts(
        text=text,
        speaker_wav=speaker_wav,
        language="en"
    )

    return {"audio": wav.tolist()}

runpod.serverless.start({"handler": handler})
