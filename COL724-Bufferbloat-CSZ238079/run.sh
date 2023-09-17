#!/bin/bash
set -e

time=60
bwnet=10
delay=1

iperf_port=5001

modprobe tcp_probe
sysctl -w net.ipv4.tcp_no_metrics_save=1
sysctl -w "net.ipv4.tcp_mem=10240 87380 268435456"

for qsize in 20 100; do
    echo "Running simulation with qsize=$qsize"
    dir=bb-q$qsize
    mn -c > /dev/null 2>&1
    python bufferbloat.py --dir=$dir --time=$time --bw-net=$bwnet --delay=$delay --maxq=$qsize
    python plot_tcpprobe.py -f $dir/cwnd.txt -o $dir/cwnd-iperf.png -p $iperf_port
    python plot_queue.py -f $dir/q.txt -o $dir/q.png
    python plot_ping.py -f $dir/ping.txt -o $dir/rtt.png
    echo "Simulation done with qsize=$qsize"
done

echo "Simulation done, check the png files in bb-q20 and bb-q100 directories."