from linux_health_monitor import get_system_metrics
import pytest

# Test that the function returns an output that is not None
def test_metrics_returned():
	result = get_system_metrics()
	assert result is not None, "Output is None"

# Test that keywords are in the returned function output
def test_keywords():
	keywords = ["timestamp", "cpu_percent", "memory_percent", "disk_percent", "running_processes"]
	result = get_system_metrics()
	assert all(keyword in result for keyword in keywords), "Keyword is missing from output"

# Test that percentages are between 0 and 100
def test_percentages():
	result = get_system_metrics()
	assert 0 <= result["cpu_percent"] <= 100, "cpu_percent out of bounds"
	assert 0 <= result["memory_percent"] <= 100, "memory_percent out of bounds"
	assert 0 <= result["disk_percent"] <= 100, "disk_percent out of bounds"

