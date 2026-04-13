# Pizzas in Peril

A 2D maze-based **Python game** built with `pygame` — play as a pizza navigating through city streets to deliver yourself to a house without hitting obstacles.

## Features

| Feature | Description |
|---------|-------------|
| **5 Unique Levels** | Each maze has a distinct layout and difficulty |
| **3 Difficulty Modes** | Easy, Medium, Hard — each increases the pizza's speed |
| **Collision Detection** | Walls stop you in your tracks; hitting a block resets position |
| **Sound Effects** | Doorbell on delivery, splat on collision, city ambience throughout |
| **Custom Graphics** | Pizza sprite, house, and maze images loaded from the `data/` folder |
| **Finish Detection** | Reach the house to trigger delivery success and advance |

## 🎮 How to Play

1. Launch the game — press **Space** to leave the intro screen
2. Use **Left / Right** arrows to cycle through levels 1–5
3. Press **1**, **2**, or **3** to select difficulty (Easy / Medium / Hard)
4. Press **Space** to start the selected level
5. Navigate with **Arrow Keys** or **WASD** to deliver the pizza to the house
6. Hit a wall → reset to start; reach the house → level complete!
7. Press **Escape** at any time to return to the level select screen

## Getting Started

### Prerequisites

- Python 3.x
- `pygame` library
- A `data/` folder at project root containing `audio/` and `images/` subdirectories

### Installation

```bash
# Clone the repo
git clone https://github.com/samadmd786/Pizzas_in_Peril.git
cd Pizzas_in_Peril

# Install dependencies
pip install pygame
```

### Running Locally

```bash
python main.py
```

## Controls

| Key | Action |
|-----|--------|
| `Space` | Start / confirm selection |
| `Arrow Keys` / `WASD` | Move the pizza |
| `Escape` | Return to level select |
| `1` / `2` / `3` | Select Easy / Medium / Hard difficulty |
| `Left` / `Right` | Cycle through levels |

## Project Structure

| File | Description |
|------|-------------|
| `main.py` | Game loop, input handling, rendering, and collision logic |
| `map_data.py` | Level definitions — maze images, start positions, finish zones, and block regions |
| `data/images/` | Sprites: pizza, house, game icon, intro/level select backgrounds |
| `data/audio/` | Sound effects: doorbell, splat, city ambience |

## Tech Stack

- **Language:** Python 3.x
- **Game Library:** [pygame](https://www.pygame.org/)
