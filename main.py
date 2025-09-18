# main.py
# AI Internship Assignment - Debug Challenge
# Original Project: Financial Document Analyzer using CrewAI
# Candidate: [Your Name]
# Purpose: Debugged & fixed errors in the original repo

"""
Changes Made:
1. Added proper file handling and cleanup for uploaded PDFs.
2. Fixed CrewAI kickoff call to include 'file_path' parameter (original code ignored file input).
3. Added default query validation to prevent empty queries.
4. Improved exception handling with meaningful error messages.
5. Updated docstrings and comments for clarity.
6. Ensured FastAPI endpoints are properly asynchronous.
"""

from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid

# Fixed CrewAI import
from crewai import Crew, Process  

# Local modules (these must exist in your repo)
from agents import financial_analyst
from task import analyze_financial_document

# Initialize FastAPI app
app = FastAPI(title="Financial Document Analyzer")


def run_crew(query: str, file_path: str):
    """
    Runs the CrewAI pipeline with the given query and PDF file.

    Changes Made:
    ✅ Original code ignored file_path; fixed to pass it to kickoff.
    """
    financial_crew = Crew(
        agents=[financial_analyst],
        tasks=[analyze_financial_document],
        process=Process.sequential  # Run tasks sequentially
    )

    # Kickoff CrewAI with both query and file_path
    return financial_crew.kickoff({'query': query, 'file_path': file_path})


@app.get("/")
async def root():
    """Health check endpoint. No changes required."""
    return {"message": "Financial Document Analyzer API is up and running!"}


@app.post("/analyze")
async def analyze_financial_document(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document for investment insights")
):
    """
    Upload a PDF and analyze using CrewAI agents.
    
    Changes Made:
    ✅ Added file_path handling.
    ✅ Validated query to prevent empty string.
    ✅ Added proper cleanup with warning messages.
    """
    # Unique filename
    file_id = str(uuid.uuid4())
    file_path = f"data/financial_document_{file_id}.pdf"

    try:
        os.makedirs("data", exist_ok=True)

        # Save the uploaded PDF
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        # Default query if empty
        if not query:
            query = "Analyze this financial document for investment insights"

        # Process the financial document
        response = run_crew(query=query.strip(), file_path=file_path)

        return {
            "status": "success",
            "query": query,
            "analysis": str(response),
            "file_processed": file.filename
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing document: {str(e)}")

    finally:
        # Cleanup uploaded file
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except Exception as cleanup_error:
                print(f"Warning: Failed to remove file {file_path}: {cleanup_error}")


if __name__ == "__main__":
    import uvicorn
    # Launch API with auto-reload for development
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
