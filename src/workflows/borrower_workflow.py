from datetime import timedelta

from temporalio import workflow

from src.activities.borrower_activities import (
    attempt_contact,
)

from src.activities.workflow_activities import (
    update_workflow_state,
)

from src.workflows.states import WorkflowState

from temporalio.common import RetryPolicy

retry_policy = RetryPolicy(
    maximum_attempts=3,
)


@workflow.defn
class BorrowerWorkflow:

    def __init__(self):

        self.current_state = (
            WorkflowState.INITIATED.value
        )

        self.borrower_response = None

    @workflow.signal
    async def borrower_update(
        self,
        response: str,
    ):
        self.borrower_response = response

    @workflow.run
    async def run(
        self,
        borrower_id: str,
    ):

        workflow_id = workflow.info().workflow_id

        await workflow.execute_activity(
            update_workflow_state,

            args=[
                workflow_id,
                self.current_state,
            ],

            start_to_close_timeout=timedelta(
                seconds=10
            ),

            retry_policy=retry_policy
        )

        contact_result = await workflow.execute_activity(
            attempt_contact,

            borrower_id,

            start_to_close_timeout=timedelta(
                seconds=10
            ),

            retry_policy=retry_policy
        )

        self.current_state = contact_result[
            "next_state"
        ]

        await workflow.execute_activity(
            update_workflow_state,

            args=[
                workflow_id,
                self.current_state,
            ],

            start_to_close_timeout=timedelta(
                seconds=10
            ),

            retry_policy=retry_policy
        )

        await workflow.wait_condition(
            lambda: self.borrower_response
            is not None,

            timeout=timedelta(
                seconds=30
            ),
        )

        if self.borrower_response == "PROMISE_TO_PAY":

            self.current_state = (
                WorkflowState.PROMISE_TO_PAY.value
            )

        else:

            self.current_state = (
                WorkflowState.ESCALATED.value
            )

        await workflow.execute_activity(
            update_workflow_state,

            args=[
                workflow_id,
                self.current_state,
            ],

            start_to_close_timeout=timedelta(
                seconds=10
            ),
        )

        return {
            "borrower_id": borrower_id,
            "final_state": self.current_state,
        }