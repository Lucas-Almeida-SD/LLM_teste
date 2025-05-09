from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="./src/assets/vendas.csv")
documents = loader.load()