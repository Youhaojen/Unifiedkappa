import sys
import re
import numpy as np
from crystal import class_poscar
from conductivity import class_kappa


def read_mesh_from_control(filename="CONTROL", default_mesh=[8, 8, 8]):
    """
    Parses the CONTROL file to extract the ngrid dimensions.
    Returns a list of 3 integers, or the default mesh if not found.
    """
    try:
        with open(filename, "r") as f:
            content = f.read()
            
            # Regex details: Matches 'ngrid(:) = X Y Z' or 'ngrid = X Y Z' with flexible spacing
            match = re.search(r"ngrid(?:\(:\))?\s*=\s*([-\d]+)\s+([-\d]+)\s+([-\d]+)", content)
            
            if match:
                mesh = [int(x) for x in match.groups()]
                print(f"Successfully loaded mesh_in from {filename}: {mesh}")
                return mesh
            else:
                print(f"Warning: 'ngrid' settings not found in {filename}. Using default: {default_mesh}")
                return default_mesh
                
    except FileNotFoundError:
        print(f"Warning: {filename} file not found. Using default: {default_mesh}")
        return default_mesh


def read_dim_from_control(filename="CONTROL", default_dim=[2, 2, 2]):
    """
    Parses the CONTROL file to extract the dim dimensions.
    Returns a list of 3 integers, or the default mesh if not found.
    """
    try:
        with open(filename, "r") as f:
            content = f.read()
            
            # Regex details: Matches 'ngrid(:) = X Y Z' or 'ngrid = X Y Z' with flexible spacing
            match = re.search(r"scell(?:\(:\))?\s*=\s*([-\d]+)\s+([-\d]+)\s+([-\d]+)", content)
            
            if match:
                dim = [int(x) for x in match.groups()]
                print(f"Successfully loaded dim_in from {filename}: {dim}")
                return dim
            else:
                print(f"Warning: 'dim' settings not found in {filename}. Using default: {default_dim}")
                return default_dim
                
    except FileNotFoundError:
        print(f"Warning: {filename} file not found. Using default: {default_dim}")
        return default_dim


# 1. Read the mesh parameters from the CONTROL file
mesh_config = read_mesh_from_control("CONTROL")
dim_config = read_dim_from_control("CONTROL")

# 2. Initialize the crystal structure and thermal conductivity objects
obj_poscar = class_poscar("../POSCAR")
obj_kappa = class_kappa(obj_poscar)

# 3. Calculate phonon thermal conductivity
obj_kappa.get_kappa_phonopy(
    mesh_in = mesh_config,  # Dynamic grid loaded from the CONTROL file
    sc_mat = dim_config,
    pm_mat = np.eye(3),
    list_temp = [300],
    name_pcell = "../POSCAR",
    name_ifc2nd = "../FORCE_CONSTANTS_2ND",
    is_minikappa = False,
    is_planckian = False,
    is_sbtetau = True,
    path_sbtetau = "./",
    list_taufactor = [2.0],
    delta_freq = 1
)
