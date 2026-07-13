import psutil
import datetime
def check_cpu():
   result = psutil.cpu_percent(interval=1)
   return result

def check_memory():
    result = psutil.virtual_memory().percent
    return result

def check_disk():
    result = psutil.disk_usage('/').percent
    return result

def health_report():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu = check_cpu()
    memory = check_memory()
    disk = check_disk()
    print ("System Health Report")
    print ("--------------------")
    print(f"Report Generated: {timestamp}")
    print (f"CPU Usage: {cpu}%")
    print (f"Memory Usage: {memory}%")
    print (f"Disk Usage: {disk}%")
    with open ("health_log.txt", "a") as log:
        log.write(f"\n{timestamp}\n")
        log.write(f"CPU: {cpu}%\n")
        log.write(f"Memory: {memory}%\n")
        log.write(f"Disk: {disk}%\n")
        log.write("---------------------")
try:
   health_report()
except ImportError:
   print("Error: psutil library not installed. Run: pip3 install psutil")
except Exception as e:
   print(f"An error has occured: {e}")
    
                
