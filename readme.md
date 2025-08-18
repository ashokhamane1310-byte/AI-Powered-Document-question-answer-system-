# 📄 Document QA System (Single-File Version)

**Process documents & get answers 100% locally** using Mistral 7B - no API calls needed!

## 🚀 Quick Start

### 1. Install Requirements
```bash
# On Ubuntu/Debian
sudo apt install python3.10 tesseract-ocr poppler-utils
pip install streamlit PyPDF2 python-docx pytesseract pillow ollama langchain chromadb sentence-transformers

# On macOS
brew install python tesseract poppler
pip install -r requirements.txt

# Download Mistral 7B
ollama pull mistral

# run the system 

ollama serve &          # Run in background
streamlit run app.py    # Main application

🧩 File Structure (Single-File Version)

app.py
├── DocumentProcessor  - Handles PDF/DOCX/TXT/Images
├── TextProcessor      - Chunking & vector database
├── QASystem          - Mistral 7B answer generation
└── Main UI           - Streamlit interface