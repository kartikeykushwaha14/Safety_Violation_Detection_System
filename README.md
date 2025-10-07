# 🛡️ Shop Safety Violation Detection System

[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95-green)](https://fastapi.tiangolo.com/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-orange)](https://opencv.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-red)](https://docs.ultralytics.com/)

A **real-time video-based safety violation detection system** for retail stores using **YOLOv8** and **FastAPI**. This project is designed to enhance shop security by automatically detecting:

- 🔫 Guns  
- 🔪 Knives  
- 🛒 Shoplifting (hands near items)  
- 🤼 Fighting (persons in conflict)

The system provides **live video streaming**, **bounding boxes**, and **violation alerts** for immediate monitoring.

---

## 🎬 Demo Video

Click to watch the demo of the system detecting shoplifting and dangerous objects in a sample store video:

[![Watch Demo](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://github.com/kartikeykushwaha14/Safety_Violation_Detection_System/blob/main/demo%20(1).mp4)

Or place a demo video file in `app/static/demo_video.mp4` and access via web interface.

---

## ⚡ Features

- **Real-time detection:** Shows bounding boxes live while the video is being processed.  
- **Violation alerts:** Displays messages for detected safety violations immediately.  
- **Logging & reporting:** All violations saved with timestamps in `alerts.json`.  
- **Web interface:** Simple browser-based start/stop controls.  
- **Multi-format support:** `.mp4`, `.avi`, `.mov` video uploads.  
- **Customizable detection:** Swap YOLOv8 weights for other objects as needed.

---

## 🛠️ Tech Stack

- **Python 3.10+** – Core programming language  
- **FastAPI** – Web server and API framework  
- **OpenCV** – Video processing and annotation  
- **Ultralytics YOLOv8** – Object detection model  
- **Jinja2** – HTML templating for dynamic web pages  

---

## 📐 How It Works

1. **Frame Processing:** Reads each video frame using OpenCV.  
2. **YOLO Detection:** Detects `person`, `hand`, `gun`, `knife`, and store items.  
3. **Violation Rules:**
   - **Gun / Knife:** Draws a red bounding box with label.  
   - **Shoplifting:** Detects hands near objects; draws bounding boxes and shows "Shoplifting?" label.  
   - **Fighting:** Detects overlapping persons; shows "Fighting?" label with bounding boxes.  
4. **Live Streaming:** Frames with bounding boxes are streamed via HTTP to the browser for live feedback.  
5. **Logging:** All detected violations saved in `alerts.json` for auditing and reporting.  

---

## 📂 Project Structure

shop-safety-detector/
├── app/
│ ├── static/ # Processed videos & demo video
│ ├── templates/ # index.html for web interface
│ ├── alerts.json # Logged violations
│ └── detection.py # YOLO detection & streaming logic
├── models/
│ └── custom_shop_model.pt # YOLOv8 custom weights
├── main.py # FastAPI server
├── requirements.txt # Required Python packages
└── README.md # Documentation


---

## 🚀 Installation & Setup

1. **Clone the repository:**
```bash
1. **Clone the repository:**
git clone https://github.com/yourusername/shop-safety-detector.git
cd shop-safety-detector

2. **Create a virtual environment:**
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate

3. **Install dependencies:**
pip install -r requirements.txt
python -m uvicorn main:app --reload

4. Add YOLOv8 weights in models/ (e.g., custom_shop_model.pt).
You can train your own dataset using Ultralytics YOLOv8.

5. Run the FastAPI server:
python -m uvicorn main:app --reload

6. Open in browser: http://127.0.0.1:8000

7. Upload video and click Start Detection. Watch live detections and alerts.

```

## 💡 Advantages

Automated safety monitoring for retail stores

Reduces human monitoring effort

Real-time visual alerts for immediate action

Provides audit logs for security management

Easily extendable for other objects or live CCTV feeds

## 🧪 Testing

Add a test video app/static/test_video.mp4.

Upload via the web interface.

Observe live detection of shoplifting, fights, knives, and guns.

Check alerts.json for a complete record of violations.

## 📊 Future Enhancements

Real-time integration with CCTV cameras

Multi-store monitoring dashboard

Notification system via email or SMS for immediate alerts

AI-based behavior prediction to preempt potential theft

## 🔗 References

YOLOv8 Documentation

FastAPI Documentation

OpenCV Documentation

## 📄 License

MIT License © 2025

## 👤 Author

Kartikey Kushwaha
MCA | AI & ML Enthusiast | Android & Python Developer

