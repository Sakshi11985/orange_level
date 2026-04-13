# SDN-Based Access Control System (POX + Mininet)

## Objective
Implement an SDN-based firewall using Mininet and POX controller.

---

## Topology
Single switch with 3 hosts:
- h1 → 10.0.0.1
- h2 → 10.0.0.2
- h3 → 10.0.0.3

---

## Policy
- Allow: h1 ↔ h2
- Block: h1 ↔ h3

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

## Performance
iperf h1 h2

---

## Screenshots
Available in screenshots folder:
- Controller running
- Allowed communication
- Blocked communication
- Flow table
- iperf result

---

## Working
- ARP packets → Flooded  
- Allowed traffic → Forwarded  
- Blocked traffic → Dropped  

---

## Author
Sakshi P Shetty
