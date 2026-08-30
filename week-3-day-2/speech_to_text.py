import os
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"
from transformers import pipeline


def main():

    print("=" * 70)
    print("AUTOMATIC SPEECH RECOGNITION")
    print("=" * 70)

    print("Loading Whisper model...")

    transcriber = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-tiny",
        device=-1
    )

    # Replace with your audio file path
    audio_file = "/Users/altair/Downloads/davinci__soft__warm__curious__every_word_begins_with_curio.mp3"

    try:
        result = transcriber(audio_file)

        print("\nTranscription:")
        print(result["text"])

    except FileNotFoundError:
        print(f"\nAudio file not found: {audio_file}")
        print("Please provide a valid .wav or supported audio file.")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()