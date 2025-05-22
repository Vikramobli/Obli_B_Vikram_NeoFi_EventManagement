# Directory: app/routes/version.py
from fastapi import APIRouter

router = APIRouter()

# TODO: implement /{id}/history/{versionId}, /{id}/rollback/{versionId}, /{id}/changelog, /{id}/diff/{v1}/{v2}