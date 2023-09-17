
NAME : KUNDAN KUMAR
ENTRY NO : 2023JCS2560


1) Why do you see a difference in webpage fetch times with short and large router buffers?

Web download time Q=20:

Average: 0.397800
Standard Deviation: 0.134881

Web download time Q=100:

Average: 1.189381
Standard Deviation: 0.384681


This phenomenon arises from the size of the buffer in use. The exchange of packets between h1 and h2 saturates the buffer, it knows about packet loss when it reaches the full capacity of the buffer. As a result, larger buffer sizes leads to more time in filling the buffer, so the duration to occupy these buffers substantially increases. If we use smaller buffers then it facilitates more effective TCP congestion control mechanisms because the packet loss is known much faster in small buffer as compared to large buffer sizes.

2)Bufferbloat can occur in other places such as your network interface card (NIC). Check
the output of ifconfig eth0 on your VirtualBox VM. What is the (maximum) transmit
queue length on the network interface reported by ifconfig? For this queue size, if you
assume the queue drains at 100Mb/s, what is the maximum time a packet might wait in
the queue before it leaves the NIC?

We get  txqueuelen=1000 and MTU=1500.

Delay = (1000 packets x 1500 bytes x 8 bits)/(100Mbps) 
      = 0.12s delay

Output of ipconfig :  "Link encap:Ethernet  HWaddr 08:00:27:b0:68:bd  
          inet addr:10.0.2.15  Bcast:10.0.2.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:9105 errors:0 dropped:0 overruns:0 frame:0
          TX packets:8759 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:731364 (731.3 KB)  TX bytes:19556549 (19.5 MB)"

        

3)How does the RTT reported by ping vary with the queue size? Describe the relation
between the two.

RTT = Queue_Size * Packet_Delay

We can say that the round-trip time (RTT) indicated by a ping showing a direct proportional relation with the queue size. When the queue is enlarged, it has the capacity to accommodate a greater number of packets, consequently causing a direct rise in the overall RTT for each individual Packet_Delay.

4) Identify and describe two ways to mitigate the bufferbloat problem.


First approach is to reduce the buffer size. This adjustment will lead to shorter waiting time for the outcome.

Web download time Q=20:

Average: 0.397800
Standard Deviation: 0.134881

Web download time Q=100:

Average: 1.189381
Standard Deviation: 0.384681

Second strategy is to address bufferbloat  by implementing Active Queue Management (AQM). This technique will involve dropping of packets, which will help in  preventing the challenges linked with drop tail queues like sudden surges in data flows and the synchronization in data flows.

5)Describe how and why your results change when you re-run the emulation.

When we run the run.sh again the output changes like standard deviation, mean, fetch time, graphs of rtt,cwnd,queue etc because of the data flows timing is different and the data arrival timing of the queue changes so it affects the results at different times. When data comes in queue it will be different at different simulation because queue cannot predict the exact data coming because there may be changes due to noise, collision of packets , traffic of network etc.


