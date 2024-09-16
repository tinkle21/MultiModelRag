from langchain_community.document_loaders import PubMedLoader

loader = PubMedLoader("liver", load_max_docs=10)
documents = loader.load()
print(documents)