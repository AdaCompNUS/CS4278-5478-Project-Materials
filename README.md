# CS4278-5478-Project-Materials

## Installation

We recommend the use of [Anaconda](https://docs.anaconda.com/anaconda/install/index.html) to create a virtual environment for the project.  

Run the following commands to install the Dukietown simulator:
```
# create a clean environment with python 3.8
conda create --name duckietown python=3.8 
conda activate duckietown

# git clone our repo
git clone https://github.com/AdaCompNUS/CS4278-5478-Project-Materials.git
cd CS4278-5478-Project-Materials

# install
pip install -e gym-duckietown
```

To test the installation, you may manually control the robot:
```angular2html
cd gym-duckietown
python manual_control.py --map-name map1
```

## Running the Simulation

We will evaluate your system on 5 [maps](./gym-duckietown/gym_duckietown/map_2021/) together with [start and goal locations](testcases/task2.json) to compute the average accumulated
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
environment is available [here](./run.py) together
with [sample control file](./map4_0_seed2_start_1,13_goal_3,3.txt). They illustrate how to add arguments and output your
controls to a file. To try our simple policy,

```
python run.py --map-name map4_0 --seed 2 --start-tile 1,13 --goal-tile 3,3 --manual False
```

If you wish to manually control the agent, use `--manual True`. 

## System Input

The robot is only allowed to take in the following information as input:

- the starting tile
- the goal tile
- a map image
- the [goal images](./goal_images)
- image observation after each step
- coarse robot position after each step

## Testing

Test cases for the two submissions are in the `testcases` folder. For an example control file, see `map4_0_seed2_start_1,13_goal_3,3.txt`.
