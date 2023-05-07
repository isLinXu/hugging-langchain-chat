import textwrap

from lang_chain.utils.textloader import text_loader


def wrap_text_preserve_newlines(text, width=110):
    '''
    wrap_text_preserve_newlines
    :param text:
    :param width:
    :return:
    '''
    # Split the input text into lines based on newline characters
    lines = text.split('\n')

    # Wrap each line individually
    wrapped_lines = [textwrap.fill(line, width=width) for line in lines]

    # Join the wrapped lines back together using newline characters
    wrapped_text = '\n'.join(wrapped_lines)

    return wrapped_text


def split_text_documents(documents):
    '''
    split_text_documents Text Splitter
    :param documents:
    :return:
    '''
    from langchain.text_splitter import CharacterTextSplitter
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    return docs


if __name__ == '__main__':
    file_path = '../data/files.txt'
    documents = text_loader(file_path)
    print(wrap_text_preserve_newlines(str(documents[0])))

