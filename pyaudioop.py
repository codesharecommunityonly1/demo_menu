# Dummy pyaudioop module to fix import error
# This is a workaround for Hugging Face Spaces


class AudioSegment:
    pass


audioop = type("audioop", (), {})()
