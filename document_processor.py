import os
from typing import List, Union
from PyPDF2 import PdfReader
from docx import Document
import pytesseract
from PIL import Image
from unstructured.partition.auto import partition

class DocumentProcessor:
    @staticmethod
    def extract_text_from_pdf(pdf_path: str) -> str:
        """Improved PDF extraction with unstructured"""
        elements = partition(pdf_path)
        return "\n".join([str(el) for el in elements])
    
    @staticmethod
    def extract_text_from_docx(docx_path: str) -> str:
        """Extract text from Word document"""
        doc = Document(docx_path)
        return "\n".join([para.text for para in doc.paragraphs])

    @staticmethod
    def extract_text_from_image(image_path: str) -> str:
        """Extract text from image using OCR"""
        return pytesseract.image_to_string(Image.open(image_path))

    @staticmethod
    def process_document(file_path: str) -> str:
        """Process document based on file type"""
        #ext = os.path.splitext(file_path)[1].lower()
        #if ext == '.pdf':
        return DocumentProcessor.extract_text_from_pdf(file_path)
        # elif ext == '.docx':
        #     return DocumentProcessor.extract_text_from_docx(file_path)
        # elif ext in ('.png', '.jpg', '.jpeg'):
        #     return DocumentProcessor.extract_text_from_image(file_path)
        # elif ext == '.txt':
        #     with open(file_path, 'r', encoding='utf-8') as file:
        #         return file.read()
        # else:
        #     raise ValueError(f"Unsupported file type: {ext}")