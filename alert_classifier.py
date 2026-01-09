def classify_alert(message):
    message = message.lower()

    important_keywords =[
        "down",
        "lost",
        "loss",
        "failure",
        "failed",
        "packet loss",
        "loss",
        "flap",
        "unreachable",
        "unable",
        "critical",
        "error",
        "unauthorized",
        "firewall rule mismatch",
        "power supply",
        "breach",
        "blocked",
        "denied",
        "block",
        "corrupted",
        "corrupt",
        "nak",
        "negative",
        "neg",
        "nack",
        "naks",
        "nacks",
        "error",
        "critical"
    ]

    warning_keywords = [
        "high",
        "low",
        "usage",
        "threshold",
        "exceeds",
        "exceeding",
        "exceeded",
        "slow",
        "degraded",
        "space",
        "reboot",
        "unexpected",
        "memory",
        "leakage",
        "leak",
        "warning"
    ]

    if "not found" in message:
        if any(k in message for k in ["bgp", "ospf", "dns", "router", "switch"]):
            return "CRITICAL"
        else:
            return "WARNING"

    for k in important_keywords:
        if k in message:
            return "CRITICAL"
        
    for k in warning_keywords:
        if k in message:
            return "WARNING"
    

    return "INFO"