from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain_community.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

class QASystem:
    def __init__(self):
        # Initialize local Mistral model
        self.llm = Ollama(
            model="mistral",
            callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
            temperature=0,
            top_k=10,
            stop=["<|endoftext|>", "</s>"]
        )
        
        self.prompt = ChatPromptTemplate.from_template(
            """[INST] Answer the question based only on the following context.
            If you don't know the answer, say "I don't know".
            
            Context: {context}
            
            Question: {question} 
            
            Answer concisely and accurately. [/INST]"""
        )

    def get_answer(self, question: str, context: str) -> str:
        """Generate answer to question based on provided context"""
        chain = (
            {"context": RunnablePassthrough(), "question": RunnablePassthrough()}
            | self.prompt
            | self.llm
        )
        return chain.invoke({"context": context, "question": question})