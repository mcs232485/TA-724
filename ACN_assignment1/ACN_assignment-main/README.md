# ACN_assignment

### 1. Why do you see a difference in webpage fetch times with short and large router buffers?

Ans:-  Average featch time for bb-20 is: 0.341259 and std Deviation is 0.092805, while for bb-100 the average fetch time is 0.925000 and std deviation is 0.275194.
  Its clear that for shorter buffer fetch time is less because of number of packets being queued up is less.

### 2. Bufferbloat can occur in other places such as your network interface card (NIC). Check the output of ifconfig eth0 on your VirtualBox VM. What is the (maximum) transmit queue length on the network interface reported by ifconfig? For this queue size, if you assume the queue drains at 100Mb/s, what is the maximum time a packet might wait in the queue before it leaves the NIC?

ANS:- For the mininet VM maximum transmit queue length is 1000, then for 1500 MTU,  the queue can hold max 1500*1000 = 15,00,000 Bytes total.
  if queue drains at 100Mb/s then maximum time a packet have to wait before it leaves the NIC  = 1500000*8/(100*10^6) = 0.12s.

### 3: How does the RTT reported by ping vary with the queue size? Describe the relation between the two.

Ans: From the grpah of rtt for 20 queue and 100 queue we can observe a direct correlation between the RTT and queue size , for a larger queue size RTT is higher than smaller queue size. so we can write, **RTT $\\approx$ (queue_delay + packet_delay + transmission dalay)**.
Also RTT increases as per congestion window increases and decreases with it as well.


### 4: Identify and describe two ways to mitigate the bufferbloat problem.
Ans: Simple way is to reduce the buffer size which will result in a lower wait time.
Also we can do **Active Queue Management** which can issue like bursty flow and global synchronisation of flow by dropping packets probabilistically. Also we can employ random packet dropping algorithm like **RED** to avoide Bufferbloat issues.

### 5. Describe how and why your results change when you re-run the emulation.
When we are re-running the emulation the packet traffic and noise in traffic will vary, also at host the download time for packets changes depending upon how empty the queue is , thus causing the variation in the cwnd and RTTs , also packet drops for the both emulation can be very different, thus causing  changes to the results in re-run of the emulations.
