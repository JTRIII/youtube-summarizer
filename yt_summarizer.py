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
    prompt = f"""
    Generate a detailed summary of the following YouTube video transcript. Ensure the summary is so informative that the reader fully understands the content without needing to watch the video. 

    Structure the response as follows:
    - Introduction: Provide context about the speaker, their background, and the purpose of the video.
    - Step-by-step guide: Clearly outline key steps mentioned, including any specific techniques, tools, or real-world examples.
    - Challenges & Solutions: Highlight any potential difficulties mentioned and how to overcome them.
    - Key Takeaways: List actionable insights that viewers can apply immediately.
    - Conclusion: Summarize the final message, including any calls to action.

    Ensure clarity, completeness, and structure.

    Transcript:
    {transcript}

    Comprehensive Summary:
    """

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
