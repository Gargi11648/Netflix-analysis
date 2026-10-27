# Netflix Movies and TV Shows Analysis - Web App
Python web app using **Pandas** (data) and **Matplotlib** (charts), served with **Streamlit**.

## Run
```
pip install -r requirements.txt
streamlit run app.py
```
Opens at http://localhost:8501

## Files
- `app.py` - web app (filters, tabs, search)
- `netflix_core.py` - data cleaning, chart functions, insights
- `generate_sample_data.py` - builds the sample CSV
- `data/netflix_titles.csv` - built-in SAMPLE of 64 real titles (the `date_added` column is simulated)

## Use the real dataset
Download `netflix_titles.csv` from Kaggle ("Netflix Movies and TV Shows") and either upload it
in the app sidebar or replace `data/netflix_titles.csv`. No code changes needed.
