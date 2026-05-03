import express, { Request, Response } from "express";
import sql from "mssql";
import cors from "cors";

const app = express();
app.use(express.json({ limit: "10mb" }));
app.use(cors());

const dbConfig: sql.config = {
  user: "plantuser",
  password: "Plant123!",
  server: "localhost",
  port: 1433,
  database: "PlantDB",
  options: {
    encrypt: false,
    trustServerCertificate: true
  }
};

sql.connect(dbConfig)
  .then(() => console.log("Connected to SQL Server"))
  .catch(err => console.error("DB Connection Error:", err));

app.post("/api/crop-images", async (req: Request, res: Response) => {
  try {
    const { plantingId, deviceId, image } = req.body;

    if (!image) {
      return res.status(400).json({ error: "No image provided" });
    }

    const buffer = Buffer.from(image, "base64");

    await sql.query`
      INSERT INTO cropImages (plantingId, deviceId, imageData)
      VALUES (${plantingId}, ${deviceId}, ${buffer})
    `;

    res.json({ message: "Image stored successfully" });

  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Server error" });
  }
});

app.listen(5000, () => {
  console.log("Server running on http://localhost:5000");
});
