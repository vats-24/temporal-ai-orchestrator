import asyncio

from temporalio.worker import (
    Worker)
from temporalio.worker.workflow_sandbox import (
    SandboxRestrictions,
    SandboxedWorkflowRunner
)

from src.core.temporal import (
    get_temporal_client,
)

from src.workflows.borrower_workflow import (
    BorrowerWorkflow,
)

from src.activities.borrower_activities import (
    attempt_contact,
    evaluate_risk,
)

from src.activities.workflow_activities import (
    update_workflow_state,
)


async def main():

    client = await get_temporal_client()

    workflow_runner = SandboxedWorkflowRunner(
        restrictions=(
            SandboxRestrictions.default
            .with_passthrough_modules(
                "src.activities.workflow_activities",
                "src.activities.borrower_activities",
            )
        )
    )

    worker = Worker(
        client,

        task_queue="borrower-task-queue",

        workflows=[
            BorrowerWorkflow
        ],

        activities=[
            attempt_contact,
            evaluate_risk,
            update_workflow_state,
        ],

        workflow_runner=workflow_runner,
    )

    print(
        "Temporal worker started..."
    )

    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())