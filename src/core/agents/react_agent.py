from .rag.hybrid_retriever import HybridRetriever

class ReActAgent:
    """
    Task-oriented agent implementing Reason + Act loop.
    """
    def __init__(self, retriever: HybridRetriever):
        self.retriever = retriever

    def execute(self, query: str) -> str:
        # Step 1: Reason
        # Step 2: Act (e.g., call retriever)
        context = self.retriever.retrieve(query)
        # Step 3: Observe & Synthesize
        return f"Synthesized response based on context: {context}"
