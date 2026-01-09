import random
import pandas as pd
from datetime import datetime, timedelta

def generate_logs(count=1000):
    levels = ["ERROR", "WARNING", "INFO"]

    messages = [
        "Interface eth0 down on router1",
        "High CPU usage on switch2",
        "Backup completed successfully",
        "Packet loss detected on switch2",
        "User admin logged in",
        "Unauthorized login attempt detected",
        "Memory usage exceeds safe threshold",
        "Disk usage high on backup server",
        "Link flapping detected on switch5",
        "Firewall rule mismatch detected",
        "System heartbeat OK",
        "User guest logged out",
        "Unexpected reboot detected",
    ]

    data = {
        "timestamp": [],
        "level": [],
        "message": []
    }

    start_time = datetime.now() - timedelta(minutes=count)

    for i in range(count):
        ts = start_time + timedelta(seconds=i * 10)
        lvl = random.choice(levels)
        msg = random.choice(messages)

        data["timestamp"].append(ts.strftime("%Y-%m-%d %H:%M:%S"))
        data["level"].append(lvl)
        data["message"].append(msg)

    return pd.DataFrame(data)