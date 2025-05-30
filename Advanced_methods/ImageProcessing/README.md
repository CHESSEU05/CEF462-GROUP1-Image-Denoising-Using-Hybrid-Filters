# NLM Denoising Project
This project cleans noisy images using Non-Local Means (NLM).

## How to Run
1. Create a virtual environment: `python -m venv nlm_env`
2. Activate it: `nlm_env\Scripts\activate` (Windows) or `source nlm_env/bin/activate` (Mac/Linux)
3. Install libraries: `pip install -r requirements.txt`
4. Put noisy images in `Images/`
5. Run the script: `python scripts/nlm_denoising.py`
6. Check results in `NLM_denosing_approach/`

## Contents
- Noisy images: `NLM_denosing_approach/input_images/`
- Cleaned images: `NLM_denosing_approach/output_images/`
- Script: `scripts/nlm_denoising.py`
- Report: `NLM_denosing_approach/NLM_analysis_report.txt`