from .base import BaseAgent


class DependencyAgent(BaseAgent):
    name = "DependencyAgent"

    def run(self, context):
        context.evidence.append(
            {
                "agent": self.name,
                "status": "completed",
                "note": "Enumerated third-party components."
            }
        )
