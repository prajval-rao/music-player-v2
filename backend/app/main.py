from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()

origins = [
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "http://0.0.0.0:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="../..")

@app.get("/", response_class=HTMLResponse)
def main_page(request: Request):
    return templates.TemplateResponse(request, "frontend/index.html")