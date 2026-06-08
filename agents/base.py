from dataclasses import dataclass, field


@dataclass
class AssessmentContext:
    target: str
    evidence: list = field(default_factory=list)


class BaseAgent:
    name = "BaseAgent"

    def run(self, context: AssessmentContext):
        raise NotImplementedError
