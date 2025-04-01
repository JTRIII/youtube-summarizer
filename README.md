# YouTube Summarizer

Watching an entire youtube video to get some information can be a hassel. This program retrieves the transcript from a YouTube video and passes it to the Llama 3.2 LLM to generate a concise summary with important details. This allows users to quickly access relevant information without having to watch the full video.

---

# Installation and Use of the Program

## 1. Clone Respoitory
```
git clone https://github.com/JTRIII/youtube-summarizer.git
cd youtube-summarizer
```

## 2. Set up Virtual Environment

#### Windows
```
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate
```

#### Mac or Linux
```
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

## 3. Upgrade Pip
```
pip install --upgrade pip
```

## 4. Download Dependencies
```
pip install -r requirements.txt
```

## 5. Run the program

#### Windows
```
python yt_summarizer.py
```

#### Mac or Linux
```
python3 yt_summarizer.py
```

## 6. Paste the YouTube URL
Once the program runs, simply paste the YouTube video link when prompted, and the summarizer will generate a detailed summary for you.