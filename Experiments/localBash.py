import subprocess
import datetime

# seeds=[9]
# algs=[ "PPO"]
# envs=["CartPole"] 
# ts=[0.5]
# alphs=[0.000001]
# count = 101
# for seed in seeds:
#     for alg in algs:
#         for env in envs:
#             for t in ts:
#                 for alph in alphs:
#                     path = f"./results"

#                     # Build the command to run experiment.py
#                     command = [
#                         "python", ".\\experiments\\experiments.py",
#                         f"--seed", str(seed),
#                         f"--alg", alg,
#                         f"--env", env,
#                         f"--t_multip", str(t),
#                         f"--alph", str(alph),
#                         f"--path", path,
#                         f"--task_ID", str(count)
#                     ]
#                     count +=1
#                     print("Running command:", " ".join(command), str(datetime.datetime.now()))
#                     subprocess.run(command)
#                     print("Command ended:", " ".join(command), str(datetime.datetime.now()))

with open("./experiments/left.txt", 'r') as f:
    configs = f.readlines()

count = 1
for config in configs:
    params = config.split("_")
    alg = params[0][3:]
    env = params[1][3:]
    seed = params[2][4:]
    t_multip = params[3][11:]
    alph = params[4][5:]
    path = "./Big_t/left"

    command = [
        "python", ".\\experiments\\experiments.py",
        f"--seed", seed,
        f"--alg", alg,
        f"--env", env,
        f"--t_multip", t_multip,
        f"--alph", alph,
        f"--path", path,
        f"--task_ID", str(count)
    ]
    count +=1
    print("Running command:", " ".join(command), str(datetime.datetime.now()))
    subprocess.run(command)
    print("Command ended:", " ".join(command), str(datetime.datetime.now()))

   
          
        

""" import subprocess
from multiprocessing import Pool, cpu_count
import datetime

# Define parameter values
seeds = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
algs = ["PPO", "DQN"]
envs = ["CartPole", "Acrobot"]
ts = [0.1, 0.2, 0.4, 0.6, 0.8, 0.10, 1.2]
alphs = [0.01, 0.02, 0.005]

# Define a function to execute experiments
def run_experiment(params):
    seed, alg, env, t, alph, task_id = params

    # Define the path
    path = f"./results"

    # Build the command to run experiment.py
    command = [
        "python", ".\\experiments\\experiments.py",
        f"--seed", str(seed),
        f"--alg", alg,
        f"--env", env,
        f"--t_multip", str(t),
        f"--alph", str(alph),
        f"--path", path,
        f"--task_ID", str(task_id)
    ]

    print("Running command:", " ".join(command), str(datetime.datetime.now()))
    subprocess.run(command)
    print("Command ended:", " ".join(command), str(datetime.datetime.now()))

# Prepare a list of all parameter combinations
def generate_params():
    task_id = 0
    params_list = []
    for seed in seeds:
        for alg in algs:
            for env in envs:
                for t in ts:
                    for alph in alphs:
                        params_list.append((seed, alg, env, t, alph, task_id))
                        task_id += 1
    return params_list

# Main parallel execution
if __name__ == "__main__":
    # Generate all parameter combinations
    params_list = generate_params()

    # Number of processes to run in parallel
    num_processes = min(cpu_count(), len(params_list))  # Use as many cores as available

    # Use multiprocessing Pool
    with Pool(processes=num_processes) as pool:
        pool.map(run_experiment, params_list)
 """