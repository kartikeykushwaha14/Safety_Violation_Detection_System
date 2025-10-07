import json
from datetime import datetime

def log_violation(violations):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "violations": violations
    }
    try:
        with open("app/alerts.json", "r") as f:
            logs = json.load(f)
    except:
        logs = []
    logs.append(log_entry)
    with open("app/alerts.json", "w") as f:
        json.dump(logs, f, indent=4)
