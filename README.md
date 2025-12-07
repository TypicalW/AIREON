# AIREON  
**AI-Driven Reinforcement Learning for Energy Optimization in IoT Networks**

AIREON is a research-driven Python project that simulates an IoT sensor network and applies Reinforcement Learning (Q-learning) to optimize energy consumption and extend network lifetime. The project includes:

- A custom-built time-slotted IoT network environment  
- Baseline MAC models (Static Duty Cycle, CSMA-like logic, TDMA-like logic)  
- A Reinforcement Learning scheduler  
- Tools for experiment tracking, logging, and visualization  

This repository will evolve from a basic simulation engine into a full research-grade RL-based energy optimization system.

---

##  **Project Goals**
- Model an IoT network with realistic behavior:
  - Sleep/idle/tx states  
  - Packet generation  
  - Collisions  
  - Energy drain over time  
  - Queueing and reliability  

- Implement baseline MAC protocols for comparison:
  - Static duty cycle  
  - CSMA/CA-inspired random access  
  - TDMA-inspired scheduled access  

- Apply **Q-learning** to dynamically choose sleep/wake and transmission actions that reduce energy usage and maintain high network performance.

- Measure:
  - Network lifetime  
  - Packet Delivery Ratio (PDR)  
  - Total energy consumption  
  - Collisions  
  - Latency  

---


 
---

##  **Technologies Used**

### **Languages**
- Python 3.13  

### **Core Libraries**
- NumPy — vectorized operations, node states, random traffic  
- Pandas — logging experiment metrics  
- Matplotlib — graphs for energy, PDR, learning curves  
- tqdm — progress bars for long simulations  

(Additional RL libraries may be added later as needed.)

---


##  **Roadmap**

### **Phase 1 — Simulation Development**
- Build a simple environment to model energy + basic transmissions  
- Extend to full queueing, collisions, sleep/wake, and link reliability  
- Add metric tracking (PDR, energy, collisions, lifetime)

### **Phase 2 — Baseline Protocols**
- Static duty cycle  
- CSMA-like access  
- TDMA-like scheduling  

### **Phase 3 — Reinforcement Learning**
- Q-learning agent architecture  
- State and action space design  
- Reward shaping and training loop  
- Comparison against baselines  

### **Phase 4 — Results + Research Paper**
- Plotting tools  
- Reproducible experiments  
- Paper-ready graphs  
- Detailed evaluation

---

##  **Contributing**
This repository is part of an ongoing research project.  
Collaboration is welcome once the base framework is stable.

---

##  **License**
This project is licensed under the **MIT License**.

---

##  **Contact**
For questions or improvements:  ashmit1665@gmail.com or ayushashutoshkumar@gmail.com
Feel free to open an issue or reach out directly.
