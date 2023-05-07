

from lang_chain.vectorstores import FAISS
from lang_chain.document_loaders import TextLoader
loader = TextLoader('./state_of_the_union.txt')
documents = loader.load()

from lang_chain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

