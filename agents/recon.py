from .base import BaseAgent


class ReconAgent(BaseAgent):
    name = "ReconAgent"

    def run(self, context):
        context.evidence.append(
            {
                "agent": self.name,
                "status": "completed",
                "note": "Documented exposed application surface."
            }
        )
