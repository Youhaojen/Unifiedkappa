# Unifiedkappa
Scripts for computing the diagonal and off-diagonal contributions to lattice thermal conductivity, based on the inputs and outputs from ShengBTE. The revised-phonopy can produce off-diagonal group velocities tensors with degeneracy properly treated.

# How to use `unifiedkappa`
* Run the installation script to create a clean Conda environment, build the revised phonopy, and install unifiedkappa

```bash
git clone https://github.com/Youhaojen/Unifiedkappa.git
cd Unifiedkappa
bash install.sh
cd ..
rm -rf Unifiedkappa
```

* Navigate to your working directory (e.g., example) containing the input files and run the CLI command with your target temperature:

```bash
unifiedkappa 300
```

* Folder `example` contains the inputs and outputs typically found in ShengBTE calculations

* The working directory must contain the following input files typically found in ShengBTE / Phonopy calculations: `POSCAR`, `CONTROL`, and `FORCE_CONSTANTS_2ND`

* Note that in order to read scattering rates produced by ShengBTE please explicitly specify onlyharmonic=.FALSE. in CONTROL file
