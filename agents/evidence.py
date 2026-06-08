from .base import BaseAgent


class EvidenceAgent(BaseAgent):
    name = "EvidenceAgent"

    def run(self, context):
        context.evidence.append(
            {
                "agent": self.name,
                "status": "completed",
                "note": "Consolidated assessment evidence."
            }
        )
