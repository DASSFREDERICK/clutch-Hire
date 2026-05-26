# 🚀 ClutchHire AI — Intelligent Recruiter DeepSystem

ClutchHire AI is an enterprise-grade, multi-agent automated recruitment screening engine. Built on top of a lightning-fast asynchronous backend and an intuitive frontend dashboard interface, the platform cross-evaluates candidate resumes against job descriptions using advanced LLM reasoning capabilities to eliminate manual talent assessment bottlenecks.

---

## 🧠 Advanced Multi-Agent Architecture

The core pipeline operates as a sequential matrix processing loop powered by **DeepSeek-V3** via the Chutes network to provide realistic, deeply analytical evaluation tracks:

1. **Agent 1: The HR Parser** ⚡  
   Ingests raw text boundaries from job descriptions and candidate file streams (supporting native text and multi-page PDFs via PyMuPDF). It sanitizes formatting and isolates core parameters like technical stacks, years of experience, and primary responsibilities.
2. **Agent 2: Deep Matrix Scorer** 📊  
   Cross-references parsed profiles against requirements across 5 strict weighted categories: Technical Skills (30%), Experience Level (25%), Domain Match (20%), Responsibilities Alignment (15%), and Education (10%). It computes an exact matching score out of 100 and maps relevant technology tags.
3. **Agent 3: Executive Explainer** 💎  
   Generates professional, objective, human-grade recruitment narrative summaries. It highlights the candidate's absolute strongest engineering asset alongside any key structural stack optimization gaps.

---

## 🛠️ Technology Stack

* **Backend Framework:** FastAPI (Python)
* **Interactive UI:** Streamlit
* **AI Core Engine:** DeepSeek-V3-TEE / DeepSeek-V3 (Orchestrated via Chutes OpenAI Client)
* **Data Validations:** Pydantic v2
* **PDF Extraction Engine:** PyMuPDF (`fitz`)

---

## 📦 Project Directory Layout

```text
clutch-Hire/
├── resume/               # Target directory for candidate document streams
│   └── Candidate Name Aris Lim.txt
├── app.py                # Streamlit Frontend User Interface
├── main.py               # FastAPI Multi-Agent Core Gateway Router
├── .env                  # Local Environment Credentials (Hidden/Protected)
└── .gitignore            # Git exclusion mapping (Ignores venv/ and __pycache__/)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

🚀 Step-by-Step Installation & Execution Guide
Follow these exact steps to clone, configure, and execute the entire ClutchHire platform locally on your machine.

Step 1: Clone the Repository
Open a terminal window and download the project code:

Bash
git clone [https://github.com/DASSFREDERICK/clutch-hire.git](https://github.com/DASSFREDERICK/clutch-hire.git)
cd clutch-hire
Step 2: Configure a Virtual Environment
Create an isolated development environment sandbox to prevent system-wide package version conflicts:

Bash
python -m venv venv
Activate the environment sandbox based on your terminal terminal shell:

Windows Command Prompt:

DOS
venv\Scripts\activate
Windows PowerShell:

PowerShell
.\venv\Scripts\Activate.ps1
Linux/macOS Terminal:

Bash
source venv/bin/activate
Step 3: Install Required Dependencies
With your virtual environment active, run the package installer to download the necessary module dependencies:

Bash
python -m pip install --upgrade pip
pip install fastapi uvicorn openai python-dotenv pydantic python-multipart pymupdf streamlit
Step 4: Add Your Security Environment Credentials
To protect sensitive credentials, ClutchHire reads parameters out of a local system variable cache.

Create a file named .env inside the root folder using your text editor and add your active cloud authentication token:

Code snippet
CHUTES_API_KEY=your_actual_chutes_api_key_here
(Note: Never commit your .env file containing this raw string to a public repository!)

Step 5: Launch the Application Cluster
To see the system running live, open two separate terminal window panels (making sure both have the venv environment activated) and execute the following commands:

Terminal 1 (Backend REST API Gateway Engine):

Bash
python main.py
Your FastAPI gateway router will boot up locally at http://localhost:8000.

Terminal 2 (Frontend Interface Portal Client):

Bash
python -m streamlit run app.py
Your Streamlit application client page interface will initialize automatically at http://localhost:8501.

💡 Usage Framework
Open your browser and navigate to the Streamlit portal: http://localhost:8501.

Input or paste your target job requirements schema directly into the designated Job Description text box block.

Drag, drop, or select multiple candidate resume files (.txt or .pdf layout formats).

Hit the ⚡ EXECUTE MATCH PIPELINE tracking button to dispatch the sequential processing pipeline and watch the logs process live on your FastAPI terminal!


***

Once you commit this file, your repository home screen dashboard page will present a clean, beautifully organized layout that w
