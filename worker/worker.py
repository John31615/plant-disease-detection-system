import pyodbc
import time
from model_utils import predict

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=NGCEBO-SPACE\\SQLEXPRESS;"
    "DATABASE=PlantDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

while True:
    try:
        cursor.execute("""
        SELECT cropImageId, imageData
        FROM cropImages
        WHERE cropImageId NOT IN (
            SELECT imageId FROM cropAiPredictions
        )
        """)

        rows = cursor.fetchall()

        for row in rows:
            image_id = row[0]
            image_bytes = row[1]

            disease, confidence = predict(image_bytes)

            status = "healthy" if disease == "Healthy" else "diseased"

            cursor.execute("""
            INSERT INTO cropAiPredictions 
            (imageId, diseaseName, confidenceScore, status)
            VALUES (?, ?, ?, ?)
            """, (image_id, disease, confidence, status))

            conn.commit()

    except Exception as e:
        print("Error:", e)

    time.sleep(5)
