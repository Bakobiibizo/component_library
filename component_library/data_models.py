from fastapi.templating import Jinja2Templates


TEMPLATES = Jinja2Templates(directory="component_library/templates")


def get_templates():
    return TEMPLATES