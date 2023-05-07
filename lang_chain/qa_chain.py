import config
from langchain.chains.question_answering import load_qa_chain
from langchain import HuggingFaceHub

from doc_langchain import create_db
from lang_chain.utils.text_utils import split_text_documents
from lang_chain.utils.textloader import text_loader

llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature": 0.5, "max_length": 512})

chain = load_qa_chain(llm, chain_type="stuff")

query = "What did the president say about the Supreme Court"

file_path = './data/files.txt'
document = text_loader(file_path)

# Text Splitter
docs = split_text_documents(document)
db = create_db(docs)
docs = db.similarity_search(query)
chain.run(input_documents=docs, question=query)
