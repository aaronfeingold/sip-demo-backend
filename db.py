from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from config import Settings

# Load DATABASE_URL from .env
# Initialize settings
settings = Settings()

# Create Async Engine
engine = create_async_engine(settings.DATABASE_URL, echo=True, future=True)

# Create session factory
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Dependency to get DB session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
