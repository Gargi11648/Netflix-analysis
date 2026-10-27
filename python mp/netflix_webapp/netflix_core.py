"""
netflix_core.py
Data cleaning, chart-drawing functions and insights used by the GUI (netflix_gui.py).
Every chart function has the signature  chart(df, ax)  and draws onto a Matplotlib Axes.
"""
import pandas as pd

NETFLIX_RED = "#E50914"
DARK = "#221F1F"
MONTH_ORDER = ["January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]


# ------------------------------------------------------------------
# Loading and cleaning
# ------------------------------------------------------------------
def load_and_clean(path):
    df = pd.read_csv(path)
    required = {"type", "director", "cast", "country", "date_added",
                "release_year", "rating", "duration", "listed_in"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError("CSV is missing columns: " + ", ".join(sorted(missing)))

    df = df.drop_duplicates()
    for col in ["director", "cast", "country"]:
        df[col] = df[col].fillna("Unknown")
    df["rating"] = df["rating"].fillna("Not Rated")

    df["date_added"] = pd.to_datetime(df["date_added"].astype(str).str.strip(),
                                      format="mixed", errors="coerce")
    df = df.dropna(subset=["date_added"]).copy()
    df["year_added"] = df["date_added"].dt.year.astype(int)
    df["month_added"] = df["date_added"].dt.month_name()
    df["duration_num"] = df["duration"].astype(str).str.extract(r"(\d+)")[0].astype(float)
    return df.reset_index(drop=True)


def has_any(series, selected):
    """True where a comma-separated cell contains ANY of the selected values (exact match)."""
    wanted = set(selected)
    return series.apply(lambda cell: any(x.strip() in wanted for x in str(cell).split(",")))


def _empty(ax, msg="No data for this selection"):
    ax.text(0.5, 0.5, msg, ha="center", va="center", fontsize=12, transform=ax.transAxes)
    ax.set_axis_off()


def _explode_counts(df, col, skip="Unknown", top=10):
    s = df[df[col] != skip][col].str.split(",").explode().str.strip()
    return s.value_counts().head(top)


def _barh(ax, counts, title, xlabel, color):
    if counts.empty:
        return _empty(ax)
    counts.sort_values().plot(kind="barh", color=color, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("")


# ------------------------------------------------------------------
# Charts
# ------------------------------------------------------------------
def chart_type_split(df, ax):
    counts = df["type"].value_counts()
    if counts.empty:
        return _empty(ax)
    ax.pie(counts, labels=counts.index, autopct="%1.1f%%", startangle=90,
           colors=[NETFLIX_RED, DARK][:len(counts)], wedgeprops={"edgecolor": "white"})
    ax.set_title("Movies vs TV Shows")


def chart_per_year(df, ax):
    if df.empty:
        return _empty(ax)
    data = df.groupby(["year_added", "type"]).size().unstack(fill_value=0)
    data.plot(kind="line", marker="o", color=[NETFLIX_RED, DARK][:data.shape[1]], ax=ax)
    ax.set_title("Content Added Per Year")
    ax.set_xlabel("Year Added")
    ax.set_ylabel("Number of Titles")


def chart_countries(df, ax):
    _barh(ax, _explode_counts(df, "country"), "Top 10 Countries", "Number of Titles", NETFLIX_RED)


def chart_genres(df, ax):
    _barh(ax, _explode_counts(df, "listed_in", skip=""), "Top 10 Genres", "Number of Titles", DARK)


def chart_ratings(df, ax):
    counts = df["rating"].value_counts().head(8)
    if counts.empty:
        return _empty(ax)
    counts.plot(kind="bar", color=NETFLIX_RED, ax=ax)
    ax.set_title("Most Common Ratings")
    ax.set_xlabel("Rating")
    ax.set_ylabel("Number of Titles")
    ax.tick_params(axis="x", rotation=0)


def chart_movie_duration(df, ax):
    movies = df[df["type"] == "Movie"]["duration_num"].dropna()
    if movies.empty:
        return _empty(ax, "No movies in this selection")
    ax.hist(movies, bins=25, color=NETFLIX_RED, edgecolor="white")
    ax.axvline(movies.mean(), color=DARK, linestyle="--", label=f"Mean = {movies.mean():.0f} min")
    ax.set_title("Movie Duration Distribution")
    ax.set_xlabel("Minutes")
    ax.set_ylabel("Number of Movies")
    ax.legend()


def chart_tv_seasons(df, ax):
    shows = df[df["type"] == "TV Show"]["duration_num"].dropna()
    if shows.empty:
        return _empty(ax, "No TV shows in this selection")
    shows.astype(int).value_counts().sort_index().plot(kind="bar", color=DARK, ax=ax)
    ax.set_title("TV Shows by Number of Seasons")
    ax.set_xlabel("Seasons")
    ax.set_ylabel("Number of Shows")
    ax.tick_params(axis="x", rotation=0)


def chart_monthly(df, ax):
    if df.empty:
        return _empty(ax)
    monthly = df["month_added"].value_counts().reindex(MONTH_ORDER).fillna(0)
    monthly.plot(kind="bar", color=NETFLIX_RED, ax=ax)
    ax.set_title("Titles Added by Month")
    ax.set_xlabel("Month")
    ax.set_ylabel("Number of Titles")
    ax.tick_params(axis="x", rotation=45)


def chart_directors(df, ax):
    _barh(ax, _explode_counts(df, "director"), "Top 10 Directors", "Number of Titles", DARK)


def chart_actors(df, ax):
    _barh(ax, _explode_counts(df, "cast"), "Top 10 Actors", "Number of Titles", NETFLIX_RED)


def chart_release_years(df, ax):
    if df.empty:
        return _empty(ax)
    df["release_year"].plot(kind="hist", bins=30, color=DARK, edgecolor="white", ax=ax)
    ax.set_title("Release Year Distribution")
    ax.set_xlabel("Release Year")
    ax.set_ylabel("Number of Titles")


CHARTS = {
    "Movies vs TV Shows (Pie)": chart_type_split,
    "Content Added Per Year (Line)": chart_per_year,
    "Top 10 Countries": chart_countries,
    "Top 10 Genres": chart_genres,
    "Ratings Distribution": chart_ratings,
    "Movie Duration (Histogram)": chart_movie_duration,
    "TV Show Seasons": chart_tv_seasons,
    "Titles Added by Month": chart_monthly,
    "Top 10 Directors": chart_directors,
    "Top 10 Actors": chart_actors,
    "Release Year Distribution": chart_release_years,
}


# ------------------------------------------------------------------
# Insights text
# ------------------------------------------------------------------
def build_insights(df):
    if df.empty:
        return "No data for this selection."
    lines = []
    n = len(df)
    lines.append(f"Total titles: {n}")
    tc = df["type"].value_counts()
    for t, c in tc.items():
        lines.append(f"  {t}: {c} ({c / n * 100:.1f}%)")
    lines.append(f"Peak year for additions: {df['year_added'].value_counts().idxmax()}")
    lines.append(f"Busiest month for additions: {df['month_added'].value_counts().idxmax()}")
    for label, col, skip in [("Top country", "country", "Unknown"),
                             ("Top genre", "listed_in", ""),
                             ("Top director", "director", "Unknown"),
                             ("Top actor", "cast", "Unknown")]:
        c = _explode_counts(df, col, skip=skip, top=1)
        if not c.empty:
            lines.append(f"{label}: {c.index[0]} ({c.iloc[0]} titles)")
    lines.append(f"Most common rating: {df['rating'].value_counts().idxmax()}")
    mv = df[df["type"] == "Movie"]["duration_num"].dropna()
    if not mv.empty:
        lines.append(f"Average movie length: {mv.mean():.0f} minutes")
    tv = df[df["type"] == "TV Show"]["duration_num"].dropna()
    if not tv.empty:
        lines.append(f"Average TV show seasons: {tv.mean():.1f}")
    gap = (df["year_added"] - df["release_year"])
    gap = gap[gap >= 0]
    if not gap.empty:
        lines.append(f"Avg gap between release and Netflix addition: {gap.mean():.1f} years")
    return "\n".join(lines)
