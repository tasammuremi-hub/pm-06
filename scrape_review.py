
import pyodbc
import requests
from bs4 import BeautifulSoup


connection_string = (
    r"DRIVER={ODBC Driver 18 for SQL Server};"
    r"SERVER=LAPTOP-UEE8OBDQ\SQLEXPRESS;"
    r"DATABASE=MoviesReviewDB;"
    r"Trusted_Connection=yes;"
    r"Encrypt=yes;"
    r"TrustServerCertificate=yes;"
)

conn = None
cursor = None

try:
    conn = pyodbc.connect(connection_string, timeout=10)
    cursor = conn.cursor()

    print("Connected to the database successfully.")

    url = "http://127.0.0.1:8000/reviews.html"
    response = requests.get(url, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    reviews = soup.select(".review-card")

    if not reviews:
        print("No reviews found on the page.")

    inserted_records = 0

    for review in reviews:
        reviewer_name = review.select_one(".reviewer").get_text(strip=True)
        review_title = review.select_one(".movie-title").get_text(strip=True)
        review_text = review.select_one(".review-text").get_text(strip=True)
        review = int(review.select_one(".rating").get_text(strip=True))

        cursor.execute(
            """
            INSERT INTO MoviesReviewDB
                (ReviewerName, MovieTitle, ReviewText, Rating)
            VALUES (?, ?, ?, ?)
            """,
            (reviewer_name, review_title, review_text, review),
        )

        inserted_records += 1

        conn.commit()
        print(
            f"{inserted_records} movie reviews inserted into the database successfully.")

except requests.RequestException as error:
    print(f"Website connection error: {error}")
    print("error")

except requests.RequestException as error:
        print(f"Website connection error: {error}")
        print("error")

except pyodbc.Error as error:
    print(f"SQL Server connection or database error: {error}")
    print("error")

except Exception as error:
    print(f"An unexpected error occurred: {error}")
    print("error")

finally:
    if cursor is not None:
        cursor.close()

    if conn is not None:
        conn.close()
        print("Database connection closed.")
