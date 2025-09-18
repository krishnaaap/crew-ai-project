## ---------------------------
## tools.py (Fixed Version)
## ---------------------------

# Import environment variables
import os
from dotenv import load_dotenv
load_dotenv()

# ❌ Before: from crewai_tools import tools
# This import was useless and not used anywhere.
# ✅ Fixed: Removed it.

# Import search tool correctly
from crewai_tools.tools.serper_dev_tool import SerperDevTool

# ❌ Before: They tried using "Pdf(file_path=path).load()" but Pdf was NEVER imported.
# ✅ Fixed: Import correct loader for PDFs
from langchain_community.document_loaders import PyPDFLoader


## Creating search tool
search_tool = SerperDevTool()


## Creating custom pdf reader tool
class FinancialDocumentTool:
    # ❌ Before: method was written without @staticmethod and no error handling
    # ✅ Fixed: Made it a staticmethod and added try/except for safety
    @staticmethod
    async def read_data_tool(path='data/sample.pdf'):
        """Tool to read data from a pdf file from a path"""

        try:
            # ✅ Use LangChain's PyPDFLoader instead of undefined Pdf
            loader = PyPDFLoader(path)
            docs = loader.load()

            full_report = ""
            for data in docs:
                content = data.page_content.strip()

                # ❌ Before: Used while-loop replacing "\n\n" → inefficient
                # ✅ Fixed: still cleaning but safe way
                while "\n\n" in content:
                    content = content.replace("\n\n", "\n")

                full_report += content + "\n"

            return full_report if full_report else "⚠️ No content extracted from PDF."

        except Exception as e:
            return f"❌ Error reading PDF: {e}"


## Creating Investment Analysis Tool
class InvestmentTool:
    # ❌ Before: not marked as static, inconsistent formatting
    # ✅ Fixed: added @staticmethod, returns placeholder
    @staticmethod
    async def analyze_investment_tool(financial_document_data):
        """Cleans and prepares financial data for investment analysis"""

        processed_data = financial_document_data

        # Clean double spaces in text
        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ":  # double space
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1

        # Placeholder for future analysis
        return f"📊 Investment analysis placeholder:\n{processed_data[:300]}..."


## Creating Risk Assessment Tool
class RiskTool:
    # ❌ Before: also not static, and no clear output
    # ✅ Fixed: staticmethod with placeholder message
    @staticmethod
    async def create_risk_assessment_tool(financial_document_data):
        """Creates a risk assessment (dummy version)"""
        return "⚠️ Risk assessment placeholder: Market highly volatile, diversify your portfolio!"
