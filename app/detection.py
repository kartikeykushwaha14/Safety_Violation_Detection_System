import cv2
from ultralytics import YOLO
import os
import json
from datetime import datetime

# Load YOLOv8 model
model = YOLO("models/yolov8n.pt")  # replace with custom weights

# Log violations
def log_violation(violations):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "violations": violations
    }
    log_file = "app/alerts.json"
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            logs = json.load(f)
    else:
        logs = []
    logs.append(log_entry)
    with open(log_file, "w") as f:
        json.dump(logs, f, indent=4)

# Generator for streaming frames with violations
def stream_video(video_path):
    cap = cv2.VideoCapture(video_path)
    violations = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(frame, verbose=False)
        frame_violations = []
        boxes_info = []

        for r in results:
            for box in r.boxes:
                cls = model.names[int(box.cls)].lower()
                conf = float(box.conf)
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                boxes_info.append({"class": cls, "coords": (x1, y1, x2, y2), "conf": conf})

                if cls in ["knife","gun"] and conf>0.5:
                    frame_violations.append({"object": cls, "confidence": round(conf,2)})
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0,0,255), 2)
                    cv2.putText(frame, f"{cls} {conf:.2f}", (x1,y1-10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0),2)

         # Detect hands near objects -> Shoplifting
        hands = [b for b in boxes_info if b["class"] == "hand"]
        objects = [b for b in boxes_info if b["class"] not in ["hand", "person"]]

        for hand in hands:
            hx1, hy1, hx2, hy2 = hand["coords"]
            for obj in objects:
                ox1, oy1, ox2, oy2 = obj["coords"]
                # If hand is close to object -> potential shoplifting
                if abs(hx1 - ox1) < 50 and abs(hy1 - oy1) < 50:
                    frame_violations.append({"object":"shoplifting","confidence": 0.9})
                    cv2.putText(frame, "Shoplifting?", (hx1, hy1 - 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                    cv2.rectangle(frame, (hx1, hy1), (hx2, hy2), (0, 0, 255), 2)

        # Stealing detection
        for hand in hands:
            hx1, hy1, hx2, hy2 = hand["coords"]
            for obj in objects:
                ox1, oy1, ox2, oy2 = obj["coords"]
                if abs(hx1-ox1)<50 and abs(hy1-oy1)<50:
                    frame_violations.append({"object":"stealing","confidence":0.9})
                    cv2.putText(frame,"Stealing?",(hx1,hy1-30),
                                cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)

        # Fighting detection

        # for box in boxes_info:
        #     print(f"Detected {box['class']} violations in current frame.")

        persons = [b for b in boxes_info if b["class"]=="person"]
        for i in range(len(persons)):
            for j in range(i+1,len(persons)):
                x1a,y1a,x2a,y2a = persons[i]["coords"]
                x1b,y1b,x2b,y2b = persons[j]["coords"]
                if (x1a<x2b and x2a>x1b) and (y1a<y2b and y2a>y1b):
                    frame_violations.append({"object":"fighting","confidence":0.9})
                    cv2.rectangle(frame,(min(x1a,x1b),min(y1a,y1b)),
                                  (max(x2a,x2b),max(y2a,y2b)),(0,0,255),3)
                    cv2.putText(frame,"Fighting?",(min(x1a,x1b),min(y1a,y1b)-10),
                                cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)

        if frame_violations:
            violations.append(frame_violations)

        # Encode frame as JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    cap.release()
    log_violation(violations)
