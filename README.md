# CS4278-5478-Project-Materials

This repository contains the evaluation materials for the CS4278/CS5478 project, autonomous lane following in gym-duckietown.

## Maps
We will evaluate your policy on 5 maps. Please find them [here](./maps/), then copy them into the map folder of your gym-duckietown environment, e.g.,
```
cp maps/* /path/to/your-gym-duckietown-repo/gym-duckietown/maps/
```

## Evaluation  

To initialize the Duckietown environment, there are three  arguments:
- `--map-name`: the name of the map
- `--seed`: random seed of the environment. 
- `--max-steps`: the maximum run step. The default value is 2000.  Do not change this default value when you generate the control files for submission.

Similar to Assignment 3, you  generate the control files for submission. Each map is associated with 10 random seed. Please test your policy with random seed **from 1 to 10**. You should generate control files for each random seed and map. In particular, there are several [invalid seeds](./invalid_seeds.json) for each map. Please skip them and test the rest.

A sample file for the environment is available [here](./example.py). We also include a [sample control file]('./../map5_seed11.txt). It illustrate how to add arguments, output your controls into a file. To try our simple policy, 
```
python example.py --map-name map5 --seed 11
```

We will compute the accumulated reward for each test case, and grade your project based on the average reward achieved. 

## Submission
The submission consists of two parts. 

1. For each map and each random seed, save your controls to a file named  "map{map_number}_seed{seed_number}.txt". For example, 
  - map1_seed5.txt
  - map2_seed1.txt
1. Provide a short report (up to 2 pages, Times Roman 10 point) to  describe your apporach. In particular, if you follow the classic modular system design approach, provide a system diagram and describe
  - how the system processes the visual input,
  - how it determines the position with respect to the lane,
  - how it controls the vehicle. 
If you adopt a end-to-end neural network learning approach, provide the network architecture diagram. Explain your architecture choices and modules, if any.

Organize your submission folder according to the following structure:
```
student_id.zip
|-- report.pdf
|-- code
|-- control_files
    |-- map*_seed*.txt
    |-- ...
```
