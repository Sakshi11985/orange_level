

# SDN-Based Access Control System (POX + Mininet)

## Overview

This project implements a Software Defined Networking (SDN) based access control system using Mininet and the POX controller.

The system acts as a centralized firewall where the controller decides whether communication between hosts should be allowed or blocked.

---

## Objective

The objective of this project is to design and implement an SDN-based firewall that demonstrates centralized control, dynamic packet handling, and enforcement of access control policies.

---

## System Architecture

Components:

* Controller: POX
* Switch: Open vSwitch
* Hosts: h1, h2, h3

Communication Protocol:

* OpenFlow is used between switch and controller

---

## Topology

Single switch with 3 hosts:

* h1 → 10.0.0.1
* h2 → 10.0.0.2
* h3 → 10.0.0.3

---

## Policy

* Allow: h1 ↔ h2
* Block: h1 ↔ h3

---

## Working

1. Packet arrives at switch
2. If no rule exists, switch sends PacketIn to controller
3. Controller checks source and destination IP
4. Allowed traffic is forwarded
5. Blocked traffic is dropped

---

## ARP Handling

ARP packets are flooded to allow IP-to-MAC mapping. Without ARP, hosts cannot communicate.

---

## Execution

### Run Controller

cd ~/pox
./pox.py access_control

### Run Mininet

sudo mn -c
sudo mn --topo single,3 --controller=remote,ip=127.0.0.1

---

## Test Results

### Allowed

h1 ping h2 → SUCCESS

### Blocked

h1 ping h3 → FAIL

---

## Performance Analysis

### Latency

Measured using ping. Represents round-trip delay between hosts.

### Throughput

Measured using iperf. Represents data transfer rate in Mbps.

---

## Flow Table

Flow rules are not permanently installed. The controller processes packets dynamically, so the flow table may appear minimal.

---

## Validation

* h1 ↔ h2 works correctly
* h1 ↔ h3 is blocked

The system behaves according to the defined policy.

---

## Advantages

* Centralized control
* Easy to modify policies
* Flexible and programmable
* Real-time decision making

---

## Limitations

* Initial delay due to controller
* Controller dependency
* No persistent flow rules
* Limited scalability

---

## Future Improvements

* Install flow rules for better performance
* Add advanced access control policies
* Use advanced controllers like Ryu or ONOS
* Extend to larger networks

---

## Conclusion

This project demonstrates how SDN enables centralized and programmable network control. The controller successfully enforces access policies by allowing or blocking communication based on predefined rules.

---

## Screenshots

Available in screenshots folder:

* Controller running
* Allowed communication
* Blocked communication
* Flow table
* iperf result

---

## Use Cases

* Network security and firewall systems
* College or campus networks for restricted access
* Enterprise networks for protecting sensitive resources
* Data center traffic control
* Cloud networking and virtual machine communication control

---

## Traditional vs SDN Networking

### Traditional Networking

* Each device makes independent decisions
* Control plane and data plane are inside the same device
* Configuration is manual and device-specific
* Hard to manage and update
* Less flexible

### SDN Networking

* Central controller makes all decisions
* Control plane and data plane are separated
* Policies are applied centrally
* Easy to manage and modify
* Highly flexible and programmable

### Key Difference

Traditional networks are distributed, while SDN is centralized and controller-based.

---

## Author

Name: Sakshi P Shetty
Course: Bachelor of Engineering
Subject: Computer Networks
Year: 2026

