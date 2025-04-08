# copernicus_downscale/water_stress_model.py
import numpy as np

def simulate_hydrology(P, E, R_params, I_params):
    R = R_params['a'] + R_params['b'] * P + R_params['c'] * E
    I = I_params['a'] + I_params['b'] * P + I_params['c'] * E
    return R, I

def compute_feasible_supply(R, I, alpha1=0.13, alpha2=0.20, alpha3=0.70):
    I_feas = alpha1 * I
    R_feas = alpha2 * alpha3 * R
    return R_feas, I_feas

def compute_ewei(demand, feasible_supply):
    return demand / feasible_supply

def compute_total_demand(sector_output, coeff):
    return sector_output * coeff
