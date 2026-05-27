import os

# Prevent Coqui TTS from prompting for Terms-of-Service acceptance (no stdin on Serverless).
os.environ["COQUI_TOS_AGREED"] = "1"

import runpod
from TTS.api import TTS

model = None

def load_model():
    global model
    if model is None:
        # Loads XTTS v2 onto the GPU
        model = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cuda")
    return model

def handler(event):
    job_input = event.get("input", {}) or {}

    text = job_input.get("text", "Hello, this is XTTS.")
    speaker_wav = job_input.get("speaker_wav", None)

    tts = load_model()

    wav = tts.tts(
        text=text,
        speaker_wav=speaker_wav,
        language="en"
    )

    # Return audio as a JSON-serializable list of floats
    return {"audio": wav.tolist()}

runpod.serverless.start({"handler": handler})
