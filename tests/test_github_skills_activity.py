import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.app import activities


def test_github_skills_activity_exists():
    assert "GitHub Skills" in activities
    assert activities["GitHub Skills"]["max_participants"] > 0
