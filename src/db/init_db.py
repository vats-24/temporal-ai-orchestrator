import asyncio 

from src.db.database import engine
from src.db.base import Base

import src.models

async def init():
    async with engine.begin() as conn:
        await conn.run_sync(
            Base.metadata.create_all
        )

if __name__ == "__main__":
    asyncio.run(init())