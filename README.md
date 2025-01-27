# port_scanner


This is a simple port scanner using socket module to scan for open ports inside a network.



**Note: Please Don't scan ports for illegal purposes.**


**Description:**

The idea behind it is to use socket module in python using a tcp handshake to scan each port to see if it's open or not.
You can use it to see which port is open or closed for a better understanding of security and network troubleshooting.




Usage: python3 portscanner.py "ip address" "max port"

example:

```python3 portscanner.py 192.168.1.1 1000```
It scans the first 1000 open ports

GoodLuck :)
