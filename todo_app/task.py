import uuid

class Task:
    # Weighted Average - Every task by it's priority, have different weights
    # It's a constant so we used upper-case form
    PRIORITY_WEIGHTS = {
        "High": 3,
        "Medium": 2,
        "Low": 1
    }

    def __init__(self, title: str, description: str, priority: str, status: str = "In process"):
        self.uuid = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.weight = self.PRIORITY_WEIGHTS.get(priority, 1)

    def to_dict(self) -> dict:
        return {
            "UUID": self.uuid,
            "Title": self.title,
            "Description": self.description,
            "Priority": self.priority,
            "Weight": self.weight,
            "Status": self.status
        }