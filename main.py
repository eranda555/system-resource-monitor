import psutil
import time
from datetime import datetime
from pathlib import Path

THRESHOLD = {
      "CPU": 80,
      "RAM": 85,
      "DISK": 90
}
INTERVAL = 5
LOG_FILE = Path("logs/system_monitor.log")

#log file is exists
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

#resussable warning
def check_warnings(resourse_name,ussage):
    threshold = THRESHOLD[resourse_name]
    if ussage > threshold:
        return f"WARNING : {resourse_name} USAGE HIGH"
    return None

def system_monitor():

 try:
  #cpu ussage
  cpu_usage = psutil.cpu_percent(interval=1)

  #ram
  ram = psutil.virtual_memory()
  ram_ussage = ram.percent

  #Disk uusage
  disk = psutil.disk_usage("/")
  disk_ussage = disk.percent

 except psutil.Error as error:
    print(f"Could not collect system information: {error}")
    return


#date and time
 timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

#monitor recording
 record = (
     f"{timestamp} | CPU USSAGE : {cpu_usage}% | "
     f"RAM USSAGE : {ram_ussage}% | DISK USSAGE : {disk_ussage}%"
 )

#displying result
 print("::::::::::::::::::::::SYSTEM RESOURCE MONITER::::::::::::::::::::::::::::\n")

 print(f"TIME          : {timestamp}")
 print(f"  CPU USSAGE  : {cpu_usage}%")
 print(f"  RAM USSAGE  : {ram_ussage}%")
 print(f"  DISK USSAGE : {disk_ussage}%\n")

 resource = [
    ("CPU",cpu_usage),
    ("RAM",ram_ussage),
    ("DISK",disk_ussage),
 ]

 Warnings = []

 for name,usage in resource:
    Warning = check_warnings(name,usage)
    if Warning:
       Warnings.append(Warning)
       print(Warning)
 try:
  #save the monitor records
  with LOG_FILE.open("a", encoding="utf-8") as file:
      file.write(record+"\n")
      for warning in Warnings:
         file.write(f"{timestamp} | {warning}\n")
  print("\nmonitor log saved!!!\n")

 except OSError as error:
    print(f"Could not save log: {error}")

    
 print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")


if __name__ == "__main__":
   try:
      print("system monitor stared!!! press ctr+c to stop")

      while True:
         system_monitor()
         time.sleep(INTERVAL)

   except KeyboardInterrupt:
      print("\n Monitor stop by user.")

