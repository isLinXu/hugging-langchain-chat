# Document Loader
def get_url_file(url="", file_name="../data/files.txt"):
    '''
    get_url_file
    :param url:
    :param file_name:
    :return:
    '''
    import requests
    res = requests.get(url)
    with open(file_name, "w") as f:
        f.write(res.text)
    return f


def text_loader(file_path):
    '''
    text_loader
    :param file_path:
    :return:
    '''
    from langchain.document_loaders import TextLoader
    loader = TextLoader(file_path)
    documents = loader.load()
    return documents


if __name__ == '__main__':
    url = "https://raw.githubusercontent.com/hwchase17/langchain/master/docs/modules/state_of_the_union.txt"
    file_res = get_url_file(url)
    # print("file_res:", file_res)

    file_path = '../data/files.txt'
    docs = text_loader(file_path)
    print("docs:", docs)
