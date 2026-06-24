import json
from pathlib import Path

def test_criterion_1_valid_json():
    """Criterion 1: valid JSON file exists at /app/report.json."""
    path = Path('/app/report.json')
    assert path.exists()
    with open(path) as f:
        json.load(f)

def test_criterion_2_total_requests():
    """Criterion 2: total_requests value."""
    with open('/app/report.json') as f:
        data = json.load(f)
    assert data.get('total_requests') == 6

def test_criterion_3_unique_ips():
    """Criterion 3: unique_ips value."""
    with open('/app/report.json') as f:
        data = json.load(f)
    assert data.get('unique_ips') == 3

def test_criterion_4_top_path():
    """Criterion 4: top_path value."""
    with open('/app/report.json') as f:
        data = json.load(f)
    assert data.get('top_path') == '/index.html'
