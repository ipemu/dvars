
# DVARS - Elastic Displacement, Velocity and Acceleration Response Spectra


## Overview
In earthquake engineering response spectrum is used to analyze the dynamic reponse of structures to seismic events.
The response spectrum shows the maximum values of displacement, velocity and/or acceleration
as a function of frequency or period.

The calculation is based on the assumption that the structure behaves as a simple mechnical harmonic oscillator,
damped by default to only 5% and tuned to the natural frequency that is being tested.
The response spectrum can be determined by applying the same earthquake to a series
of simple oscillators with different natural frequencies and a uniform damping of 5%.
In the analog implementation of this test, the earthquake acts on a series of oscillators in parallel, 
while computer simulation is usually arranged serially - by repeatedly processing
the time record of the earthquake on a sequentially retuned harmonic oscillator model.
For each excitation of the recorded acceleration waveform, the maximum observed response
in terms of relative displacement or absolute acceleration is recorded.

This repository provides a Python interface to a C implementation of response spectrum computation,
which is based on the classical algorithm ``rdcalcdp``,
taken from [EXSIM12 repository](https://github.com/GFZ-Centre-for-Early-Warning/exsim)
(K. Assatourians and G. Atkinson, 2012).
This is a modified version of the algorithm ``Quake.For``, originally written by J.M. Roesset in 1971.
The formulation is from Nigam and Jennings (BSSA, v. 59, 909-922, 1969).

## Installation prerequisites
- Python 3.x
- Dependencies: ctypes, numpy, matplotlib

For buildeng the C extension:
- C compiler (e.g., GCC)
- Cross-compilation tools Mingw64 if building for MS Windows

## Installation
Since the DVARS package is not yet available on PyPI, you can install it directly from the wheel.

To install the DVARS package, you can use pip:
```bash
pip install dvars-0.1.2-cp311-cp311-linux_x86_64.whl --upgrade
```
## Usage
```python
# Import the dars function from the dvars module
from dvars import dars
# Use help for listing arguments
help(dars)
```
The ``dars`` function provides a calculation of the response spectrum.
The input is a time history of ground motion (accelerogram)
and the output is a tuple containing:
- A numpy array of frequencies (in Hz)
- A numpy array of relative displacements
- A numpy array of absolute accelerations

Simply as the output of the dars function we get DSR - Displacement Response Spectra.
Other modifications used in practice are:
- PSA (PARS) - Pseudo Acceleration Response Spectra,
- PSV (PVRS) - Pseudo Velocity Response Spectra,

which can be derived from DSR according to the following relationships:
- pseudo-velocity response spectrum $\mathsf{PSV}(f) = (2 \pi f) \mathsf{DRS}(f)$
- pseudo-acceleration response spectrum $\mathsf{PSA}(f) = (2 \pi f) \mathsf{PSV}(f)$

The series of absolute accelerations $AA$ is given for completeness.
Due to the small value of the standard oscillator damping (5%), the values
of absolute acceleration $AA$ and pseudo-acceleration response spectrum $\mathsf{PSA}$ are practically the same.

$$AA(f) \sim \mathsf{PSA}(f) = (2 \pi f)^2 \mathsf{DRS}(f)$$

The absolute acceleration and pseudo-acceleration values start to differ significantly in situations such as long periods and/or greater than standard damping.

## Example
Examples are not included in the distribution package, but you can find them in the repository https://github.com/zacherle/dvars in the `examples` directory.

The notebook ``example_dars_esmdb.ipynb`` compares the response spectrum calculated by the `dvars.dars` function
with the data stored in the [ESM-DB](https://esm-db.eu), the Engineering Strong-Motion Database. 
```bash
jupyter notebook examples/example_dvars.ipynb
```

## Building the C extension and wheel distribution

To build the C extension and wheel distribution, you need to have the following prerequisites installed:
- Python 3.x
- A C compiler (e.g., GCC for Linux, MinGW for Windows)
- `build` and `setuptools` for building the package

You can download the source package from the github repository.

```bash
tar -xvf dvars-0.1.2.tar.gz
cd dvars-0.1.2
python3 -m build --wheel
```

This will create a source distribution and a wheel distribution in the `dist` directory.

<!--
Alternatively, you can use the `make` command to build the package and the C extension
using cross-compilation tools on Linux for Windows.

```bash
# linux native build
make build
# or for on Linux cross-compilation for Windows
# buildw32 is for 32-bit Windows builds
make buildw32
# buildw64 is for 64-bit Windows builds
make buildw64
# clean removes build artifacts
make clean
# distclean removes all build artifacts and cleated distribution files
make distclean
```
-->

## Limitations
- The algorithm is designed for linear oscillators and may not be suitable for non-linear systems.
- If non-standard damping is required, then the assumptions for calculating pseudo-acceleration
  from the relative displacement series are not met and the results may not be accurate.
  Use the absolute acceleration series instead.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements,
please open an issue or submit a pull request.

## License
This project is open source.

## Literature
- Nigam, N.C., and Jennings, P.C. (1969). "Calculation of Response Spectra from Strong-motion Earthquake Records." Bulletin of the Seismological Society of America, Vol. 59, No.2, pp. 909-922. April, 1969

