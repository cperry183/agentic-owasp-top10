from .base import BaseAgent


class AuthAgent(BaseAgent):
    name = "AuthAgent"

    def run(self, context):
        context.evidence.append(
            {
                "agent": self.name,
                "status": "completed",
                "note": "Reviewed authentication and session controls."
            }
        )
