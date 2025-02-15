#!/bin/bash

# reading the output file path from the configs
path=$(python3 -c "import json; print(json.load(open('config.json'))['output_path'])")


# Define arrays of parameter values
seeds=(1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20)
algs=("PPO" "A2C")
envs=("CartPole" "Acrobot")
ts=(0.03125 0.0625 0.125 0.25 0.5 1 2 4 8 16 32 64 128)
alphs=(0.1 0.01 0.001 0.0001 0.00001 0.000001)

# Create or overwrite the parameters file
output_file="parameters.txt"
> "$output_file"

# Generate parameter combinations for each seed
for seed in "${seeds[@]}"; do
  for alg in "${algs[@]}"; do
    for env in "${envs[@]}"; do
      for t in "${ts[@]}"; do
        for alph in "${alphs[@]}"; do
          # Append the parameter combination to the file
          echo "--seed $seed --alg $alg --env $env --t_multip $t --alph $alph --path $path " >> "$output_file"
        done
      done
    done
  done
done
