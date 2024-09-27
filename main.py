import psutil
import matplotlib.pyplot as plt
import time

# Function to get CPU and Memory usage
def get_performance_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    return cpu_usage, memory_usage

# Lists to store metrics
cpu_usage_list = []
memory_usage_list = []

# Time duration for monitoring
monitor_duration = 60  # seconds
start_time = time.time()

while time.time() - start_time < monitor_duration:
    cpu, memory = get_performance_metrics()
    cpu_usage_list.append(cpu)
    memory_usage_list.append(memory)
    print(f"CPU Usage: {cpu}%, Memory Usage: {memory}%")
    time.sleep(1)  # Sleep for 1 second before the next reading

# Plotting the results
plt.figure(figsize=(12, 6))

# CPU Usage Plot
plt.subplot(2, 1, 1)
plt.plot(cpu_usage_list, label='CPU Usage (%)', color='blue')
plt.title('CPU Usage Over Time')
plt.xlabel('Time (seconds)')
plt.ylabel('CPU Usage (%)')
plt.ylim(0, 100)
plt.grid()
plt.legend()

# Memory Usage Plot
plt.subplot(2, 1, 2)
plt.plot(memory_usage_list, label='Memory Usage (%)', color='green')
plt.title('Memory Usage Over Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Memory Usage (%)')
plt.ylim(0, 100)
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
