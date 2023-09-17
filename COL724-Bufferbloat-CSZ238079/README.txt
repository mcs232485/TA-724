Q1: Why do you see a difference in webpage fetch times with short and large router buffers?
Ans: This is due to the Bufferbloat. With larger buffer size, during congestion router absorbs more packets and causes more delay.
But with smaller buffer size, router drops more packets during congestion and doesn't cause more queuing delay.

Q2: Bufferbloat can occur in other places such as your network interface card (NIC). Check the output of ifconfig eth0 on your VirtualBox VM. What is the (maximum) transmit queue length on the network interface reported by ifconfig? For this queue size, if you assume the queue drains at 100Mb/s, what is the maximum time a packet might wait in the queue before it leaves the NIC?
Ans: `ifconfig` command doesn't provided the desired value of "txqueuelen". `ethtool -g <intf-name>` gives this value as 4096.
Drain Rate = 10^6 * 100 bits/s, MTU = 1500, Maximum queuing delay = 4096 * 1500 / (10^6 * 100) = 0.06144 seconds

3. How does the RTT reported by ping vary with the queue size? Describe the relation between the two.
Ans: The RTT increases for qsize=100, this is due to Bufferbloat: with large qsize, lots of packets get queued up during the time of congestion and this increases the queuing delay and hence RTT.

4. Identify and describe two ways to mitigate the bufferbloat problem.
Ans: (a) Active Queue Management (AQM): To manage the buffer queues actively to ensure that they don't become excessively large. Controlled Delay (CoDel), Random Early Detection (RED), Fair Queuing CoDel are some of the AQM techniques used popularly.
(b) Quality of Service (QoS): To ensure different delays based on priority of the flow.

5. Describe how and why your results change when you re-run the emulation.
Ans: Initial run of the simulation takes comparatively longer time than the subsequent runs, this is due to various factors during the simulation, but primarily the system load and caching of required libraries. Also, there was slight decrease in the fetch_time of index.html, this too is due to caching.