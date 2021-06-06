import matplotlib.pyplot as plt
import numpy as np
from hpob_handler import HPOBHandler
from methods.botorch import GaussianProcess

valid_acquisitions = ["UCB", "EI", "PM", "PI", "qEI"]
trials = ["test0", "test1", "test2", "test3", "test4"]
perf_list = []
n_iterations = 20

hpob_hdlr = HPOBHandler(root_dir="../hpob-data/", mode="test")
search_space_id =  hpob_hdlr.get_search_spaces()[1]
dataset_id = hpob_hdlr.get_datasets(search_space_id)[1]

for acq_name in valid_acquisitions:
    perf_per_method = []
    for trial in trials:
        print("Using ", acq_name, " as acquisition function...")

        #define the HPO method
        method = GaussianProcess(acq_name=acq_name)

        #evaluate the HPO method
        perf = hpob_hdlr.evaluate(method, search_space_id = search_space_id, 
                                                dataset_id = dataset_id,
                                                trial = trial,
                                                n_iterations = n_iterations )
        perf_per_method.append(perf)

    plt.plot(np.array(perf_per_method).mean(axis=0))
plt.legend(valid_acquisitions)
plt.show()
