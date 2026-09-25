from temporalio import activity

from sqlalchemy import select

from src.db.database import AsyncSessionLocal

from src.models.workflow_instance import (
    WorkflowInstance,
)

from src.models.audit_log import (
    AuditLog,
)


@activity.defn
async def update_workflow_state(
    workflow_id: str,
    state: str,
) -> bool:

    async with AsyncSessionLocal() as session:

        result = await session.execute(
            select(WorkflowInstance)
            .where(
                WorkflowInstance.workflow_id
                == workflow_id
            )
        )

        workflow_instance = result.scalar_one()

        workflow_instance.current_state = state

        audit_log = AuditLog(
            action="STATE_TRANSITION",
            resource_type="WORKFLOW",
            resource_id=workflow_id,
            correlation_id=workflow_id,
            tenant_id=workflow_instance.tenant_id,
        )

        session.add(audit_log)

        await session.commit()

    return True