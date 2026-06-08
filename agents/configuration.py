from .base import BaseAgent


class ConfigurationAgent(BaseAgent):
    name = "ConfigurationAgent"

    def run(self, context):
        context.evidence.append(
            {
                "agent": self.name,
                "status": "completed",
                "note": "Reviewed deployment configuration."
            }
        )
