import asyncio
import openai
from sqlalchemy.ext.asyncio import AsyncSession
from db import engine, AsyncSessionLocal
from models import Base, Wine
from sqlalchemy.future import select

# Wine data to be inserted
wine_data = [
    {
        "name": "Château Margaux",
        "region": "Bordeaux",
        "varietal": "Cabernet Sauvignon",
        "description": "Rich, complex, with notes of dark berries.",
    },
    {
        "name": "Domaine de la Romanée-Conti",
        "region": "Burgundy",
        "varietal": "Pinot Noir",
        "description": "Elegant, floral, with a long finish.",
    },
]


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def generate_embedding(text: str):
    response = openai.Embedding.create(input=text, model="text-embedding-ada-002")
    return response["data"][0]["embedding"]


async def populate_wines():
    async with AsyncSessionLocal() as session:
        for wine in wine_data:
            embedding = await generate_embedding(wine["description"])
            new_wine = Wine(
                name=wine["name"],
                region=wine["region"],
                varietal=wine["varietal"],
                description=wine["description"],
                vector=embedding,
            )
            session.add(new_wine)
        await session.commit()


async def main():
    await create_tables()
    await populate_wines()


if __name__ == "__main__":
    asyncio.run(main())
