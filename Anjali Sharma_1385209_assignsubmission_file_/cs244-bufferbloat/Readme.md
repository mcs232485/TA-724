
1. Why do you see a difference in webpage fetch times with short and large router buffers?

Mean time for queue length 20 is 0.604055 whereas for queue length 100 it is 1.34475. Average fetch times increase with increas ein queue length.When queue size is large TCP will continuelly double congestion window and keep sending more packets, the fetch time will be longer when queue size is large. And when queue size is small TCP has to half its congestion window every time limit is reached and thus webpage fetch request can be more quickly sent.

2. Bufferbloat can occur in other places such as your network interface card (NIC). Check the output of ifconfig eth0 on your VirtualBox VM. What is the (maximum) transmit queue length on the network interface reported by ifconfig? For this queue size, if you assume the queue drains at 100Mb/s, what is the maximum time a packet might wait in the queue before it leaves the NIC?
 
The maximum transmit queue  lenght is 1000. Maximun waiting time is 1000 packets * 1500 Bytes / 100 Mb/s = 0.12 s

3. How does the RTT reported by ping vary with the queue size? Describe the relation between the two.

RTT gets larger when queue size is larger as seen from the graphs. As the propogation delay is constant
RTT = queue_size * propogation_delay

4. Identify and describe two ways to mitigate the bufferbloat problem.

The first way is to tune the max queue size, by limiting the buffer size under a limited bandwidth network could reduce the RTT. The second way is that we can use active queue management schemas such as RED to randomly drop packets in early stage with a probability parameter.

5. Describe how and why your results change when you re-run the emulation.
 When re run the mean times vary a little for both queue sizes. The changes are there due to difference in ping times every time it is emulated.