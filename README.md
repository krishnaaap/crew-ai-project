Financial Document Analyzer

A FastAPI application that analyzes financial PDFs and provides structured investment insights using CrewAI.

Changes & Fixes:

Renamed endpoint to avoid overwriting imported task.

Uploaded file path is now passed to CrewAI tasks.

Made run_crew asynchronous to avoid blocking FastAPI.
task.py – Issues & Changes:

Prompts were hallucination-heavy, producing fake URLs, numbers, and contradictory advice.

verification task didn’t actually check if a document was financial.

All tasks ran synchronously (async_execution=False), slowing concurrent requests.

Fixed analyze_financial_document to pass uploaded file path to CrewAI.

Optimized prompts to extract real financial metrics (revenue, expenses, profit, recommendations).

Made all tasks async (async_execution=True) for better concurrency.

Structured expected_output in JSON for easier parsing and consistency.

agents.py – Issues & Changes:

llm was a placeholder, not properly initialized with a real LLM backend.

financial_analyst agent hallucinated data and didn’t focus on actual document content.

verifier agent guessed file type instead of checking for real financial keywords.

Adjusted agents to use realistic, structured prompts aligned with task.py.

Enabled proper delegation, memory, and concurrency settings to match task execution.
tools.py – Issues & Changes:

FinancialDocumentTool.read_data_tool existed but didn’t reliably extract structured data from PDFs.

No clear separation between tools for searching online vs reading financial documents.

Search tool (search_tool) was loosely defined and not integrated properly with tasks.

Fixed read_data_tool to consistently read PDFs and return text in a usable format for CrewAI.

Ensured tools are correctly passed to agents and tasks for structured, real analysis instead of hallucinations.

Setup:

pip install -r requirements.txt

uvicorn app:app --reload

Usage:

GET / → Health check

POST /analyze → Upload PDF + optional query, returns analysis
