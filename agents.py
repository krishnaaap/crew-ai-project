## Importing libraries and files
import os
from dotenv import load_dotenv
from crewai import LLM
from crewai.agents import Agent

from tools import search_tool, FinancialDocumentTool

# Load environment variables
load_dotenv()

### Loading LLM
llm = LLM(model="gpt-4", api_key=os.getenv("OPENAI_API_KEY"))

# Creating an Experienced Financial Analyst agent
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Accurately analyze financial documents and provide investment insights.",
    verbose=True,
    memory=True,
    backstory=(
        "You are an experienced financial analyst with deep knowledge of markets, "
        "financial ratios, and corporate filings. You provide clear, actionable insights."
    ),
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    max_iter=3,
    max_rpm=5,
    allow_delegation=True
)

# Creating a document verifier agent
verifier = Agent(
    role="Financial Document Verifier",
    goal="Verify whether the uploaded document is a valid financial report.",
    verbose=True,
    memory=True,
    backstory=(
        "You previously worked in financial compliance. You carefully check documents "
        "to ensure they are genuine financial reports."
    ),
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    max_iter=2,
    max_rpm=5,
    allow_delegation=False
)

# Creating an investment advisor agent
investment_advisor = Agent(
    role="Investment Advisor",
    goal="Provide tailored investment recommendations based on financial data.",
    verbose=True,
    backstory=(
        "You are a trusted investment advisor who balances risks and opportunities, "
        "helping clients make informed decisions."
    ),
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    max_iter=3,
    max_rpm=5,
    allow_delegation=False
)

# Creating a risk assessor agent
risk_assessor = Agent(
    role="Risk Assessment Expert",
    goal="Evaluate risks in financial documents and provide clear risk assessments.",
    verbose=True,
    backstory=(
        "You specialize in risk management and regulatory compliance. "
        "You identify key risk factors and suggest mitigations."
    ),
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    max_iter=3,
    max_rpm=5,
    allow_delegation=False
)
