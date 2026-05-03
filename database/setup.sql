-- Plant Disease Detection System - Database Setup Script
-- Run this in SQL Server Management Studio (SSMS) to set up the database

-- 1. Create the database
CREATE DATABASE PlantDB;
GO

USE PlantDB;
GO

-- 2. Create tables
CREATE TABLE cropImages (
    cropImageId INT IDENTITY PRIMARY KEY,
    plantingId INT,
    deviceId INT,
    imageData VARBINARY(MAX),
    createdAt DATETIME DEFAULT GETDATE()
);

CREATE TABLE cropAiPredictions (
    predictionId INT IDENTITY PRIMARY KEY,
    imageId INT REFERENCES cropImages(cropImageId),
    diseaseName NVARCHAR(100),
    confidenceScore FLOAT,
    status NVARCHAR(50),
    createdAt DATETIME DEFAULT GETDATE()
);
GO

-- 3. Create login and user for the server
CREATE LOGIN plantuser WITH PASSWORD = 'Plant123!';
GO

CREATE USER plantuser FOR LOGIN plantuser;
ALTER ROLE db_owner ADD MEMBER plantuser;
GO

PRINT 'Database setup complete!';
