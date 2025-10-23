from fastapi import FastAPI, APIRouter
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import JSONResponse
from routes.task_create import router as create_router
from routes.task_read import router as read_router
from routes.task_update import router as update_router
from routes.task_soft_delete import router as soft_delete_router
from routes.task_perm_delete import router as perm_delete_router
from routes.task_recover import router as recover_router
import yaml
import os
from fastapi.openapi.utils import get_openapi

app = FastAPI(openapi_url=None, docs_url=None)
router = APIRouter()

@router.get("/")
def default():
    return {
        "message": "Welcome to the Task Management API!",
        "docs_url": "/docs",
        "openapi_url": "/openapi.json"
    }

app.include_router(create_router, prefix="/tasks", tags=["task_create"])
app.include_router(read_router, prefix="/tasks", tags=["task_read"])
app.include_router(update_router, prefix="/tasks", tags=["task_update"])
app.include_router(soft_delete_router, prefix="/tasks", tags=["task_soft_delete"])
app.include_router(perm_delete_router, prefix="/tasks", tags=["task_perm_delete"])
app.include_router(recover_router, prefix="/tasks", tags=["task_recover"])
app.include_router(router) # Needed for default route to work

# Load custom Swagger (OpenAPI) YAML spec if it exists, otherwise auto-generate
if os.path.exists("docs/openapi.yaml"):
    with open("docs/openapi.yaml", "r") as f:
        openapi_schema = yaml.safe_load(f)
else:
    openapi_schema = get_openapi(
        title="Task Management API",
        version=app.version,
        routes=app.routes
    )

# Serve the custom spec at /openapi.json
@app.get("/openapi.json", include_in_schema=False)
def get_open_api():
    return JSONResponse(content=openapi_schema)

# Serve Swagger UI that uses custom spec
@app.get("/docs", include_in_schema=False)
def custom_swagger_ui():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Task Management API Spec")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
