# port_scanner


This is a simple port scanner using socket module to scan for open ports inside a network.



**Note: Please Don't scan ports for illegal purposes.**


**Description:**

The idea behind it to use socket module in python using a tcp handshake to each port to it's open or not.
You can use it to see which port is open or closed for a better understanding of security and network troubleshooting.




Usage: python3 portscanner.py <ip address> 
example:

```python3 portscanner.py 192.168.1.1 -p 22```

example using a port range:

```python3 portscanner 192.168.1.1 -p 21-80 ```

