"""
Minimal orchestration engine for defensive OWASP Top 10 assessments.
"""

from agents.base import AssessmentContext
from agents.recon import ReconAgent
from agents.auth import AuthAgent
from agents.input_validation import InputValidationAgent
from agents.dependencies import DependencyAgent
from agents.configuration import ConfigurationAgent
from agents.evidence import EvidenceAgent
from agents.report import ReportAgent
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True)
    args = parser.parse_args()

    ctx = AssessmentContext(target=args.target)

    pipeline = [
        ReconAgent(),
        AuthAgent(),
        InputValidationAgent(),
        DependencyAgent(),
        ConfigurationAgent(),
        EvidenceAgent(),
        ReportAgent(),
    ]

    for agent in pipeline:
        print(f"[+] Running {agent.name}")
        agent.run(ctx)

    print("\nAssessment complete.")
    print(f"Evidence collected: {len(ctx.evidence)} items")


if __name__ == "__main__":
    main()
