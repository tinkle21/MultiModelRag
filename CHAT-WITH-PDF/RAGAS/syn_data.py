from langchain_community.document_loaders import DirectoryLoader
loader = DirectoryLoader("CHAT-WITH-PDF/data")
documents = loader.load()