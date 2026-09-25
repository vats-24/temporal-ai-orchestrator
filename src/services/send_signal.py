import asyncio

from src.core.temporal import (
    get_temporal_client,
)

from src.workflows.borrower_workflow import (
    BorrowerWorkflow,
)


WORKFLOW_ID = "borrower-c5012e9f-c26e-490e-8b85-e8f8fb09e859"


async def main():

    client = await get_temporal_client()

    handle = client.get_workflow_handle(
        WORKFLOW_ID
    )

    await handle.signal(
        BorrowerWorkflow.borrower_update,

        "PROMISE_TO_PAY"
    )

    print(
        "Signal sent successfully"
    )


if __name__ == "__main__":
    asyncio.run(main())