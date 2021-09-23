# CS4278-5478-Project-Materials

## Installation

`pip install -e gym-duckietown`

## Running the Simulation

We will evaluate your system on 5 [maps](./gym-duckietown/gym_duckietown/map_2021/) to compute the average accumulated
reward. A primary component of your grade is how fast the robot finds the goal, and the reward achieved. In particular,
take note below:

- Oscillating in place may generate a high score in the simulator, but will be penalized in our evaluation. This is a
  flaw in the Duckietown simulator.

To initialize the gym-duckietown environment, there are five arguments:

- `--map-name`: the name of the map
- `--seed`: random seed of the environment
- `--start-tile`: the starting tile. E.g. 1,13
- `--goal-tile`: the goal tile. E.g. 3,3
- `--max-steps`: the maximum run step. The default value is 1500. Do not change this default value when you generate the
  control files for submission.

Generate the control files for submission, similar to what you have done in Lab 1. A sample file for the python
environment is available [here](./example.py) together
with [sample control file](./map4_0_seed2_start_1,13_goal_3,3.txt). They illustrate how to add arguments and output your
controls to a file. To try our simple policy,

```
python example.py --map-name map4_0 --seed 2 --start-tile 1,13 --goal-tile 3,3
```

## System Input

The robot is only allowed to take in the following information as input:

- the starting tile
- the goal tile
- a map image
- image observation after each step
- rough robot position after each step

More details can be found in [example.py](./example.py).

## Submission

In map1, map2 and map3, the task is to follow the lane and achieve high reward. In map4 and map5, the task is to
navigate to the goal position and find the target duck as fast as possible. During the navigation, lane following is
also required.

The submission consists of two parts.

- The [goal.json](./goal.json) file has specified a set of map name, seed, start tile, goal tile. For each map, seed,
  start tile and goal tile, save your controls to a file named
  {map_name}\_seed{seed}\_start\_{start_tile\[0\]},{start_tile\[1\]}\_goal\_{goal\[0\]},{goal\[1\]}.txt. For example,
    - map4_0_seed2_start_1,13_goal_3,3.txt

  Check `example.py` for the format of the control file and make sure the submitted file is in correct format.


- Provide a short report (up to 2 pages, Times Roman 10 point) to describe your apporach. In particular, if you follow
  the classic modular system design approach, provide a system diagram and describe
    - how the system processes the visual input,
    - how the system processes the low level control,
    - how it determines the position with respect to the lane,
    - how it controls the vehicle.

  If you adopt a end-to-end neural network learning approach, provide the network architecture diagram. Explain your
  architecture choices, algorithms and modules, if any.

- Organize your submission folder **strictly** according to the following structure:

```
student_id.zip
|-- report.pdf
|-- code
|-- control_files
    |-- map4_0_seed2_start_1,13_goal_3,3.txt
    |-- ...
```

