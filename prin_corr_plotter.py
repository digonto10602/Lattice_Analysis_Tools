#This serves as a header file for run_princorr_plot
#has the functions that does the actual plot 

import numpy as np 
import matplotlib as mpl 
import matplotlib.pyplot as plt 
import scipy.interpolate
from mpl_toolkits.axes_grid1 import make_axes_locatable
import os.path
from scipy.optimize import curve_fit
import scipy.interpolate
import sys #important for using argv from input

#nval = 0

#file_path = "/home/digonto/Codes/Lattice_Analysis/KKpi.S2I2/szscl21_24_128_b1p50_t_x4p300_um0p0840_sm0p0743_n1p265/fits_mhi/000_A1m/out/t0_10/prin_corrs/ord" + str(nval) + "/SUMMARY_GNU_DATA"

def str_to_float_or_str(s):
    try:
        return float(s)   # try to convert
    except ValueError:
        return s 

def read_indexed_file(filename):
    blocks = []
    current = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:  # blank line = new block
                if current:
                    blocks.append(current)
                    current = []
                continue
            if line.startswith("#"):  # skip comments
                continue
            try:
                #splits everything, keeps number as float and 
                row = [str_to_float_or_str(x) for x in line.split()]
                current.append(row)
            except ValueError:
                # skip rows that contain non-numeric entries (like "|")
                continue
        if current:
            blocks.append(current)
    return blocks

# Read the indexed file again
#blocks = read_indexed_file(file_path)

def plot_prin_corr_func(nval, input_file, plot_filename):
    plt.rcParams.update({'font.size': 18})
    plt.rc('font',**{'family':'serif','serif':['Computer Modern Roman']})
    plt.rc('text', usetex=True)

    #N = 100
    blocks = read_indexed_file(input_file)

    fig, ax = plt.subplots(figsize=(12, 5))

    func_data = blocks[0][:]

    active_data = blocks[1][:]
    inactive_data = blocks[2][:]
    mass_data = blocks[4][:]

    #how the mass data is splitted is 
    mass_val = mass_data[0][1] #float
    mass_err = mass_data[0][2] #float
    chisq = mass_data[0][6] #string
    #print(mass_data[0][6])

    x = [row[0] for row in func_data] 
    y = [row[1] for row in func_data]
    ymin = [row[2] for row in func_data]
    ymax = [row[3] for row in func_data]

    adx = [row[0] for row in active_data]
    ady = [row[1] for row in active_data]
    adyerr = [row[2] for row in active_data]

    iadx = [row[0] for row in inactive_data]
    iady = [row[1] for row in inactive_data]
    iadyerr = [row[2] for row in inactive_data]

    ax.set_xlim([0.0,36])
    ax.set_ylim([0.85,1.3])

    ax.plot(x,y, linestyle='solid', color="darkred")
    plt.fill_between(x, ymin, ymax, color="blue", alpha=0.1)

    ax.errorbar(adx, ady , xerr=None, yerr=adyerr,
                marker='o',markerfacecolor="None", markersize=10, color="black",
                linestyle='none',capsize=5)
    ax.errorbar(iadx, iady , xerr=None, yerr=iadyerr,
                marker='o',markerfacecolor="None", markersize=10, color="grey",
                linestyle='none',capsize=5)

    plot_label =     ( "$n = $" + str(nval) + "\n\n" 
                    + "$a_t E_n = $" + str(f"{mass_val:.4f}") + "$\pm$" + str(f"{mass_err:.4f}") + "\n\n"
                    + "$\chi^2$/dof $ = $" + chisq )
    plt.text(
        0.65, 0.95,            # x, y position in axes coordinates (0 to 1)
        plot_label,     
        horizontalalignment='left',
        verticalalignment='top',
        transform=plt.gca().transAxes  # relative to axes, not data
    )
    
    output = plot_filename 
    plt.savefig(output)
    plt.close()  

#plot_prin_corr_func(blocks)
# Show summary and preview
#output_preview = {
#    "total_blocks": len(blocks),
#    "block0_first3_rows": blocks[0][:3] if len(blocks) > 0 else None,
#    "block1_first3_rows": blocks[1][:3] if len(blocks) > 1 else None
#}

#print(output_preview)

#for i in range(len(blocks)):
#    print(blocks[i][:])
#    print("===================")