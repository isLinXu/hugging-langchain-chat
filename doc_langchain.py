from lang_chain.embeddings import embeddings
from lang_chain.utils.text_utils import wrap_text_preserve_newlines, split_text_documents
from lang_chain.utils.textloader import text_loader

def create_db(docs):
    from langchain.vectorstores import FAISS
    db = FAISS.from_documents(docs, embeddings)
    return db
def docs_search(docs, query):
    # Vectorstore: https://python.langchain.com/en/latest/modules/indexes/vectorstores.html
    # from langchain.vectorstores import FAISS
    #
    # db = FAISS.from_documents(docs, embeddings)
    db = create_db(docs)

    # query = "What did the president say about the Supreme Court"
    docs = db.similarity_search(query)

    print("query:", query)
    print("answer:", wrap_text_preserve_newlines(str(docs[0].page_content)))


if __name__ == '__main__':
    # Text loader
    file_path = './lang_chain/data/files.txt'
    document = text_loader(file_path)

    # Text Splitter
    docs = split_text_documents(document)

    query = "What did the president say about the Supreme Court"

    answer = docs_search(docs, query)
