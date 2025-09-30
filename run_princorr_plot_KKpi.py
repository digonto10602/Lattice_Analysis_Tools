#This file will run the plotter for each individual state 
#to generate a prin_corr plot using SUMMARY_GNU_DATA

import numpy as np 
import sys
import subprocess
import os.path
import prin_corr_plotter 

#File Directory
file_dir = "/home/digonto/Codes/Lattice_Analysis/KKpi.S2I2/"
#example = "/home/digonto/Codes/Lattice_Analysis/KKpi.S2I2/szscl21_24_128_b1p50_t_x4p300_um0p0840_sm0p0743_n1p265/fits_mhi/000_A1m/out/t0_10/prin_corrs/ord0/SUMMARY_GNU_DATA"
#Input 
L20_irrep_list = ["000_A1m","100_A2","110_A2","111_A2","200_A2"]

#L20 and L24 irrep list are the same 
L24_irrep_list = L20_irrep_list 

L20_ensemble_name = "szscl21_20_128_b1p50_t_x4p300_um0p0840_sm0p0743_n1p265"
L24_ensemble_name = 'szscl21_24_128_b1p50_t_x4p300_um0p0840_sm0p0743_n1p265'

L20_mass_directory = "szscl21_20_128_b1p50_t_x4p300_um0p0840_sm0p0743_n1p265_per/fits_mhi/"  #000_A1m/out/t0_9/prin_corrs/ord*

L24_mass_directory = "szscl21_24_128_b1p50_t_x4p300_um0p0840_sm0p0743_n1p265/fits_mhi/"

L20_t0_list = ["9", #000_A1m
               "10",#100_A2
               "13",#110_A2
               "8", #111_A2
               "10" #200_A2
              ]

L24_t0_list = ["12", #000_A1m
               "10",#100_A2
               "12",#110_A2
               "12", #111_A2
               "12" #200_A2
              ]

gap = " "
max_state = 30

#first do the L20 files 
for i in range(0, len(L20_irrep_list), 1):
    for j in range(0, max_state, 1):
        state_num = j 
        filename = (file_dir + L20_mass_directory + L20_irrep_list[i] 
                    + "/out/t0_" + L20_t0_list[i] + "/prin_corrs/ord" 
                    + str(state_num) + "/SUMMARY_GNU_DATA")
        if(os.path.exists(filename)):
            print("file found = ", filename)
            output_file = L20_ensemble_name + "_" + L20_irrep_list[i] + "_state_" + str(state_num) + ".pdf"
            prin_corr_plotter.plot_prin_corr_func(state_num, filename, output_file)

for i in range(0, len(L24_irrep_list), 1):
    for j in range(0, max_state, 1):
        state_num = j 
        filename = (file_dir + L24_mass_directory + L24_irrep_list[i] 
                    + "/out/t0_" + L24_t0_list[i] + "/prin_corrs/ord" 
                    + str(state_num) + "/SUMMARY_GNU_DATA")
        if(os.path.exists(filename)):
            print("file found = ", filename)
            output_file = L24_ensemble_name + "_" + L24_irrep_list[i] + "_state_" + str(state_num) + ".pdf"
            prin_corr_plotter.plot_prin_corr_func(state_num, filename, output_file)




        