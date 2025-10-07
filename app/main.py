from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.detection import stream_video
import tempfile, os

app = FastAPI(title="Safety Violation Detector")
os.makedirs("app/static", exist_ok=True)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

uploaded_video_path = None

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def upload_video(file: UploadFile = File(...)):
    global uploaded_video_path
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    temp_file.write(await file.read())
    temp_file.seek(0)
    uploaded_video_path = temp_file.name
    return {"message":"Video uploaded!"}

@app.get("/video_feed")
def video_feed():
    if not uploaded_video_path:
        return HTMLResponse("Upload a video first!")
    return StreamingResponse(stream_video(uploaded_video_path),
                             media_type='multipart/x-mixed-replace; boundary=frame')
