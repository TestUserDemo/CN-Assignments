#Create a simulator object
set ns [new Simulator]

#Define different colors for data flow Blue-TCP Red-UDP
$ns color 1 Blue
$ns color 2 Red

#Open the nam trace file
set nf [open a.nam w]
$ns namtrace-all $nf
set nf1 [open b.tr w]
$ns trace-all $nf1

#Define a finish procedure
proc finish {} {
	global ns nf
	$ns flush-trace
	close $nf
	exec nam a.nam &
	exit 0
}

#Create 6 nodes
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]

#Create links between nodes
$ns duplex-link $n0 $n1 2Mp 10ms DropTail
$ns duplex-link $n0 $n3 1.3Mp 10ms DropTail
$ns duplex-link $n1 $n3 1.3Mp 10ms DropTail
$ns duplex-link $n1 $n2 1.3Mp 10ms DropTail
$ns duplex-link $n2 $n4 1.5Mp 10ms DropTail
$ns duplex-link $n1 $n4 1.7Mp 10ms DropTail
$ns duplex-link $n4 $n5 2.3Mp 10ms DropTail

$ns duplex-link-op $n0 $n3 orient right
$ns duplex-link-op $n0 $n1 orient right-up
$ns duplex-link-op $n3 $n1 orient left-up
$ns duplex-link-op $n1 $n2 orient right
$ns duplex-link-op $n2 $n4 orient left-up
$ns duplex-link-op $n4 $n5 orient up
$ns duplex-link-op $n1 $n4 orient right-up

#Monitor the queue
$ns duplex-link-op $n1 $n4 queuePos 0.5
$ns duplex-link-op $n1 $n2 queuePos 0.5

$ns queue-limit $n1 $n4 8
$ns queue-limit $n1 $n2 8

#Attach TCP agent from n0 to n5
set tcp1 [new Agent/TCP]
$tcp1 set class_ 2
$ns attach-agent $n0 $tcp1

set sink1 [new Agent/TCPSink]
$ns attach-agent $n5 $sink1

$ns connect $tcp1 $sink1
$tcp1 set fid_ 1

#Attach FTP over TCP
set ftp [new Application/FTP]
$ftp attach-agent $tcp1
$ftp set type_ FTP

$ns at 0.4 "$ftp start"
$ns at 2.4 "$ftp stop"
$ns at 2.5 "$ns detach-agent $n0 $tcp1 ; $ns detach-agent $n5 $sink1"

#Attach UDP agent from n0 to n4
set udp [new Agent/UDP]
$ns attach-agent $n0 $udp

set null [new Agent/Null]
$ns attach-agent $n4 $null

$ns connect $udp $null
$udp set fid_ 2

#Set up CBR for UDP connection
set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
$cbr set type_ CBR
$cbr set packet_size_ 1000
$cbr set rate 1Mb
$cbr set random_ true

$ns at 2.0 "$cbr start"
$ns at 3.6 "$cbr stop"
$ns at 4.0 "finish"

$ns run

