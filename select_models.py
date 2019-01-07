from model_information import *
from os import listdir
import shutil
from os.path import isfile, join
import sys
sys.setrecursionlimit(10000) # For larger Problems

def load_pyomo_model(problem_name):
    testinstance = importlib.import_module(problem_name)
    return testinstance.m

def read_test_instances(path):
    '''Read test instance Data '''
    files = listdir(path)
    suffix = ".py"
    pyfiles = [file for file in files if file.endswith(suffix)]
    testset = [file[:-3] for file in pyfiles]
    return testset

def copy_files(instance_list ,from_path, to_path):
    for f in instance_list:
        f = from_path + "\\"+ f + ".py"
        shutil.copy(f, to_path)

path = r"Z:\hg2412\Research\minlplib_quad_pyomo"
sys.path.append(path)
#instances = read_test_instances(path)
#print(len(instances))
#testset = []
#for instance in instances:
#    m = load_pyomo_model(instance)
#    print('testing ' + instance )
#    if not contains_eq_constrs_on_int_vars(m):
#        print('add ' + instance + " to testset" )
#        testset.append(instance)
#print(testset)

testset = ['autocorr_bern20-03', 'autocorr_bern25-03', 'blend029', 'blend146', 'blend480', 'blend531', 'blend718', 'blend721', 'blend852', 'crudeoil_lee1_05', 'crudeoil_lee1_06', 'crudeoil_lee1_07', 'crudeoil_lee1_08', 'crudeoil_lee1_09', 'crudeoil_lee1_10', 'crudeoil_lee2_05', 'crudeoil_lee2_06', 'crudeoil_lee2_07', 'crudeoil_lee2_08', 'crudeoil_lee2_09', 'crudeoil_lee2_10', 'crudeoil_lee3_05', 'crudeoil_lee3_06', 'crudeoil_lee3_07', 'crudeoil_lee3_08', 'crudeoil_lee3_09', 'crudeoil_lee3_10', 'crudeoil_lee4_05', 'crudeoil_lee4_06', 'crudeoil_lee4_07', 'crudeoil_lee4_08', 'crudeoil_lee4_09', 'crudeoil_lee4_10', 'crudeoil_li02', 'crudeoil_li03', 'crudeoil_li06', 'crudeoil_li11', 'crudeoil_li21', 'cvxnonsep_normcon20r', 'cvxnonsep_normcon30r', 'cvxnonsep_normcon40r', 'edgecross10-010', 'edgecross10-020', 'edgecross10-030', 'edgecross10-040', 'edgecross10-050', 'edgecross10-060', 'edgecross10-070', 'edgecross10-080', 'edgecross10-090', 'edgecross14-019', 'edgecross14-039', 'edgecross14-058', 'edgecross14-078', 'edgecross14-098', 'edgecross14-117', 'edgecross14-137', 'edgecross14-156', 'edgecross14-176', 'edgecross20-040', 'edgecross20-080', 'edgecross22-048', 'edgecross22-096', 'edgecross24-057', 'edgecross24-115', 'ex1223a', 'ex1263a', 'ex1264a', 'ex1265a', 'ex1266a', 'ex4', 'faclay20h', 'faclay25', 'faclay30', 'faclay30h', 'faclay33', 'faclay35', 'gabriel01', 'gabriel02', 'gabriel04', 'gabriel05', 'gabriel06', 'gabriel07', 'gabriel08', 'gabriel09', 'genpooling_lee1', 'genpooling_lee2', 'genpooling_meyer04', 'genpooling_meyer10', 'genpooling_meyer15', 'hydroenergy1', 'hydroenergy2', 'hydroenergy3', 'ndcc12', 'ndcc12persp', 'ndcc13', 'ndcc13persp', 'ndcc14', 'ndcc14persp', 'ndcc15', 'ndcc15persp', 'ndcc16', 'ndcc16persp', 'nous1', 'nous2', 'portfol_classical050_1', 'portfol_classical200_2', 'portfol_robust050_34', 'portfol_robust100_09', 'portfol_robust200_03', 'portfol_shortfall050_68', 'portfol_shortfall100_04', 'portfol_shortfall200_05', 'ringpack_10_1', 'ringpack_10_2', 'ringpack_20_1', 'ringpack_20_2', 'ringpack_20_3', 'ringpack_30_1', 'ringpack_30_2', 'smallinvDAXr1b010-011', 'smallinvDAXr1b020-022', 'smallinvDAXr1b050-055', 'smallinvDAXr1b100-110', 'smallinvDAXr1b150-165', 'smallinvDAXr1b200-220', 'smallinvDAXr2b010-011', 'smallinvDAXr2b020-022', 'smallinvDAXr2b050-055', 'smallinvDAXr2b100-110', 'smallinvDAXr2b150-165', 'smallinvDAXr2b200-220', 'smallinvDAXr3b010-011', 'smallinvDAXr3b020-022', 'smallinvDAXr3b050-055', 'smallinvDAXr3b100-110', 'smallinvDAXr3b150-165', 'smallinvDAXr3b200-220', 'smallinvDAXr4b010-011', 'smallinvDAXr4b020-022', 'smallinvDAXr4b050-055', 'smallinvDAXr4b100-110', 'smallinvDAXr4b150-165', 'smallinvDAXr4b200-220', 'smallinvDAXr5b010-011', 'smallinvDAXr5b020-022', 'smallinvDAXr5b050-055', 'smallinvDAXr5b100-110', 'smallinvDAXr5b150-165', 'smallinvDAXr5b200-220', 'smallinvSNPr1b010-011', 'smallinvSNPr1b020-022', 'smallinvSNPr1b050-055', 'smallinvSNPr1b100-110', 'smallinvSNPr1b150-165', 'smallinvSNPr1b200-220', 'smallinvSNPr2b010-011', 'smallinvSNPr2b020-022', 'smallinvSNPr2b050-055', 'smallinvSNPr2b100-110', 'smallinvSNPr2b150-165', 'smallinvSNPr2b200-220', 'smallinvSNPr3b010-011', 'smallinvSNPr3b020-022', 'smallinvSNPr3b050-055', 'smallinvSNPr3b100-110', 'smallinvSNPr3b150-165', 'smallinvSNPr3b200-220', 'smallinvSNPr4b010-011', 'smallinvSNPr4b020-022', 'smallinvSNPr4b050-055', 'smallinvSNPr4b100-110', 'smallinvSNPr4b150-165', 'smallinvSNPr4b200-220', 'smallinvSNPr5b010-011', 'smallinvSNPr5b020-022', 'smallinvSNPr5b050-055', 'smallinvSNPr5b100-110', 'smallinvSNPr5b150-165', 'smallinvSNPr5b200-220', 'sonet17v4', 'sonet18v6', 'sonet19v5', 'sonet20v6', 'sonet21v6', 'sonet22v4', 'sonet23v6', 'sonet24v2', 'sonet25v5', 'sporttournament06', 'sporttournament08', 'sporttournament10', 'sporttournament12', 'sporttournament14', 'sporttournament16', 'sporttournament18', 'sporttournament20', 'sporttournament22', 'sporttournament24', 'sporttournament26', 'sporttournament28', 'sporttournament30', 'sporttournament32', 'sporttournament34', 'sporttournament36', 'sporttournament38', 'sporttournament40', 'sporttournament42', 'sporttournament44', 'sporttournament46', 'sporttournament48', 'sporttournament50', 'squfl010-025persp', 'squfl010-040persp', 'squfl010-080persp', 'squfl015-060persp', 'squfl015-080persp', 'squfl020-040persp', 'squfl020-050persp', 'squfl020-150persp', 'squfl025-025persp', 'squfl025-030persp', 'squfl025-040persp', 'squfl030-100persp', 'squfl030-150persp', 'squfl040-080persp', 'st_e13', 'supplychain', 'tln12', 'tln2', 'tln4', 'tln5', 'tln6', 'tln7', 'tloss', 'tltr', 'topopt-zhou-rozvany_75']

to_path = r"Z:\hg2412\Research\01_FeasibleRoundingApproaches\04_numeric_granularity\testbed"

copy_files(testset, path, to_path)