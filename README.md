# ELF-1 Simulation

MuJoCo simulation environment for the **ELF-1 humanoid robot**.

ELF-1 is a small humanoid robot designed for:

- robotics learning
- control experiments
- educational robotics
- rapid prototyping of robot behaviors

The simulation is based on **MuJoCo** and allows testing robot kinematics, control strategies, and motion experiments before building the physical robot.

---

# Robot Overview

ELF-1 currently contains:

**Arms**

- shoulder pitch (1 DOF)
- shoulder roll (1 DOF)

**Legs**

- hip (1 DOF)
- knee (1 DOF)

Total actuated joints:

```
8 DOF
```

The robot base uses a **free joint**, allowing full floating-base simulation.

---

# Repository Structure

```
elf-1-simulation
│
├ models
│   └ elf1_mini_biped.xml
│
├ scripts
│   └ elf1_arm_lift_3.py
│
├ controllers
│
└ README.md
```

| Folder | Description |
|------|------|
| models | MuJoCo robot definitions |
| scripts | simple simulation experiments |
| controllers | robot control algorithms |
| experiments | motion and behavior tests |

---

# Requirements

Install MuJoCo Python bindings:

```
pip install mujoco
```

Python version used for this project:
Python 3.9.25

The simulation was tested with Python 3.9.25. Other Python 3.x versions may also work.

# Run the Simulation

Example experiment: **arm movement**

```
python scripts/elf1_arm_lift_3.py
```

This will open the MuJoCo viewer and move the left arm using the two shoulder DOF.

---

# Robot Model

The robot is defined in:

```
models/elf1_mini_biped.xml
```

The model contains:

- torso
- head
- two legs
- two arms
- motors for each joint
- simple contact feet

The geometry is intentionally simple to keep simulation stable and fast.

---

# Development Roadmap

Planned simulation experiments:

- arm motion experiments
- balance controller
- simple walking gait
- inverse kinematics
- reinforcement learning experiments

---

# Related Repositories

This repository is part of the **ELF Robotics project**.

| Repository | Purpose |
|------|------|
| elf-hardware | CAD and electronics |
| elf-kids-lab | educational robotics experiments |

---

# License

MIT License
