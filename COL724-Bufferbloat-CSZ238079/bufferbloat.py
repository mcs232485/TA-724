#!/usr/bin/python

import os
import math

from subprocess import Popen, PIPE
from time import sleep, time
from multiprocessing import Process
from argparse import ArgumentParser

from mininet.topo import Topo
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.net import Mininet
from mininet.clean import cleanup

from monitor import monitor_qlen

parser = ArgumentParser(description="Bufferbloat tests")
parser.add_argument('--bw-host', '-B', type=float, help="Bandwidth of host links (Mb/s)", default=1000)
parser.add_argument('--bw-net', '-b', type=float, help="Bandwidth of bottleneck (network) link (Mb/s)", required=True)
parser.add_argument('--delay', type=float, help="Link propagation delay (ms)", required=True)
parser.add_argument('--dir', '-d', help="Directory to store outputs", required=True)
parser.add_argument('--time', '-t', help="Duration (sec) to run the experiment", type=int, default=10)
parser.add_argument('--maxq', type=int, help="Max buffer size of network interface in packets", default=100)
parser.add_argument('--cong', help="Congestion control algorithm to use", default="reno") #Linux uses "--cong=cubic" by default
args = parser.parse_args()

class BBTopo(Topo):
    def build(self):
        self.addHost('h1')
        self.addHost('h2')
        self.addSwitch('s0')
        self.addLink('s0', 'h1', bw=args.bw_host, delay="%sms" % args.delay)
        self.addLink('s0', 'h2', bw=args.bw_host, delay="%sms" % args.delay)

def start_tcpprobe(outfile="cwnd.txt"):
    os.system("rmmod tcp_probe; modprobe tcp_probe full=1;")
    Popen("cat /proc/net/tcpprobe > %s/%s" % (args.dir, outfile), shell=True)
    print("tcpprobe started.")

def stop_tcpprobe():
    try:
        Popen("killall -9 cat", shell=True).wait()
        print("tcpprobe stopped.")
    except:
        print("Error: Can't stop tcpprobe.")

def start_qmon(iface, interval_sec=0.1, outfile="q.txt"):
    monitor = Process(target=monitor_qlen, args=(iface, interval_sec, outfile))
    monitor.start()
    print("qmon started.")
    return monitor

def start_iperf(net):
    net.get('h2').popen("iperf -s -w 16m")
    net.get('h1').popen("iperf -c {} -t {}".format(net.get('h2').IP(), args.time), shell=True, stdout=PIPE, stderr=PIPE)
    print("iperf started.")

def start_webserver(net):
    h1 = net.get('h1')
    proc = h1.popen("python http/webserver.py", shell=True)
    print("webserver started.")
    return [proc]

def start_ping(net):
    net.get('h1').popen("ping -i 0.1 -w %s %s >> %s/ping.txt &" % (args.time, net.get('h2').IP(), args.dir), shell=True)
    print("ping started.")

def bufferbloat():
    if not os.path.exists(args.dir):
        os.makedirs(args.dir)
    os.system("sysctl -w net.ipv4.tcp_congestion_control=%s" % args.cong)
    try:
        cleanup()
    except:
        print("Error while cleaning up mininet.")
    net = Mininet(topo=BBTopo(), host=CPULimitedHost, link=TCLink)
    net.start()

    start_tcpprobe("cwnd.txt")
    ping_process = Process(target=start_ping, args=(net,))
    ping_process.start()
    qmon = start_qmon(iface='s0-eth1', outfile='%s/q.txt' % (args.dir))
    start_iperf(net)
    start_webserver(net)

    start_time = time()
    fetch_times = []
    while True:
        for _ in range(3):
            fetch_time = float(net.get('h1').cmd("curl -o /dev/null -s -w %{time_total} http://" + net.get('h1').IP() + ":80/http/index.html"))
            fetch_times.append(fetch_time)
            sleep(5)
        now = time()
        delta = now - start_time
        if delta > args.time:
            break

    avg = sum(fetch_times) / len(fetch_times)
    sd = math.sqrt(sum((x - avg) ** 2 for x in fetch_times) / len(fetch_times))
    print("Average Fetch Time(second):", avg, "Standard Deviation(second):", sd)

    stop_tcpprobe()
    try:
        qmon.terminate()
    except:
        print("Error: Can't stop tcpprobe.")
    ping_process.join()
    try:
        net.stop()
    except:
        print("Error: Can't stop mininet.")
    try:
        Popen("pgrep -f webserver.py | xargs kill -9", shell=True).wait()
    except:
        print("Error: Can't stop webserver.")

if __name__ == "__main__":
    bufferbloat()