#!/usr/bin/env python
import sys
import numpy as np
from constraints import Constraint

def sampler(input_file, output_file, n_result):
    ct = Constraint(input_file)
    ndim = ct.get_ndim()
    current_results = []

    while len(current_results) < n_result:
        res = np.random.random(ndim)
        res = (res/sum(res)*sum(ct.get_example())).round(5)
        if not ct.apply(res):
            continue
        current_results.append(res)
    print('example:',ct.get_example())
    print('res:',res)
    with open(output_file, 'a') as f:
        for l, el in enumerate(current_results):
            string = ' '.join(map(str, el))
            # for item in string:
            f.write(string)
            f.write('\n')
    return current_results

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    n_result = int(sys.argv[3:][0])
    print('input_file from sys.argv[3] :',n_result,type(n_result))

    # input_file = 'formulation.txt'
    # output_file = 'samples.txt'
    # n_result = 10
    sampler(input_file,output_file,n_result)
