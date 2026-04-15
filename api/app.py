from fastapi import FastAPI
from datetime import datetime
import sqlite3
from textblob import TextBlob

app = FastAPI()

# -----------------------------
# DATABASE SETUP
# -----------------------------
conn = sqlite3.connect("data/poll.db", check_same_thread=False)
cursor = conn.cursor()

# FULL TABLE (WITH FEEDBACK + SENTIMENT)
cursor.execute("""
CREATE TABLE IF NOT EXISTS polls (
    timestamp TEXT,
    user TEXT,
    tool TEXT,
    region TEXT,
    rating INTEGER,
    feedback TEXT,
    sentiment TEXT
)
""")
conn.commit()

# -----------------------------
# HOME ROUTE
# -----------------------------
@app.get("/")
def home():
    return {"message": "Poll API Running 🚀"}

# -----------------------------
# SUBMIT POLL (WITH FEEDBACK + AI SENTIMENT)
# -----------------------------
@app.post("/submit")
def submit_poll(user: str, tool: str, region: str, rating: int, feedback: str):

    # 🔥 SENTIMENT ANALYSIS
    polarity = TextBlob(feedback).sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # INSERT INTO DATABASE
    cursor.execute(
        "INSERT INTO polls VALUES (?, ?, ?, ?, ?, ?, ?)",
        (str(datetime.now()), user, tool, region, rating, feedback, sentiment)
    )
    conn.commit()

    return {
        "status": "Vote Recorded ✅",
        "sentiment": sentiment
    }

# -----------------------------
# GET TOOL RESULTS
# -----------------------------
@app.get("/results")
def get_results():
    cursor.execute("SELECT tool, COUNT(*) FROM polls GROUP BY tool")
    data = cursor.fetchall()

    result = {tool: count for tool, count in data}
    return {"results": result}

# -----------------------------
# GET FULL DATA (FOR DASHBOARD)
# -----------------------------
@app.get("/all-data")
def get_all_data():
    cursor.execute("SELECT * FROM polls")
    data = cursor.fetchall()

    columns = ["Timestamp", "User", "Tool", "Region", "Rating", "Feedback", "Sentiment"]

    result = [dict(zip(columns, row)) for row in data]
    return result

# -----------------------------
# EXPORT FOR POWER BI
# -----------------------------
@app.get("/export")
def export_data():
    cursor.execute("SELECT * FROM polls")
    data = cursor.fetchall()

    return {"data": data}