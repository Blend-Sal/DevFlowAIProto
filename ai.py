from datetime import date, datetime
from typing import List
from model import TaskInput, PrioritizedTask

HIGH_RISK_KEYWORDS = ["bug", "crash", "security", "failure", "error"]
LOW_RISK_KEYWORDS = ["refactor", "cleanup", "documentation", "style"]


def days_until(deadline_str: str) -> int:
    deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
    return max((deadline - date.today()).days, 0)


def risk_score(text: str) -> int:
    text = text.lower()
    if any(k in text for k in HIGH_RISK_KEYWORDS):
        return 5
    if any(k in text for k in LOW_RISK_KEYWORDS):
        return 1
    return 3


def prioritize_tasks(tasks: List[TaskInput], weights=None) -> List[PrioritizedTask]:
    if weights is None:
        weights = {
            "deadline": 0.4,
            "importance": 0.3,
            "risk": 0.2,
            "effort": -0.1
        }

    result = []

    for t in tasks:
        d = days_until(t.deadline)
        deadline_score = max(0, 5 - d)
        risk = risk_score(t.description)

        breakdown = {
            "deadline": weights["deadline"] * deadline_score,
            "importance": weights["importance"] * t.importance,
            "risk": weights["risk"] * risk,
            "effort": weights["effort"] * t.effort
        }

        score = round(sum(breakdown.values()), 2)

        reason = (
            f"Deadline in {d} days | "
            f"Importance {t.importance} | "
            f"Risk {risk}"
        )

        result.append(
            PrioritizedTask(
                **t.dict(),
                score=score,
                breakdown=breakdown,
                reason=reason
            )
        )

    return sorted(result, key=lambda x: x.score, reverse=True)
