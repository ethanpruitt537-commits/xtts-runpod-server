import base64, tempfile

def handler(event):
    job_input = event.get("input", {}) or {}

    text = job_input.get("text", "Hello, this is XTTS.")
    language = job_input.get("language", "en")

    speaker_wav_b64 = job_input.get("speaker_wav_b64")
    if not speaker_wav_b64:
        return {"error": "Missing required field: input.speaker_wav_b64 (base64 WAV)."}

    # Write the speaker audio to a temp wav file
    wav_bytes = base64.b64decode(speaker_wav_b64)
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        f.write(wav_bytes)
        speaker_path = f.name

    tts = load_model()

    wav = tts.tts(
        text=text,
        speaker_wav=speaker_path,
        language=language
    )

    return {"audio": wav.tolist()}
