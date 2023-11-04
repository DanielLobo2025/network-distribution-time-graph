import matplotlib.pyplot as plt
import math

F = 2000  
us = 10  
uc = 1   
dc = 2   
num_clients = [1, 2, 4, 8, 16, 32, 64, 128, 256] 
def min_distribution_time_cs(N):
    return F / us + F / (uc * N) + F / dc
def min_distribution_time_p2p(N):
    return F / us + F / (uc * N) + F / (dc * N)
distribution_time_cs = []
distribution_time_p2p = []
for N in num_clients:
    distribution_time_cs.append(min_distribution_time_cs(N))
    distribution_time_p2p.append(min_distribution_time_p2p(N))
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
plt.subplots_adjust(wspace=0.4)
ax1.plot(num_clients, distribution_time_cs, marker='o', label='Client-Server')
ax1.set_xlabel('Number of Clients (N) - Daniel Lobo')
ax1.set_ylabel('Minimum Distribution Time (seconds)')
ax1.set_title('Minimum Distribution Time (Client-Server)')
ax1.set_yscale('linear')
ax2.plot(num_clients, distribution_time_p2p, marker='o', label='P2P')
ax2.set_xlabel('Number of Clients (N) - Daniel Lobo')
ax2.set_ylabel('Minimum Distribution Time (seconds)')
ax2.set_title('Minimum Distribution Time (P2P)')
ax2.set_yscale('linear')
plt.savefig('distribution_time_graph.png')
plt.show()
