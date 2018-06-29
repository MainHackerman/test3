import os
from testlib import *

def test0(test_val):
    CreateDataSet(test_val)
    results = GetResults()
    results = results[1:-1]
    cor_results = [4,4,4,3,1]
    phases = ['Slova','Mezery','Znaky','Souhlasky','Samohlasky']
    for i in range(5):
        if results[i][-1] == str(cor_results[i]):
            os.system('rlPass ' + phases[i] + ' correct')
        else:
            os.system('rlPass ' + phases[i] + ' not correct')
    ClearEnv()

test0_val = ['a b c d ']
test0(test0_val)

