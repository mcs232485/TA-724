Commands used:

sudo python bufferbloat_experiment.py --bw-host 1000 --bw-net 100 --delay 10 --dir experiment_results --time 20 --maxq 100 --cong reno

sudo python bufferbloat_experiment.py --bw-host 1000 --bw-net 100 --delay 10 --dir experiment_results --time 20 --maxq 20 --cong reno

sudo sh run.sh

Statistics:
100 Packet Queue:
 - Average Fetch Time: 0.01825 seconds
 - Standard Deviation: 0.0551258030932 seconds

20 Packet Queue:
 - Average Fetch Time: 0.001 seconds
 - Standard Deviation: 2.16840434497e-19 seconds

Questions:

1. The presence of a large router buffer size leads to TCP sending more packets than the network topology can handle. TCP relies on packet drops to gauge available bandwidth. Consequently, with a larger queue, incoming packets experience longer wait times, resulting in increased delays. As a result, the webpage fetch time is hampered by the significant queue filled with TCP packets that are arriving rapidly.

2. The maximum transmit queue length on the "eth0" network interface is 1000 packets. If this queue becomes full, it would hold 1,500,000 bytes (equivalent to 12,000,000 bits). Assuming it drains at a rate of 100 Mb/s, it would take approximately 0.12 seconds for the 1000th packet to exit the queue.

3. The Round-Trip Time (RTT) formula:
	 RTT(t, r) = Tp(r)*2 + L(t)/D
	where,
	t: time
	r: route
	Tp: propagation delay of a specific route
	L: length of the queue at a given moment, measured in bits
	D: rate of queue drainage, expressed in bits per second

4. Mitigating bufferbloat can involve using appropriately sized queues in network routers based on the network topology. Ideally, queues should be sized to maximize bandwidth usage. However, as observed, a queue size of 100 packets proved excessive. Striking a balance is crucial, avoiding excessively small queues that drop too many packets and underutilize bandwidth. Additionally, adapting the TCP congestion control algorithm to reduce reliance on dropped packets for slowdown can mitigate bufferbloat. Enhanced information about queue status and network topology would enable TCP to more effectively manage its bandwidth.

5. When re-running the emulation, the results might change due to factors such as varying network conditions, other activities on the host system, and inherent randomness in packet transmission and queue management. These factors can introduce variability in measurements and affect the observed behaviors of bufferbloat.
