🧠 AI Image Processing Bots

Image Classification Bot (ResNet50) & Background Remover Bot (rembg)
An AI-powered desktop application suite built using Python, Deep Learning, and Computer Vision, demonstrating real-world usage of pretrained models through intuitive GUI-based tools.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

📌 Projects Overview
This repository contains two AI-based image processing applications:

Project

🖼️ Image Classification Bot

Description 

Classifies uploaded images using a pretrained ResNet50 model and displays prediction with confidence



Project 

✂️ Background Remover Bot

Discretion

Automatically removes background from images using the rembg deep learning model
Both projects focus on practical AI implementation, not just model accuracy.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🖼️ 1️⃣ Image Classification Bot (ResNet50)

🔍 Description
A desktop GUI application that allows users to upload an image and classify it into one of 1000 ImageNet classes using the ResNet50 pretrained convolutional neural network.

⚙️ How It Works
User uploads an image via GUI
Image is resized and preprocessed
ResNet50 predicts the image class

App displays:
Predicted class name
Confidence score (%)

🛠️ Tech Stack
Python 3.10
TensorFlow / Keras
ResNet50 (ImageNet weights)
Tkinter (GUI)
Pillow (Image handling)
NumPy

🧩 Key Features
User-friendly desktop interface
Pretrained deep learning model
Real-time prediction
Confidence score display
No training required (transfer learning)

🖥️ GUI Preview
Simple, clean, and minimal interface designed for easy interaction.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

✂️ 2️⃣ Background Remover Bot (rembg)

🔍 Description
An AI-powered background removal tool that automatically removes the background from images using a deep learning segmentation model via the rembg library.

⚙️ How It Works
User uploads an image
rembg model detects foreground
Background is removed automatically
Output image is saved with transparent background

🛠️ Tech Stack
Python
rembg
Pillow
NumPy
Tkinter (optional GUI version)

🧩 Key Features
Fully automatic background removal
Supports multiple image formats
High-quality foreground extraction
No manual masking required

🚀 What I Learned from These Projects
Working with pretrained deep learning models
Image preprocessing & tensor manipulation
Transfer learning concepts

🖥️GUI integration with AI models
Handling TensorFlow & Python version conflicts
Debugging real-world dependency issues
Converting ML scripts into usable applications

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🎯 Future Improvements

-Convert projects into .exe applications
-Add drag-and-drop support
-Batch image processing
-Deploy as a web app
-Add custom-trained models

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🤝 Author

Vedant Sonwalkar
CSE (AI & DS) Student
Passionate about AI, Computer Vision & Applied Machine Learning
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
