1. Webpage fetch request takes lesser time with smaller queue size. In case of larger queue size, TCP will double the congestion window, as there will be a 4ms delay for each packet, fetch time will be relatively longer for larger queue size.

2. Transmit queue length for my mininet is 1000. Using the info that 150kb (100 packets), we have that each packet is of 1500 bytes. So, in total, we have 1500*1000 = 1.5e6 bytes. 
Now 100Mb/s = 1.25e7 bytes/s, hence, it will take 0.12 second.

3. RTT is larger for 100 queue size. We know, RTT = queue_size * prop_delay, as prop_delay is fixed, larger the queue size, higher the delay.

4. (a) Some mechanism to drop packets with probabilty p. (maybe randomly or based on some analysis)
(b) By experimenting with different queue size, we can use the one with best RTT.

5. Time to fetch the webpage can vary. 