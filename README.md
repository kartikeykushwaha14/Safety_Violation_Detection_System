# Shop Safety Violation Detection System

A **real-time video-based safety violation detection system** for shops and retail stores. This system uses **YOLOv8 object detection** to detect potential safety violations and alerts the user with live bounding boxes and violation messages.

---

## Features

- **Detects dangerous items**: Guns, Knives.
- **Detects Shoplifting**: Hands near objects.
- **Detects Fighting**: Overlapping persons in the frame.
- **Live video streaming**: Shows processed video with bounding boxes in real-time.
- **Violation logging**: Logs all violations with timestamp in `alerts.json`.
- **Web-based interface**: Start/Stop detection directly from the browser.

---

## Advantages

- **Real-time monitoring**: Helps store managers monitor safety without manually watching hours of footage.
- **Automatic alert system**: Notifies security teams about potential threats immediately.
- **Visual evidence**: Bounding boxes highlight violations for easy review.
- **Flexible deployment**: Can process pre-recorded videos or live CCTV feeds.
- **Customizable**: YOLOv8 model can be trained for additional objects or behaviors.

---

## Requirements

- Python 3.10+
- OpenCV (`opencv-python`)
- FastAPI (`fastapi`)
- Uvicorn (`uvicorn`)
- Ultralytics YOLOv8 (`ultralytics`)
- Jinja2 (`jinja2`) for templates
- A YOLOv8 custom-trained model capable of detecting `gun`, `knife`, `hand`, `person`, and other shop-related objects.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/shop-safety-detector.git
cd shop-safety-detector
