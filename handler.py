def handler(event):
    job_input = event.get("input", {}) or {}

    text = job_input.get("text", "Hello, this is XTTS.")
    speaker_wav = job_input.get("speaker_wav", None)
    speaker = job_input.get("speaker", None)  # NEW

    tts = load_model()

    kwargs = {
        "text": text,
        "language": "en",
    }

    # If you provide a speaker_wav, XTTS will voice-clone from it.
    if speaker_wav:
        kwargs["speaker_wav"] = speaker_wav
    else:
        # Fallback to a named speaker if no wav provided
        kwargs["speaker"] = speaker or "female_01"

    wav = tts.tts(**kwargs)
    return {"audio": wav.tolist()}
