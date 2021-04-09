# CS4278-5478-Project-Materials


## Evaluation  
We will evaluate your system on 5 [maps](./maps/). Copy the maps into the map folder of your gym-duckietown environment, e.g.,
```
cp maps/* /path/to/your-gym-duckietown-repo/gym-duckietown/maps/
```
Each map is associated with several [random seeds](./seeds.json). 

To initialize the gym-duckietown environment, there are three  arguments:
- `--map-name`: the name of the map
- `--seed`: random seed of the environment 
- `--max-steps`: the maximum run step. The default value is 2000.  Do not change this default value when you generate the control files for submission.

Similar to Assignment 3, you generate the control files for submission. 

A sample file for the python environment is available [here](./example.py). We also include a [sample control file](./map5_seed11.txt). It illustrates how to add arguments and output your controls to a file. To try our simple policy, 
```
python example.py --map-name map5 --seed 11
```

We will evaluate your system on these 5 maps and compute the accumulated reward for each test case. A primary component of your grade is the average reward achieved. 

### Stop Sign:
The agent must slow down below 0.15m/s if it is within 0.3m of a stop sign. The Duckiebot must recognize the sign from camera images.


## Submission
The submission consists of two parts. 

- For each map and each random seed, save your controls to a file named  "map{map_number}_seed{seed_number}.txt". For example, 
  - map1_seed5.txt
  - map2_seed1.txt
- Provide a short report (up to 2 pages, Times Roman 10 point) to  describe your apporach. In particular, if you follow the classic modular system design approach, provide a system diagram and describe
  - how the system processes the visual input,
  - how it determines the position with respect to the lane,
  - how it controls the vehicle. 

If you adopt a end-to-end neural network learning approach, provide the network architecture diagram. Explain your architecture choices, algorithms and modules, if any.

Organize your submission folder according to the following structure:
```
student_id.zip
|-- report.pdf
|-- code
|-- control_files
    |-- map*_seed*.txt
    |-- ...
```

