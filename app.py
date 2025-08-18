import streamlit as st
from document_processor import DocumentProcessor
from text_processor import TextProcessor
from qa_system import QASystem
import os
import tempfile
import time

# Initialize components
document_processor = DocumentProcessor()
text_processor = TextProcessor()
qa_system = QASystem()

# Streamlit UI
st.title("📄 Free Local Document QA System")
st.write("Upload a document and ask questions - 100% local processing")

# Document upload
uploaded_file = st.file_uploader(
    "Choose a document (PDF, Word, TXT, or image)",
    type=["pdf", "docx", "txt", "png", "jpg", "jpeg"],
    key="file_uploader"
)
# Initialize with session state
if 'text_processor' not in st.session_state:
    st.session_state.text_processor = TextProcessor()
# # Process document when uploaded
# if uploaded_file is not None and not st.session_state.get('file_processed', False):
#     with st.spinner("Processing document..."):
#         with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
#             tmp_file.write(uploaded_file.getvalue())
#             tmp_file_path = tmp_file.name
        
#         try:
#             # Process document
#             text = document_processor.process_document(tmp_file_path)
#             chunks = text_processor.chunk_text(text)
#             text_processor.create_vector_store(chunks)
            
#             st.session_state['file_processed'] = True
#             st.session_state['file_name'] = uploaded_file.name
#             st.success(f"✅ Document processed successfully! ({len(chunks)} chunks)")
#         except Exception as e:
#             st.error(f"Error processing document: {str(e)}")
#         finally:
#             os.unlink(tmp_file_path)
# Document processing
if uploaded_file and not st.session_state.get('file_processed'):
    with st.spinner("Processing..."):
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_path = tmp_file.name
        
        try:
            text = document_processor.process_document(tmp_path)
            chunks = st.session_state.text_processor.chunk_text(text)
            
            if st.session_state.text_processor.create_vector_store(chunks):
                st.session_state.file_processed = True
                st.success("Ready for questions!")
            else:
                st.error("Failed to process document")
        finally:
            os.unlink(tmp_path)

# # Question input and answer display
# if st.session_state.get('file_processed', False):
#     st.subheader(f"Ask about: {st.session_state['file_name']}")
#     question = st.text_input("Your question:", key="question_input")
    
#     if question:
#         start_time = time.time()
#         with st.spinner("🧠 Thinking..."):
#             try:
#                 # Get relevant context
#                 context = text_processor.search_documents(question)
                
#                 # Generate answer
#                 answer = qa_system.get_answer(question, "\n\n".join(context))
                
#                 # Display results
#                 st.subheader("Answer")
#                 st.write(answer)
                
#                 # Show performance metrics
#                 st.caption(f"Response time: {time.time()-start_time:.2f}s")
                
#                 # Show context snippets
#                 with st.expander("🔍 See relevant context"):
#                     for i, snippet in enumerate(context, 1):
#                         st.write(f"**Snippet {i}:**")
#                         st.write(snippet)
#                         st.write("---")
#             except Exception as e:
#                 st.error(f"Error generating answer: {str(e)}")

# Question answering
if st.session_state.get('file_processed'):
    question = st.text_input("Ask about the document:")
    if question:
        with st.spinner("Thinking..."):
            try:
                context = st.session_state.text_processor.search_documents(question)
                answer = qa_system.get_answer(question, "\n\n".join(context))
                st.write(answer)
            except Exception as e:
                st.error(f"Error: {str(e)}")
# Reset button
if st.session_state.get('file_processed', False):
    if st.button("Reset and upload new document"):
        st.session_state.clear()
        st.rerun()