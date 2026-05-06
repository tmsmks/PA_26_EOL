"""Service d'enrichissement IA : génère de nouvelles réponses plausibles via LLM."""
from services.enrichment.service import EnrichmentService, EnrichRequest, Proposal

__all__ = ["EnrichmentService", "EnrichRequest", "Proposal"]
