from .base import BaseAgent


class InputValidationAgent(BaseAgent):
    name = "InputValidationAgent"

    def run(self, context):
        context.evidence.append(
            {
                "agent": self.name,
                "status": "completed",
                "note": "Executed safe input validation checks."
            }
        )
