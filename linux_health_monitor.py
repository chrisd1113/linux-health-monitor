import psutil
import datetime
import json
import time

def get_system_metrics():
	metrics = {
		"timestamp": datetime.datetime.now().isoformat(),
		"cpu_percent": psutil.cpu_percent(interval=1),
		"memory_percent": psutil.virtual_memory().percent,
		"disk_percent": psutil.disk_usage("/").percent,
		"running_processes": len(psutil.pids()),
	}

	
	return metrics

if __name__ == "__main__":

	print("=== Linux Health Monitor Starting ===")
	for i in range(3):
		print(get_system_metrics())
		time.sleep(2)
	print("=== Monitoring Complete ===")


