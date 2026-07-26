from temporalio.client import Client
from src.core.config import settings

async def get_temporal_client():
    client = await Client.connect(settings.TEMPORAL_SERVER)

    return client