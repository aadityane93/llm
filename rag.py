from langchain_community.document_loaders import DirectoryLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter

data_path = "data"

def load_documents():
    loader = DirectoryLoader(data_path, glob="*.md")
    documents = loader.load()
    return documents

# def split_text(documents: list[Document]):
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size = 1000,
#         chunck_overlap = 500,
#         length_function=len,
#         add_start_index=True,
#     )

    # chunks = text_splitter.split_documents(documents)
    # print (f"Split {len(documents)} documents into {len(chunks)}")
    # document = chunks[10]
    # print(document.page_content)
    # print(document.metadata)
    # return chunks

documents = load_documents()

print (documents)