from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from component_library.data_models import get_templates
from component_library.routes.button import button

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="component_library/static"), name="static")

templates = get_templates()

app.include_router(button)

@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", status_code=200)

@app.get("/component/{name}", response_class=HTMLResponse)
async def get_component(request: Request):
    name = request.path_params["name"]
    template_path = Path(f"component_library/templates/components/{name}.html")
    if not template_path.is_file():
        raise HTTPException(status_code=404, detail="Component not found")
    return templates.TemplateResponse(request=request, name=f"components/{name}.html", status_code=200)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)