from .base import BaseAgent


class ReportAgent(BaseAgent):
    name = "ReportAgent"

    def run(self, context):
        context.evidence.append(
            {
                "agent": self.name,
                "status": "completed",
                "note": "Generated executive summary."
            }
        )
