#!/usr/bin/env python
# Script function: takes the condition-specific timing files generated by optimize
# and puts them into a single document, good for experimental presentation software

# USED FOR CARAT -- SPONT
import numpy as np
import sys
import pandas as pd
import argparse
import subprocess
import re

parser = argparse.ArgumentParser()
parser.add_argument('--run', action='store', type=int, help="run")
args=parser.parse_args()


# create function that reshapes the timing files
def timing_type8(data, num, run):
	df=pd.read_table(data, sep=' ', header=None)
	df=df.transpose()
	df=df.drop(8)
	run2 = run-1
	df=df.loc[:,[run2]]
	df=df.rename(index=str, columns={run2:"Onset Time"})
	df['Type']=num
	return df;

# load and reshape the timing files
p="./Pleasant.1D"
P = timing_type8(p,1,args.run)

n="./Neutral.1D"
N = timing_type8(n,2,args.run)

u="./Unpleasant.1D"
U=timing_type8(u,3,args.run)

# put all reshaped timing files together
times = [P, N, U]
result = pd.concat(times)
result = result.sort_values(by=['Onset Time'])
result = result.reset_index()
result = result.drop('index', axis=1)

# add a column with trial type names
trialtypes = {1: "Pleasant", 2: "Neutral", 3: "Unpleasant"}
result['TrialType'] = result['Type'].map(trialtypes)

# write to csv
result.to_csv('SPONT_timings_run' + str(args.run) + '.csv', index=False, sep=',')
