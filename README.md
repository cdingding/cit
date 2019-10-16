# Installations

## 1. Clone this sampling package to local folder
* git clone https://github.com/cdingding/citSampler.git

## 2. Go to the folder of this package containing setup.py

## 3. Standard Build and Install
* python setup.py install

# Examples

## 1. Use the package in Jupyter notebook 
* Example import:
    * from citSampler import Constraint, sampler, testOutputVectors 
* Follow the ipython notebook to sample and test output vectors
    * Example file: citrine_sampling_and_test_example_Oct16_2019

## 2. Change directory to citSampler containing the executable file "Sampler"
* Go the folder containing the executable file, sampler, and the input files 
* Use as command line API
* ./sampler 'formulation.txt' 'formulation_sample_outputs.txt' 1000 
* the above notebook provides a way to test the output vectors

# Further improvement
* Optimized the sampling speed