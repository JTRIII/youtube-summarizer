import ollama
import re
from youtube_transcript_api import YouTubeTranscriptApi


#####################################################################
# Extract YouTube video ID from video link using regex
#####################################################################
def get_video_id(url):
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)

    if match:
        return match.group(1)
    else:
        return None


#####################################################################
# Use video ID to extract transcript using youtube-transcript-api
#####################################################################
def extract_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    video_text = ""
    for script in transcript:
        text = "".join(script['text'])
        video_text += text + "\n" 
    return video_text


#####################################################################
# Experiment with different prompts that effectively summarize the transcript
#####################################################################

def summarize_transcript(transcript):
    # prompt = f"Summarize the following YouTube video transcript:\n\n{transcript}\n\nSummary:"
    # prompt = f"Summarize the following YouTube video transcript, breaking it down into key sections such as introduction, main points, and conclusion:\n\n{transcript}\n\nSummary (include Introduction, Key Points, and Conclusion):"
    prompt = f"Summarize the following YouTube video transcript in a way that provides all key details, insights, and explanations so that the reader does not need to watch the video. Make sure to cover all important topics in detail, providing examples if available:\n\n{transcript}\n\nComprehensive Summary:"

    try:
        # Call the LLaMA 3 model via Ollama
        response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": prompt}])
        # Access the correct part of the response
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"


#############
# Main
#############
if __name__ == "__main__":

    # Get URl from user
    url = input("Please enter your YouTube URL: ")

    video_id = get_video_id(url)
    transcript = extract_transcript(video_id)
    summary = summarize_transcript(transcript)
    print(f"Summary: {summary}")
