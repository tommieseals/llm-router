"Health checking for providers."

from typing import Dict, Any

class HealthChecker:
    "Monitor provider health."
    
    def __init__(self):
        self._cache: Dict[str, Dict] = {}
    
    def check(self, provider_id: str, provider) -> Dict[str, Any]:
        "Check health of a provider."
        if hasattr(provider, health_check):
            result = provider.health_check()
        else:
            result = {healthy: True, note: No health check available}
        self._cache[provider_id] = result
        return result
    
    def is_healthy(self, provider_id: str) -> bool:
        "Check if provider is healthy (uses cache)."
        cached = self._cache.get(provider_id)
        if cached:
            return cached.get(healthy, False)
        return True  # Assume healthy if not checked
