"""
Class for loading and converting data,
and embedding extraction/storage.
"""

from langchain_astradb import AstraDBVectorStore
from langchain_huggingface import HuggingFaceEndpointEmbeddings

from flipkart.config import Config
from flipkart.data_converter import DataConverter


class DataIngestor:
    def __init__(self) -> None:
        self.embedding = HuggingFaceEndpointEmbeddings(model=Config.EMBEDDING_MODEL)
        self.vectorstore = AstraDBVectorStore(
            collection_name="flipkart_database",
            embedding=self.embedding,
            api_endpoint=Config.ASTRA_DB_API_ENDPOINT,
            token=Config.ASTRA_DB_APPLICATION_TOKEN,
            namespace=Config.ASTRA_DB_KEYSPACE,
        )

    def ingest(
        self,
        csv_filepath: str = "data/flipkart_product_review.csv",
        load_existing: bool = True,
    ) -> AstraDBVectorStore:
        """
        Converts CSV data to Documents, embed, and save to AstraDB vectorstore.
        Returns the populated vectorstore.
        """
        if load_existing:
            return self.vectorstore

        # Convert CSV rows into Documents:
        docs = DataConverter(csv_filepath).convert()

        # Convert Documents to embeddings and store to Vectorstore:
        self.vectorstore.add_documents(docs)

        return self.vectorstore


# if __name__ == "__main__":
#     data_ingestor = DataIngestor()
#     data_ingestor.ingest(load_existing=False)
