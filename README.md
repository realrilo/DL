# Create and activate virtual environment
# Windows:
- python -m venv .venv
- .venv\Scripts\activate

# Mac/Linux:
- python3 -m venv .venv
- source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# run
uvicorn app.main:app --reload

# cloud host
https://realrilo-exam-dl.hf.space/predict
