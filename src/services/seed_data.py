import asyncio
import uuid

from sqlalchemy import select

from src.core.temporal import (
    get_temporal_client,
)

from src.db.database import (
    AsyncSessionLocal,
)

from src.models.borrower import (
    Borrower,
)

from src.models.workflow_instance import (
    WorkflowInstance,
)

from src.workflows.borrower_workflow import (
    BorrowerWorkflow,
)


async def main():

    # Connect to Temporal
    client = await get_temporal_client()

    # Find an existing borrower
    async with AsyncSessionLocal() as session:

        result = await session.execute(
            select(Borrower)
            .where(
                Borrower.full_name == "John Doe"
            )
        )

        borrower = result.scalar_one()

        borrower_id = borrower.id
        tenant_id = borrower.tenant_id

        print(
            f"Borrower ID: {borrower_id}"
        )

        print(
            f"Tenant ID: {tenant_id}"
        )

        # Generate Temporal workflow ID
        workflow_id = (
            f"borrower-{uuid.uuid4()}"
        )

        # Create WorkflowInstance
        workflow_instance = WorkflowInstance(
            borrower_id=borrower_id,
            tenant_id=tenant_id,
            workflow_id=workflow_id,
            current_state="STARTED",
        )

        session.add(workflow_instance)

        await session.commit()

        print(
            "WorkflowInstance created"
        )

    # Start Temporal workflow
    handle = await client.start_workflow(

        BorrowerWorkflow.run,

        # Pass the REAL borrower UUID
        str(borrower_id),

        id=workflow_id,

        task_queue="borrower-task-queue",
    )

    print(
        f"Workflow started: {workflow_id}"
    )

    # Wait for workflow completion
    result = await handle.result()

    print(result)


if __name__ == "__main__":
    asyncio.run(main())