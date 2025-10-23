# note: This generates a default spec based on the default API config. Any modifications made to the spec will need to be reflected in the API backend.

from fastapi.openapi.utils import get_openapi
from main import app
import yaml
import os

openapi_schema = get_openapi(
    title="Task Management API",
    version=app.version,
    routes=app.routes
)

os.makedirs("docs", exist_ok=True)

with open("docs/openapi.yaml", "w") as f:
    yaml.dump(openapi_schema, f, sort_keys=False)

print("Swagger/OpenAPI spec saved to openapi.yaml")