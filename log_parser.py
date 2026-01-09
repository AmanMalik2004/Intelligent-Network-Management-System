import re
import pandas as pd

LOG_PATTERN = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(ERROR|WARNING|INFO)\s+(.*)"

def parse_logs(fp):
    tsp = []
    lvl = []
    msg = []

    with open(fp, "r") as f:
        for line in f:
            match = re.match(LOG_PATTERN, line)
            if match:
                tsp.append(match.group(1))
                lvl.append(match.group(2))
                msg.append(match.group(3))
    
    df = pd.DataFrame({
        "timestamp": tsp,
        "level": lvl,
        "message": msg
    })

    return df