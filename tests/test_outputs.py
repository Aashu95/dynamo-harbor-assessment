import json
import os
from collections import Counter

REPORT_PATH = "/workspace/report.json"
LOG_PATH = "/workspace/access.log"

def get_ground_truth():
    with open(LOG_PATH, "r") as f:
        lines = f.readlines()
    
    requests = len(lines)
    ips = set()
    paths = Counter()
    
    for line in lines:
        parts = line.split()
        if len(parts) > 6:
            ips.add(parts[0])
            paths[parts[6]] += 1
            
    top_path = paths.most_common(1)[0][0] if paths else ""
    return {"total_requests": requests, "unique_ips": len(ips), "top_path": top_path}

def load_agent_report():
    with open(REPORT_PATH, "r") as f:
        return json.load(f)

def test_criterion_1_file_exists_and_is_valid_json():
    assert os.path.exists(REPORT_PATH), f"{REPORT_PATH} was not found."
    try:
        load_agent_report()
    except json.JSONDecodeError:
        assert False, f"{REPORT_PATH} is not a valid JSON file."

def test_criterion_2_total_requests():
    truth = get_ground_truth()
    data = load_agent_report()
    assert "total_requests" in data, "The 'total_requests' key is missing."
    assert data["total_requests"] == truth["total_requests"], f"Expected {truth['total_requests']} total requests, got {data.get('total_requests')}"

def test_criterion_3_unique_ips():
    truth = get_ground_truth()
    data = load_agent_report()
    assert "unique_ips" in data, "The 'unique_ips' key is missing."
    assert data["unique_ips"] == truth["unique_ips"], f"Expected {truth['unique_ips']} unique IPs, got {data.get('unique_ips')}"

def test_criterion_4_top_path():
    truth = get_ground_truth()
    data = load_agent_report()
    assert "top_path" in data, "The 'top_path' key is missing."
    assert data["top_path"] == truth["top_path"], f"Expected top path to be '{truth['top_path']}', got '{data.get('top_path')}'"
