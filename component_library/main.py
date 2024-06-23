from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI()
templates = Jinja2Templates(directory="component_library/templates")

@app.get("/component/{name}", response_class=HTMLResponse)
async def get_component(request: Request):
    name = request.path_params["name"]
    template_path = Path(f"component_library/templates/{name}.html")
    if not template_path.is_file():
        raise HTTPException(status_code=404, detail="Component not found")
    return templates.TemplateResponse(request=request, name=f"{name}.html", status_code=200)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)