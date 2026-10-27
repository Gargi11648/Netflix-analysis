"""
Netflix Movies and TV Shows Analysis - Web App (Streamlit)
Run:  streamlit run app.py      (opens at http://localhost:8501)
"""
import os
import pandas as pd
import streamlit as st
from matplotlib.figure import Figure

import netflix_core as core

st.set_page_config(page_title="Netflix Analysis", page_icon="🎬", layout="wide")

DEFAULT_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "netflix_titles.csv")

st.markdown(
    "<h1 style='color:#E50914;margin-bottom:0'>NETFLIX <span style='color:#888;font-size:0.6em'>"
    "Movies &amp; TV Shows Analysis</span></h1>",
    unsafe_allow_html=True,
)


# ------------------------------------------------------------------
# Data loading
# ------------------------------------------------------------------
@st.cache_data(show_spinner="Loading and cleaning data...")
def get_data(source):
    """source is a file path (str) or uploaded file object."""
    return core.load_and_clean(source)


st.sidebar.header("1. Data")
uploaded = st.sidebar.file_uploader("Upload netflix_titles.csv", type="csv")

df = None
try:
    if uploaded is not None:
        df = get_data(uploaded)
        st.sidebar.success(f"Using uploaded file: {uploaded.name}")
    elif os.path.exists(DEFAULT_CSV):
        df = get_data(DEFAULT_CSV)
        st.sidebar.info("Using data/netflix_titles.csv")
except Exception as exc:
    st.error(f"Could not read the file: {exc}")
    st.stop()

if df is None:
    st.warning("Upload the Netflix titles CSV from the sidebar to begin.")
    st.stop()

if "is_sample" in df.columns:
    st.warning(
        "You are looking at the built-in SAMPLE: about 65 real Netflix titles, but the 'date added' "
        "values are simulated. Upload the full Kaggle `netflix_titles.csv` in the sidebar to analyse "
        "the complete, real catalogue."
    )

# ------------------------------------------------------------------
# Filters
# ------------------------------------------------------------------
st.sidebar.header("2. Filters")
types = st.sidebar.multiselect("Type", sorted(df["type"].unique()), default=sorted(df["type"].unique()))
y_min, y_max = int(df["year_added"].min()), int(df["year_added"].max())
if y_min < y_max:
    years = st.sidebar.slider("Year added to Netflix", y_min, y_max, (y_min, y_max))
else:
    years = (y_min, y_max)

all_genres = sorted(df["listed_in"].str.split(",").explode().str.strip().unique())
genres_sel = st.sidebar.multiselect("Genre (any of)", all_genres)

all_countries = sorted(c for c in df["country"].str.split(",").explode().str.strip().unique() if c != "Unknown")
countries_sel = st.sidebar.multiselect("Country (any of)", all_countries)

all_ratings = sorted(df["rating"].unique())
ratings_sel = st.sidebar.multiselect("Rating", all_ratings)

view = df[df["type"].isin(types) & df["year_added"].between(years[0], years[1])]
if genres_sel:
    view = view[core.has_any(view["listed_in"], genres_sel)]
if countries_sel:
    view = view[core.has_any(view["country"], countries_sel)]
if ratings_sel:
    view = view[view["rating"].isin(ratings_sel)]
view = view.copy()

if view.empty:
    st.warning("No titles match these filters. Try widening them.")
    st.stop()

# ------------------------------------------------------------------
# KPI row
# ------------------------------------------------------------------
n_movies = int((view["type"] == "Movie").sum())
n_shows = int((view["type"] == "TV Show").sum())
mv = view[view["type"] == "Movie"]["duration_num"].dropna()
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total titles", f"{len(view):,}")
c2.metric("Movies", f"{n_movies:,}")
c3.metric("TV shows", f"{n_shows:,}")
c4.metric("Avg movie length", f"{mv.mean():.0f} min" if not mv.empty else "n/a")


# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------
def show_chart(name, data):
    fig = Figure(figsize=(7, 4.2))
    ax = fig.subplots()
    core.CHARTS[name](data, ax)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    fig.tight_layout()
    st.pyplot(fig)


tab_over, tab_cat, tab_ppl, tab_titles, tab_ins = st.tabs(
    ["Overview", "Genres, Countries & Ratings", "Directors & Actors", "Explore Titles", "Key Insights"]
)

with tab_over:
    a, b = st.columns(2)
    with a:
        show_chart("Movies vs TV Shows (Pie)", view)
    with b:
        show_chart("Content Added Per Year (Line)", view)
    a, b = st.columns(2)
    with a:
        show_chart("Titles Added by Month", view)
    with b:
        show_chart("Release Year Distribution", view)

with tab_cat:
    a, b = st.columns(2)
    with a:
        show_chart("Top 10 Genres", view)
    with b:
        show_chart("Top 10 Countries", view)
    a, b = st.columns(2)
    with a:
        show_chart("Ratings Distribution", view)
    with b:
        show_chart("Movie Duration (Histogram)", view)
    show_chart("TV Show Seasons", view)

with tab_ppl:
    a, b = st.columns(2)
    with a:
        show_chart("Top 10 Directors", view)
    with b:
        show_chart("Top 10 Actors", view)

    st.subheader("Look up a director or actor")
    person = st.text_input("Type a name (e.g. a director or actor)")
    if person.strip():
        q = person.strip().lower()
        hits = view[view["director"].str.lower().str.contains(q, regex=False)
                    | view["cast"].str.lower().str.contains(q, regex=False)]
        st.write(f"**{len(hits)}** titles found")
        if not hits.empty:
            cols = [c for c in ["title", "type", "release_year", "rating", "duration", "listed_in"] if c in hits.columns]
            st.dataframe(hits[cols], use_container_width=True, hide_index=True)

with tab_titles:
    st.subheader("Search and explore the actual titles")
    s1, s2 = st.columns([2, 1])
    query = s1.text_input("Search by title")
    sort_by = s2.selectbox("Sort by", ["Newest added", "Oldest release", "Newest release", "Longest duration", "Title (A-Z)"])

    data = view
    if query.strip() and "title" in data.columns:
        data = data[data["title"].astype(str).str.lower().str.contains(query.strip().lower(), regex=False)]

    if sort_by == "Newest added":
        data = data.sort_values("date_added", ascending=False)
    elif sort_by == "Oldest release":
        data = data.sort_values("release_year")
    elif sort_by == "Newest release":
        data = data.sort_values("release_year", ascending=False)
    elif sort_by == "Longest duration":
        data = data.sort_values("duration_num", ascending=False)
    elif "title" in data.columns:
        data = data.sort_values("title")

    show_cols = [c for c in ["title", "type", "director", "country", "release_year", "rating",
                             "duration", "listed_in", "date_added"] if c in data.columns]
    st.caption(f"{len(data):,} titles")
    st.dataframe(data[show_cols], use_container_width=True, hide_index=True, height=380)

    if "title" in data.columns and not data.empty:
        st.subheader("Title details")
        pick = st.selectbox("Pick a title", data["title"].head(300).tolist())
        row = data[data["title"] == pick].iloc[0]
        d1, d2 = st.columns([1, 2])
        d1.markdown(
            f"**Type:** {row['type']}  \n**Released:** {row['release_year']}  \n"
            f"**Rating:** {row['rating']}  \n**Duration:** {row['duration']}  \n"
            f"**Added:** {row['date_added'].strftime('%d %b %Y')}"
        )
        d2.markdown(
            f"**Director:** {row['director']}  \n**Cast:** {row['cast']}  \n"
            f"**Country:** {row['country']}  \n**Genres:** {row['listed_in']}  \n"
            + (f"**About:** {row['description']}" if "description" in row.index else "")
        )

    st.download_button("Download filtered data (CSV)", view.to_csv(index=False).encode("utf-8"),
                       file_name="netflix_filtered.csv", mime="text/csv")

with tab_ins:
    st.code(core.build_insights(view), language=None)
