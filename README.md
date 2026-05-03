# 🌿 AI Plant Disease Detection System

**Part of the Modular Smart Mini-Farm (MSMF)** — an international engineering collaboration between Belgium Campus iTversity and Penn State University, designed for deployment at Spa Park School in Bela-Bela, South Africa.

---

## 📌 Overview

This project is an AI-powered plant disease detection system that automates the identification of tomato leaf diseases using computer vision and machine learning.

The system captures plant images via a webcam, processes them through a REST API, and uses a TensorFlow Lite model to generate disease predictions. All data is stored and managed using Microsoft SQL Server.

It was developed as the **IT and AI component of the “Plants Tile”** within the Modular Smart Mini-Farm (MSMF), a multidisciplinary engineering project integrating software, hardware, and agricultural science to support sustainable farming education.

---

## 👨‍💻 My Contribution

This component of the Modular Smart Mini-Farm project focuses on the **AI-based plant disease detection pipeline**.

My responsibilities included:

* Designing and implementing the **Node.js (Express) REST API** for image ingestion
* Developing the **Python AI worker** to process images using a TensorFlow Lite model
* Integrating the system with **SQL Server** for data storage and communication between components
* Implementing a **decoupled architecture** where the API and AI worker communicate via the database
* Handling **image processing workflows**, including encoding, storage, and retrieval
* Ensuring the system runs reliably in a local development environment

This work forms the **core AI and backend functionality** of the Plants module in the MSMF system.

---

## 🎯 Objectives

* Automate plant disease detection using image-based analysis
* Reduce reliance on manual crop inspection
* Demonstrate integration of AI, backend systems, and databases
* Support smart farming and educational use in real-world environments

---

## 🏗️ System Architecture

```text
Webcam (capture.py)
      │
      │  HTTP POST (base64 image)
      ▼
Node.js REST API (server.ts)
      │
      │  INSERT into cropImages
      ▼
SQL Server — PlantDB
      │
      │  Worker polls every 5 seconds
      ▼
Python AI Worker (worker.py)
      │
      │  Runs TFLite inference via model_utils.py
      ▼
cropAiPredictions table
```

> The Node.js API and Python worker are **decoupled systems**. Communication occurs exclusively through the database, ensuring modularity and scalability.

---

## 🔍 System Workflow

1. The client captures an image using a webcam
2. The image is encoded and sent to the API
3. The API stores the image in SQL Server
4. The worker continuously polls for unprocessed images
5. The ML model processes the image
6. A disease prediction and confidence score are generated
7. Results are stored in the database

---

## 🧠 AI Model

| Property      | Detail                                            |
| ------------- | ------------------------------------------------- |
| Dataset       | Kaggle New Plant Diseases Dataset (Tomato subset) |
| Training Data | 12,824 training + 3,202 validation images         |
| Classes       | 10 tomato disease categories                      |
| Input Size    | 224 × 224 pixels                                  |
| Model Format  | TensorFlow Lite (.tflite)                         |
| File Location | `worker/plant_disease_model.tflite`               |

---

## 🗄️ Database Design (PlantDB)

### `cropImages`

Stores captured images and metadata:

* Image data (VARBINARY)
* Device and planting identifiers
* Timestamp

### `cropAiPredictions`

Stores model outputs:

* Disease name
* Confidence score
* Health status
* Timestamp

---

## 📁 Project Structure

```text
├── server/
│   └── server.ts          # Node.js REST API (port 5000)
├── client/
│   └── capture.py         # Webcam capture client
├── worker/
│   ├── worker.py          # Background AI worker
│   └── model_utils.py     # Model loading & inference
```

---

## ⚙️ Setup & Usage

### Prerequisites

* Python 3.11
* Node.js (v18+)
* SQL Server Express (TCP/IP enabled on port 1433)
* SQL Server Authentication enabled

---

### 1. Start the API

```bash
cd server
npx ts-node server.ts
```

---

### 2. Capture an Image

```bash
cd client
py -3.11 capture.py
```

---

### 3. Run the AI Worker

```bash
cd worker
py -3.11 worker.py
```

> ⚠️ Start the API **before** running the client or worker.

---

## 🌐 API Endpoint

### Upload Image

```http
POST /upload
Content-Type: application/json
```

### Request

```json
{
  "image": "base64_encoded_image"
}
```

### Response

```json
{
  "message": "Image stored successfully",
  "imageId": 1
}
```

---

## 🔧 Technical Notes

* TCP/IP must be enabled in SQL Server Configuration Manager
* Port 1433 must be explicitly configured
* SQL Server Authentication is required (Windows Auth unsupported via `mssql` over TCP)
* `tflite-runtime` is not supported on Python 3.14 (use Python 3.11)
* Model class labels must match training order exactly

---

## 🚀 Future Enhancements

| Current System   | Planned Upgrade              |
| ---------------- | ---------------------------- |
| Laptop webcam    | Raspberry Pi + Camera Module |
| Local SQL Server | Remote MySQL server          |
| Full TensorFlow  | Lightweight `tflite-runtime` |

---

## 🌍 Project Context

This system forms part of the **Modular Smart Mini-Farm (MSMF)** — a collaborative international initiative between Belgium Campus iTversity (South Africa) and Penn State University (USA).

The MSMF consists of five integrated modules:

* Power
* Plants
* Water
* Chickens
* Data

The final system will be deployed at **Spa Park School (Bela-Bela)** to support STEM education, sustainable agriculture awareness, and hands-on learning for middle school students.

---

## 🛠️ Technologies Used

* Python (OpenCV, TensorFlow Lite)
* Node.js (Express, TypeScript)
* Microsoft SQL Server
* REST API Architecture

---

## 📈 Key Features

* Automated plant disease detection
* Decoupled, database-driven architecture
* Real-time image processing pipeline
* Scalable and modular system design

---

## 👨‍💻 Author

Developed as part of an academic and international engineering collaboration project.
Enock-Mntungwa — Belgium Campus iTversity
---
