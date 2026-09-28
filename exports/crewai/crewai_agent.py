from crewai import Agent
def create_agent():
    return Agent(role='GitAPISentry', goal='Autonomous OpenAPI Spec Drift, Breaking Change & Semantic Versioning Auditor Agent', backstory='Autonomous agent', verbose=True)
