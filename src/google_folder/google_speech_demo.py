from google.cloud import speech

def transcribe(gcs_uri: dict):
    path_type = "gcs"
    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(uri=gcs_uri[path_type])
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        model = "latest_long",
        sample_rate_hertz=44100,
        language_code="en-US"
    )

    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=10000)
    transcript_builder = []
    for result in response.results:
        transcript_builder.append(f"{result.alternatives[0].transcript}")
    transcript = "".join(transcript_builder)

    return transcript

if __name__ == "__main__":
    file_name = {"gcs": 'gs://song_list/alone.mp3'}
    transcribe(file_name)


