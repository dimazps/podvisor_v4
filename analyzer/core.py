import re

def analyze_logs(log_text):
    # Mock logic — replace with your actual regex/event correlation
    lines = log_text.splitlines()
    start_events = [line for line in lines if "START" in line]
    end_events = [line for line in lines if "END" in line]
    durations = []

    for start, end in zip(start_events, end_events):
        # Extract timestamps and compute duration (mocked)
        durations.append({"start": start, "end": end, "duration": "5s"})

    anomalies = [line for line in lines if "ERROR" in line or "FAIL" in line]

    return {
        "start_events": start_events,
        "end_events": end_events,
        "durations": durations,
        "anomalies": anomalies
    }