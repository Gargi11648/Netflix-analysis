# 🎬 Netflix Movies & TV Shows Analysis Web App

## 📌 Project Overview

The Netflix Movies & TV Shows Analysis Web App is a Python-based interactive dashboard that helps users explore and analyze Netflix movies and TV shows. It uses Streamlit to create an interactive web interface, Pandas for data processing, and Matplotlib for data visualization.

The application allows users to explore content by genre, country, rating, release year, director, actor, and duration through interactive charts, filters, and search functionality.

## ✨ Features

- Interactive dashboard for Netflix movies and TV shows.
- Summary statistics showing total titles, movies, TV shows, and average movie duration.
- Filters for content type, year added, genre, country, and rating.
- Visualizations of movies versus TV shows.
- Analysis of content added by year and month.
- Release-year distribution.
- Top genres and countries.
- Ratings distribution.
- Movie-duration and TV-show-season analysis.
- Search functionality for titles, directors, and actors.
- Detailed information about selected titles.
- Download filtered data in CSV format.
- Upload your own Netflix dataset through the sidebar.
- Automatically generated key insights.

## 🛠️ Technologies Used

- **Python:** Main programming language.
- **Streamlit:** Interactive web application framework.
- **Pandas:** Data cleaning, processing, and analysis.
- **Matplotlib:** Data visualization.
- **CSV:** Dataset storage format.

## 📁 Project Structure

```text
netflix_webapp/
│
├── app.py
├── netflix_core.py
├── generate_sample_data.py
├── requirements.txt
├── README.md
│
└── data/
    └── netflix_titles.csv
```

### File Description

- `app.py` — Main Streamlit application.
- `netflix_core.py` — Contains data processing, visualization, and insight-generation functions.
- `generate_sample_data.py` — Generates sample Netflix dataset records.
- `requirements.txt` — Contains the required Python packages.
- `data/netflix_titles.csv` — Sample dataset used by the application.
- `README.md` — Project documentation.

## ⚙️ Requirements

Before running the project, make sure you have installed:

- Python 3.9 or later.
- pip package manager.
- Visual Studio Code or another Python-compatible editor.

## 🚀 Installation and Setup

### Step 1: Download the Project

Download or clone the project repository and open the project folder in Visual Studio Code.

### Step 2: Create a Virtual Environment

Run the following command in the terminal:

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### Step 3: Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

Execute the following command:

```bash
streamlit run app.py
```

The application should open automatically in your browser.

If it does not open automatically, visit:

```text
http://localhost:8501
```

## 📊 How to Use the Application

1. Start the application using Streamlit.
2. Use the included sample dataset or upload a compatible Netflix CSV file.
3. Apply filters to select content type, genre, country, rating, and year.
4. Explore the dashboard charts and summary statistics.
5. Search for movies and TV shows using titles, directors, or actors.
6. View detailed information about selected titles.
7. Download filtered data as a CSV file.

## 🗂️ Dataset Information

The project uses a Netflix Movies and TV Shows dataset in CSV format.

The dataset can contain the following fields:

- `type` — Movie or TV Show.
- `title` — Title of the movie or TV show.
- `director` — Director's name.
- `cast` — Actors appearing in the title.
- `country` — Country associated with the title.
- `date_added` — Date the title was added.
- `release_year` — Original release year.
- `rating` — Content rating.
- `duration` — Movie duration or number of TV-show seasons.
- `listed_in` — Genres or categories.

The project includes a sample dataset. For broader analysis, users can upload a larger compatible Netflix dataset.

## 🧹 Data Processing

The application performs several data-processing operations:

- Removes duplicate records.
- Handles missing values.
- Converts date fields into appropriate date formats.
- Extracts year and month information from dates.
- Processes movie durations and TV-show seasons.
- Prepares the dataset for analysis and visualization.

## 📈 Example Analysis

The dashboard can help answer questions such as:

- Are movies or TV shows more common in the dataset?
- Which genres have the most titles?
- Which countries have the most content?
- What are the most common content ratings?
- How has the number of titles added changed over time?
- What is the distribution of movie durations?
- Which directors and actors appear most frequently?
- How many seasons do TV shows have?

The results depend on the dataset and filters selected.

## 🐛 Troubleshooting

### Streamlit Command Not Found

Install the dependencies or run:

```bash
python -m streamlit run app.py
```

### Dataset Error

Ensure the uploaded CSV contains the required columns and uses the expected column names.

### No Data Appears

Clear some filters or select a wider range of years.

### Application Does Not Open

Check the terminal for errors and manually open:

```text
http://localhost:8501
```

## 🔮 Future Improvements

- Add more interactive charts.
- Improve data validation and error handling.
- Add additional filters and comparisons.
- Provide downloadable charts and reports.
- Add more advanced data-analysis features.
- Deploy the application online.

## 👩‍💻 Author

**Project Name:** Netflix Movies & TV Shows Analysis Web App  
**Programming Language:** Python  
**Project Type:** Data Analysis and Interactive Web Application

## 📄 Disclaimer

This project is developed for educational purposes and data-analysis practice. Netflix is a trademark of its respective owner. This project is not affiliated with or endorsed by Netflix.
