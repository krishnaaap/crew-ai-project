Financial Document Analyzer

A FastAPI application that analyzes financial PDFs and provides structured investment insights using CrewAI.

Changes & Fixes:

Renamed endpoint to avoid overwriting imported task.

Uploaded file path is now passed to CrewAI tasks.

Made run_crew asynchronous to avoid blocking FastAPI.

Optimized prompt for clear JSON output (revenue, expenses, profit, recommendations).

Added safe file cleanup after processing.

Default query handling improved for empty inputs.

Setup:

pip install -r requirements.txt

uvicorn app:app --reload

Usage:

GET / → Health check

POST /analyze → Upload PDF + optional query, returns analysis
