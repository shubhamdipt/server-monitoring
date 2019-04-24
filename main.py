import psutil
import configparser
import requests


CONFIG = configparser.ConfigParser()
CONFIG.read("config.ini")


def main():
    cpu = int(psutil.cpu_percent(interval=1))
    mem = int(psutil.virtual_memory().percent)
    disk = psutil.disk_usage('/').free
    r = requests.post(
        CONFIG["DASHBOARD_SERVER"]["URL"],
        data={
            "DEVICE_IP": CONFIG["SERVER"]["IP"],
            "CPU_USAGE": cpu,
            "MEMORY_USAGE": mem,
            "DISK_SPACE_LEFT": disk
        })
    print(r.text)


if __name__ == '__main__':
    main()