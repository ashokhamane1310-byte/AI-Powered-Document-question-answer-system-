# AI-Powered Document QA System

![Demo Screenshot](./demo/screenshot.png)

A local AI system that answers questions from uploaded documents (PDF, Word, TXT, images) using Mistral 7B LLM - 100% private, no API calls needed.

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Ollama (for Mistral 7B)
- Tesseract OCR (for image support)

**Install prerequisites:**
```bash
# Linux (Ubuntu/Debian)
sudo apt install python3.10 tesseract-ocr poppler-utils

# macOS
brew install python tesseract poppler

# Windows (WSL2 recommended)
winget install Python.TesseractOCR.Poppler


#Installation
#Clone the repository:

git clone https://github.com/yourusername/AI-Powered-Document-question-answer-system-.git
cd AI-Powered-Document-question-answer-system-

#Install Python dependencies:

pip install -r requirements.txt

#Download Mistral 7B model:

ollama pull mistral


#Launch the application & run the project 

streamlit run app.py


# upload the document and start asking questions about document. model is acapable of understanding document and answering question to the expert level 


#📂 Project Structure
text
.
├── app.py                  # Main application
├── document_processor.py   # File processing logic
├── text_processor.py       # Text chunking/vector DB
├── qa_system.py           # Mistral 7B integration
├── requirements.txt        # Dependencies
└── chroma_db/             # Vector database storage
└── readme.md/             # user guide 






