from temporalio import activity

from src.workflows.states import WorkflowState

@activity.defn
async def attempt_contact(
    borrower_id: str,
):
    print(
        f"attempting contact with borrower {borrower_id}"
    )

    return {
        "success": True,
        "next_state": WorkflowState.CONTACT_ATTEMPTED.value
    }


@activity.defn
async def evaluate_risk(
    borrower_id: str,
):
    print(
        f"evaluating borrower risk {borrower_id}"
    )

    return {
        "risk_score": 0.82,
        "recommended_state": WorkflowState.NEGOTIATION.value
    }