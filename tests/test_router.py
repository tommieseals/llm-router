"Tests for LLM Router."

import pytest
from llm_router import Router
from llm_router.usage import UsageTracker
from llm_router.health import HealthChecker


class TestUsageTracker:
    def test_record_usage(self, tmp_path):
        tracker = UsageTracker(str(tmp_path / usage.json))
        tracker.record(ollama, tokens=100, cost=0)
        stats = tracker.get_stats()
        assert stats[providers][ollama][calls] == 1
        assert stats[providers][ollama][tokens] == 100

    def test_multiple_providers(self, tmp_path):
        tracker = UsageTracker(str(tmp_path / usage.json))
        tracker.record(ollama, tokens=100)
        tracker.record(nvidia, tokens=200, cost=0)
        stats = tracker.get_stats()
        assert len(stats[providers]) == 2


class TestHealthChecker:
    def test_is_healthy_default(self):
        checker = HealthChecker()
        # Unknown provider should be assumed healthy
        assert checker.is_healthy(unknown) is True

    def test_cache_result(self):
        checker = HealthChecker()
        checker._cache[test] = {healthy: False}
        assert checker.is_healthy(test) is False


class TestRouter:
    def test_init(self):
        router = Router()
        assert ollama in router.providers
        assert router.health is not None
        assert router.usage is not None
