from backend.database import Base, engine
from backend.models import Review


print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")
