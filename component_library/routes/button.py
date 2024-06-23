from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from pytailwindcss import run as tai

from component_library.data_models import get_templates

button = APIRouter()

templates = get_templates()

@button.post("/button-click", response_class=HTMLResponse)
async def button_click(request: Request):
    # Simulating a button click response
    return templates.TemplateResponse(request, name="components/button.html", context={
        "tai": tai(["-i", "component_library/static/css/tailwind.css", "-o", "component_library/static/css/main.css"]),
        "type": "default",
        "size": "medium",
        "text": "Clicked!",
    })
