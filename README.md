# server-monitoring
Sends data about the performance of the server

This repository is dependent on https://github.com/shubhamdipt/monitoring-dashboard .

## Requirements

* Python3

* There must be a device already added to the dashboard server with the server IP.


```
$pip install -r requirements.txt
```

Create a config file as follows:
```
[SERVER]
IP = <the current server IP>

[DASHBOARD_SERVER]
URL = <the url where data needs to be sent.>
```

## Usage

Initiate a cron job running the main.py script.
```
*/5 * * * * /root/server-monitoring/run.sh
```
