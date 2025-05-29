### 🧠 Agent-Based Model: Higher-Order Thinking in Evolutionary Games

This project implements an agent-based model that simulates how agents with different levels of strategic reasoning perform and evolve in competitive environments. The model explores evolutionary dynamics where cognitive complexity, environmental uncertainty, and payoff structures determine which strategies prevail over time.
For more details here the respective [Paper](BachelorThesis Tim Birkert.pdf)
---   

## 🔍 Overview

Agents of different reasoning depths — from level-0 (random) to higher-order thinkers (e.g., level-1, level-2) — repeatedly interact in randomly generated strategic games. Over multiple generations, their relative success determines reproduction and mutation dynamics.

The model provides insights into:
- Which types of agents are evolutionarily stable
- How payoff structures and environmental uncertainty shape strategic behavior
- When complexity becomes an advantage or a burden

---

## 🧪 Simulation Example Results

<div align="center">
  <img src="Bilder/II Poisson 1.0, N-C, N-S0.png" alt="" width="45%" />
  <img src="Bilder/Poisson 1.0, N-C, N-S0.png" alt="Simulation 2" width="45%" />
</div>
  
The [Plot file](functions/Plot.py) creates two graphics that illustrate the evolutionary dynamics of the simulated population

## 📁 Project Structure
Agent-based-model---Higher-order-thinking/  
│  
├── main.py # Main simulation script  
├── Game_creater.py # Constructs random strategic games that are solvable by IESDS  
├── Strategy.py # Defines agent strategies based on their and their assumed opponents level  
├── Population.py # Handles population dynamics and reproduction  
├── Poisson_distribution.py # Draws the first population from an Poisson-distribution  
├── Distribution_determening.py # Replicator dynamics  
├── Plot.py # Visualizes simulation results  
├── README.md # This file  
└── LICENSE # Project license (MIT)  

