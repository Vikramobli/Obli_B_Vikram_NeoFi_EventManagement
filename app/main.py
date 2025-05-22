# Directory: app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, events, share, version

app = FastAPI(title="NeoFi Collaborative Event Manager", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(events.router, prefix="/api/events", tags=["Events"])
app.include_router(share.router, prefix="/api/events", tags=["Sharing"])
app.include_router(version.router, prefix="/api/events", tags=["Versioning"])

# Root
@app.get("/")
def read_root():
    return {"message": "NeoFi Backend Challenge - Event Management API"}