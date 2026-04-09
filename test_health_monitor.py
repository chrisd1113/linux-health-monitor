from linux_health_monitor import get_system_metrics
import pytest

def test_metrics_returned():
	result = get_system_metrics()
	assert result is not None, "Output is None"

def test_keywords():
	keywords = ["timestamp", "cpu_percent", "memory_percent", "disk_percent", "running_processes"]
	result = get_system_metrics()
	assert all(keyword in result for keyword in keywords), "Keyword is missing from output"

def test_percentages():
	result = get_system_metrics()
	assert 0 <= result["cpu_percent"] <= 100, "cpu_percent out of bounds"
	assert 0 <= result["memory_percent"] <= 100, "memory_percent out of bounds"
	assert 0 <= result["disk_percent"] <= 100, "disk_percent out of bounds"

