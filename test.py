import streamlit as st
from document_processor import DocumentProcessor
from text_processor import TextProcessor
from qa_system import QASystem
import os
import tempfile
import time
import sys

def main():
    try:
        st.title("📄 Free Local Document QA System")
        st.write("Debug: Passed title")  # Should appear immediately
        
        document_processor = DocumentProcessor()
        st.write("Debug: Created document processor")
        
        # ... rest of your existing code ...
        
    except Exception as e:
        st.error(f"CRITICAL ERROR: {str(e)}")
        print(f"Error in main(): {e}", file=sys.stderr)

if __name__ == "__main__":
    main()