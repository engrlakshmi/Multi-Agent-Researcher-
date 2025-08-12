# Multi-Agent-Researcher
# 🔍 Streamlit Research Summarizer (DuckDuckGo + Ollama)

A **Streamlit-based research tool** that:
1. Searches the web using **DuckDuckGo** (via LangChain tools)
2. Cleans up the query
3. Uses an **Ollama LLM** to refine and summarize the results in real time

---

## 📌 Features
- **Live Search**: Uses DuckDuckGo to get the latest information
- **Query Cleaning**: Removes unnecessary spaces for better search accuracy
- **Single LLM Call**: Combines refinement and summarization in one pass
- **Streaming Output**: Displays AI-generated summaries as they are produced
- **Caching**: Avoids repeated searches for the same query

---

## 🛠 Requirements
- **Python 3.9+**
- **Ollama** installed locally (for the `qwen3:8b` model) → [Ollama Installation Guide](https://ollama.com/download)
- **Docker** (if running in a container)

---

## 📂 Project Structure
.
├── app.py # Streamlit app
├── Dockerfile # Docker setup
└── requirements.txt # Python dependencies

## 📦 Installation (Local)

1️⃣ Clone the repo:
git clone https://github.com/yourusername/research-summarizer.git
cd research-summarizer
2️⃣ Install dependencies:
pip install -r requirements.txt
3️⃣ Start Ollama locally:
ollama serve
ollama pull qwen3:8b
4️⃣ Run the app:
streamlit run app.py
🐳 Running with Docker
1️⃣ Build the Docker image:
docker build -t research-summarizer .
2️⃣ Run the container:
docker run -p 8501:8501 research-summarizer
3️⃣ Access in browser:
http://localhost:8501
Note: The container must be able to connect to your local Ollama server, so you may need to expose its API port (11434).

📜 Example Usage
Enter:
Latest AI news August 2025
The app:
1. Cleans the query
2. Searches DuckDuckGo
3. Summarizes results using qwen3:8b
4. Displays a 200-word concise summary
