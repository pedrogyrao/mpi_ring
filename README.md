# MPI Ring Election

Simple ring election using mpi4py library.

## Instalation

``` Shell
pip install -r requirements
```

## Running

* To run without any process unavailable:

``` Shell
mpiexec -n 4 python mpi_process.py
```

* To run with one or more processes unavailable:

``` Shell
mpiexec -n 4 python mpi_process.py 1 2 (...) n
```

> Note that this simple code was intended to run using 4 processes at the same time and using the process 0 as the controller.
