Q1. Why do you see a difference in webpage fetch times with short and large router buffers?
	
As we can see from the plotted graphs, the average fetch times for the short router buffer is shorter than that of the long router buffer. This is likely 		due to excess buffering of packets in the queue. Because the short router buffer will have a shorter queue, the number of packets queued is less resulting in a shorter wait time.

----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
Q2. Bufferbloat can occur in other places such as your network interface card (NIC). Check the output of ifconfig eth0 on your VirtualBox VM. What is the (maximum) transmit queue length on the network interface reported by ifconfig? For this queue size, if you assume the queue drains at 100Mb/s, what is the maximum time a packet might wait in the queue before it leaves the NIC?

The output of the ifconfig for my NIC is as follows:

wlp0s20f3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.5  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 2401:4900:1c53:226f:bb17:2217:ac45:98fb  prefixlen 64  scopeid 0x0<global>
        inet6 fe80::8c0:d2e6:97e5:84d  prefixlen 64  scopeid 0x20<link>
        inet6 2401:4900:1c53:226f:a7a7:ea6f:6afb:babf  prefixlen 64  scopeid 0x0<global>
        inet6 2401:4900:1c53:226f:7bd7:19d7:9d91:37c0  prefixlen 64  scopeid 0x0<global>
        ether 20:c1:9b:b8:cb:6c  txqueuelen 1000  (Ethernet)
        RX packets 5052761  bytes 6214010784 (6.2 GB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 1581337  bytes 440730654 (440.7 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

This means that when the queue is full, it would hold 1,500,000 (1000*1500) byte packets. Therefore, the maximum time a packet would have to wait before it leaves the NIC is: 1000 * 1500 * 8 * 1/(100*10^6) = 0.12s

------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
Q3. How does the RTT reported by ping vary with the queue size? Describe the relation between the two.

Looking at the graphs, RTT is directly proportional to queue size. Therefore, we can write this as: RTT = k * qsize.

------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------

Q4. Identify and describe two ways to mitigate the bufferbloat problem.

The first way is to simply reduce the queue size by having a shorter router buffer. The second way is to somehow tweak the flow of traffic such that we are limiting the rate of traffic although at a cost of lower bandwidth.

------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------

Q5. Describe how and why your results change when you re-run the emulation.

The discrepencies between two emulations can be due to a larger time period for which the average is calculated, we can reduce the sampling time and aim for an accurate trigger time for samples between two simulations. Another possible reason can be due to the very large TCP window of 16m in the code, which causes unpredictable spike in the starting of the simulation.

