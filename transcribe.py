import argparse
import whisper
import time

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Transcribe audio using OpenAI's Whisper model.")
    parser.add_argument("--model", type=str, required=True, choices=["tiny", "base", "small", "medium", "large", "turbo"],
                        help="Model size to use for transcription (tiny, base, small, medium, large, turbo).")
    parser.add_argument("--audio", type=str, required=True, help="Path to the audio file to transcribe.")
    parser.add_argument("--language", type=str, default=None, help="Language code for transcription (e.g., 'ar' for Arabic).")
    #parser.add_argument("--translate", action="store_true", help="Translate the audio to English.")

    # Parse arguments
    args = parser.parse_args()

    # Load the specified model
    start_loadingModel = time.time()
    print(f"Loading {args.model} model...")
    model = whisper.load_model(args.model)
    print(f"Elapsed time Loading model: {time.time() - start_loadingModel:.2f} seconds")

    # Transcribe the audio
    start_decodeAudio = time.time()
    print(f"Transcribing {args.audio}...")
    result = model.transcribe(args.audio, language=args.language, task="transcribe")

    # Print the results
    print("\nTranscription:\n")
    print(result["text"])

    print(f"Elapsed time Decoding audio: {time.time() - start_decodeAudio:.2f} seconds")

if __name__ == "__main__":
    # Record start time
    start_time = time.time()

    main()

    elapsed_time = time.time() - start_time
    print(f"Total Elapsed time: {elapsed_time:.2f} seconds")
