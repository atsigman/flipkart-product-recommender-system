import pandas as pd

from typing import List

from langchain_core.documents import Document


class DataConverter:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def convert(self) -> List[Document]:
        df = pd.read_csv(self.file_path)[["product_title", "review"]]

        docs = [
            Document(page_content=row["review"],
                     metadata={"product_title": row["product_title"]}
            )
            for _, row in df.iterrows()
        ]

        return docs
