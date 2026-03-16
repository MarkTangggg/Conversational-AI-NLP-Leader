import logging
from typing import Dict, Any
from .agents.react_agent import ReActAgent
from .rag.hybrid_retriever import HybridRetriever

class AIOrchestrator:
    """
    Enterprise-grade AI Orchestrator managing the interaction between
    Agents, RAG systems, and ML tools.
    """
    def __init__(self, config: Dict[str, Any] = None):
        self.logger = logging.getLogger(__name__)
        self.retriever = HybridRetriever()
        self.agent = ReActAgent(retriever=self.retriever)
        self.logger.info("AI Orchestrator initialized.")

    def process_query(self, query: str) -> str:
        self.logger.info(f"Processing query: {query}")
        # Core logic for delegating task to agent
        response = self.agent.execute(query)
        return response
