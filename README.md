# Powder Simulator

A simple 2D particle simulation in Python using Pygame. Simulates different materials like sand, water, and other elements interacting in a grid.

## Features

* Grid-based simulation
* Multiple element types (sand, water, etc.)
* Gravity and simple physics
* Real-time user interaction (place/remove elements with mouse)
* Toggle modes (e.g., delete elements with `D` key)

## Requirements

* Python 3.10+
* Pygame

Install dependencies with:

```bash
pip install pygame
```

## How to Run

```bash
python Main.py
```

## Controls

* **Left click**: place current element
* **Hold left click**: continuously place elements
* **D key**: toggle delete mode
* **1 key**: assign sand element
* **2 key**: assign metal element
* **3 key**: assign water element
* **4 key**: assign stone element

## Project Structure

```
PowderSimulator/
├─ Main.py           # Main loop
├─ Grid.py           # Grid management
├─ config.py         # constants management
├─ elements/         # Element classes
│  └─ Element.py
│  └─ Metal.py
│  └─ Sand.py
│  └─ Stone.py
│  └─ Water.py
└─ README.md
```

## License

MIT License
