## Importing libraries and files
from crewai import Task

from agents import financial_analyst, verifier, investment_advisor, risk_assessor
from tools import FinancialDocumentTool

# -----------------------------
# Task: Analyze Financial Document
# -----------------------------
analyze_financial_document = Task(
    description=(
        "Analyze the uploaded financial document carefully and answer the user's query: {query}. "
        "Focus on extracting meaningful insights from the data such as revenue, expenses, ratios, "
        "growth trends, and investment opportunities."
    ),
    expected_output=(
        "A clear and structured financial analysis including:\n"
        "- Key highlights from the report (revenue, profit, expenses, debt)\n"
        "- Important financial ratios and their interpretation\n"
        "- Growth or decline patterns\n"
        "- Summary of insights relevant to the user's query"
    ),
    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

# -----------------------------
# Task: Investment Analysis
# -----------------------------
investment_analysis = Task(
    description=(
        "Based on the financial document, evaluate investment opportunities. "
        "Consider profitability, growth, industry outlook, and risks before making recommendations."
    ),
    expected_output=(
        "Detailed investment recommendations including:\n"
        "- Buy/Hold/Sell recommendations with reasoning\n"
        "- At least 3–5 investment opportunities supported by data\n"
        "- Potential red flags or risks to consider\n"
        "- Clear actionable insights for investors"
    ),
    agent=investment_advisor,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

# -----------------------------
# Task: Risk Assessment
# -----------------------------
risk_assessment = Task(
    description=(
        "Evaluate risks associated with the financial document. "
        "Highlight potential financial, operational, market, or regulatory risks that may impact decisions."
    ),
    expected_output=(
        "Structured risk assessment including:\n"
        "- Financial risks (debt, liquidity, revenue concentration)\n"
        "- Market risks (competition, economic changes)\n"
        "- Operational risks (management, supply chain)\n"
        "- Regulatory/compliance risks\n"
        "- Risk mitigation strategies"
    ),
    agent=risk_assessor,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

# -----------------------------
# Task: Verification
# -----------------------------
verification = Task(
    description=(
        "Verify whether the uploaded file is a valid financial document (e.g., balance sheet, income statement, "
        "annual report). If not, clearly mention it."
    ),
    expected_output=(
        "Verification result:\n"
        "- Confirm whether the document is a financial report or not\n"
        "- Provide reasoning (e.g., it contains financial terms, ratios, tables)\n"
        "- Mention the document type if possible"
    ),
    agent=verifier,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)
