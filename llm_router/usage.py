"Usage tracking for API calls."

import json
from pathlib import Path
from datetime import date
from typing import Dict, Any

class UsageTracker:
    "Track API usage and costs."
    
    def __init__(self, storage_path: str = None):
        self.storage_path = Path(storage_path or Path.home() / .llm-router / usage.json)
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        self._stats = self._load()
    
    def _load(self) -> Dict:
        try:
            if self.storage_path.exists():
                data = json.loads(self.storage_path.read_text())
                if data.get(date) == str(date.today()):
                    return data
        except:
            pass
        return {date: str(date.today()), providers: {}, total_cost: 0.0}
    
    def _save(self):
        self.storage_path.write_text(json.dumps(self._stats, indent=2))
    
    def record(self, provider: str, tokens: int = 0, cost: float = 0):
        "Record a usage event."
        if provider not in self._stats[providers]:
            self._stats[providers][provider] = {calls: 0, tokens: 0, cost: 0.0}
        
        self._stats[providers][provider][calls] += 1
        self._stats[providers][provider][tokens] += tokens
        self._stats[providers][provider][cost] += cost
        self._stats[total_cost] += cost
        self._save()
    
    def get_stats(self) -> Dict[str, Any]:
        "Get current usage statistics."
        return self._stats
