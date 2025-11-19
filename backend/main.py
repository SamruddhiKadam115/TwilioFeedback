from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import review_router, webhook_router
from backend.database import Base, engine
from sqlalchemy import text

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

# Allow requests from the Vite dev server during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173", "http://localhost:5174", "http://127.0.0.1:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"status": "ok", "database": "ok"}
    except Exception:
        return {"status": "error", "database": "unavailable"}


# Include routers
app.include_router(review_router.router, prefix="/api/reviews", tags=["reviews"])
app.include_router(webhook_router.router, prefix="/webhook", tags=["webhook"])