
# 🧠 GenAI Log Analyzer

An interactive, modular log analysis tool powered by OpenAI's GenAI. Supports multi-run parsing, anomaly detection, and natural-language querying via a Streamlit GUI.

## 🚀 Features

- 🔍 Multi-run log parsing with overlapping process support  
- 🧠 GenAI-powered summarization and Q&A  
- 🧵 UserID threading and anomaly grouping  
- 📊 Duration extraction and summary analytics  
- 🖼️ Streamlit GUI for file upload and prompt-based interaction  
- 🧱 Modular design for reproducibility across devices

## 📦 Installation

git clone https://github.com/your-username/genai-log-analyzer.git
cd genai-log-analyzer
pip install -r requirements.txt


> 💡 Requires Python 3.9+ and an OpenAI API key.

## 🛠️ Usage

### CLI Mode


python log_analyzer.py --input logs/app.log --query "Summarize errors by user"


### GUI Mode


streamlit run gui.py

- Upload your log file  
- Enter a natural-language prompt (e.g. “What anomalies occurred yesterday?”)  
- View structured summaries and extracted durations

## 🧪 Example Prompts

- “Summarize login failures by user”  
- “Group overlapping processes and show durations”  
- “Highlight anomalies and their timestamps”  
- “Explain what happened between 10:00 and 10:30”

## 🧩 Modular Components

| Module         | Description                              |
|----------------|------------------------------------------|
| `parser.py`    | Multi-pattern log parsing and extraction |
| `agent.py`     | GenAI integration for summarization      |
| `gui.py`       | Streamlit interface                      |
| `utils.py`     | Duration, threading, and anomaly logic   |

## 📁 Sample Logs

Sample logs for testing are available in the `logs/` directory.

## 🧠 GenAI Setup

Set your OpenAI API key as an environment variable:

export OPENAI_API_KEY=your-key-here


## 🧼 To-Do

- [ ] Add export options (JSON/CSV)  
- [ ] Integrate GitHub Actions for CI  
- [ ] Enhance anomaly clustering logic  
- [ ] Add unit tests for parser and agent

## 📜 License

MIT License

---

Built with ❤️ by dimazps and Copilot.
```

