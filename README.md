# YouTube Summarizer

Watching an entire youtube video to get some information can be a hassel. This program retrieves the transcript from a YouTube video and passes it to the Llama 3.2 LLM to generate a concise summary with important details. This allows users to quickly access relevant information without having to watch the full video.

---

# Installation and Use of the Program

## 1. Clone Respoitory
```
git clone https://github.com/JTRIII/youtube-summarizer.git
cd youtube-summarizer
```

## 2. Install Ollama & Download the LLaMA Model
#### Install Ollama
Ollama is required to run the LLaMA model locally. Follow the installation steps for your OS:
- Windows & Mac: Download and install Ollama from [ollama.com](https://ollama.com/)
- Linux: Install using the following command:
```
curl -fsSL https://ollama.com/install.sh | sh
```

#### Download the LLaMA 3.2 Model
Once Ollama is installed, pull the required model by running:
```
ollama pull llama3.2
```

## 3. Set up Virtual Environment

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

## 4. Upgrade Pip
```
pip install --upgrade pip
```

## 5. Download Dependencies
```
pip install -r requirements.txt
```

## 6. Run the program

#### Windows
```
python yt_summarizer.py
```

#### Mac or Linux
```
python3 yt_summarizer.py
```

## 7. Paste the YouTube URL
Once the program runs, simply paste the YouTube video link when prompted, and the summarizer will generate a detailed summary for you.

---

## Notes
- Ensure you have Python 3.8 or higher installed.

- If you encounter issues with dependencies, try running `pip install --upgrade pip setuptools wheel` before installing requirements.

- You may need to install `ffmpeg` if your system lacks support for YouTube transcripts.

- If Ollama isn't working properly, restart your terminal after installing it.