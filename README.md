# COMP 151 Project 3

Mark Fraser

m_fraser3@u.pacific.edu

# Table of Contents

1. [COMP 151 Project 3](#comp-151-project-3)
2. [Table of Contents](#table-of-contents)
3. [Usage](#usage)
    1. [Args](#args)
        1. [config](#config)
        2. [milestone](#milestone)
4. [Optimal Solutions](#optimal-solutions)
    1. [Global Optimal](#global-optimal)
    2. [Optimal Parameters](#optimal-parameters)

# Usage

To run the program, use either of the following commands in the project's root
directory.

```
/path/to/project/$ python main.py --config <config_file>
/path/to/project/$ python main.py -c <config_file>
```

##  Args

### config

This is the path to the configuration file for the program to parse.  The file
must contain the following parameters:

```
[PARAMETERS]
map = <directory path to the map file>
alpha = <alpha value [0, +inf]>
beta = <beta value [0, +inf]>
rho = <evaporation rate [0,1]>
num_ants_per_city = <number of ants spawned at each city [1, +inf]>
num_iterations = <number of iterations for the program to run [1, +inf]>
```

NOTE:  Certain combinations of the above parameters can cause the program to
fail (e.g. -- alpha is > 0 and rho == 1).  Such combinations can potentially
cause the ant's city selection computation to evaluate to 0, thereby throwing a
'division by zero' error.  Because this scenario is difficult to foresee, it is
up to the user to provide reasonable values.

### milestone

This is a global constant in `swarm_traveling_salesman.py`.  It is not intended
to be changed, but if the tester wishes to see a finer or coarser granularity,
this value determines after how many generations intermediate output is printed.
The default value is `10`.

# Optimal Solutions

## Global Optimal

Leveraging the `find_best_path.py` script, we obtain the following global
optimal solutions for the provided maps to be:

```
Results for map/map1.txt
------------------------
    Path:
        C -> D -> B -> A
    Length: 6


Results for map/map2.txt
------------------------
    Path:
        B -> A -> C -> D -> E
    Length: 11


Results for map/map3.txt
------------------------
    Path:
        D -> A -> E -> B -> C
    Length: 65


Results for map/map4.txt
------------------------
    Path:
        E -> H -> B -> C -> F -> G -> A -> D
    Length: 159


Results for map/map5.txt
------------------------
    Path:
        F -> B -> H -> C -> E -> I -> A -> D -> J -> G
    Length: 184


Results for map/map6.txt
------------------------
    Path:
        P -> M -> W -> N -> G -> B -> X -> E -> I -> K -> J -> Z -> F -> H -> L -> Y -> R -> S -> U -> V -> C -> T -> O -> A -> D -> Q
    Length: 592
```

NOTE: `find_best_path.py` can take half an hour or more to run all
configurations.  It will also generate a lot of output.  If you wish to run the
program, pipe the output to a file to make it easier to sift through results.

```
/path/to/project$ python find_best_path.py > output.txt
```

## Optimal Parameters

The following configuration on the developer's machine has proven to be one of
the best configurations for finding a near-optimal solution.  It is difficult to
find one true configuration that solves all optimally without taking an
excessive amount of time to run, as a graph's layout can change the
effectiveness of a configuration.

The config is:

```
[PARAMETERS]
map = maps/map1.txt
alpha = 1
beta = 1.5
rho = 0.4
num_ants_per_city = 1
num_iterations = 100
```

The best results obtained on the developer's machine are:

**map1.txt**

```
Results:
--------

Best Path:
A -> B -> D -> C

Length:
6

Pheremone Map:
        A       B       C       D
A       0.0     130.5   76.78   0.0
B       130.5   0.0     0.0     74.98
C       76.78   0.0     0.0     130.18
D       0.0     74.98   130.18  0.0
```

**map2.txt**

```
Results:
--------

Best Path:
E -> D -> C -> A -> B

Length:
11

Pheremone Map:
        A       B       C       D       E
A       0.0     67.76   64.79   0.0     0.0
B       67.76   0.0     0.0     0.0     24.88
C       64.79   0.0     0.0     58.01   0.0
D       0.0     0.0     58.01   0.0     65.67
E       0.0     24.88   0.0     65.67   0.0
```

**map3.txt**

```
Results:
--------

Best Path:
D -> A -> B -> C -> E

Length:
68

Pheremone Map:
        A       B       C       D       E
A       0.0     10.61   0.0     9.8     0.0
B       10.61   0.0     10.82   0.0     0.0
C       0.0     10.82   0.0     0.0     9.74
D       9.8     0.0     0.0     0.0     5.17
E       0.0     0.0     9.74    5.17    0.0
```

**map4.txt**

```
Results:
--------

Best Path:
E -> H -> B -> C -> F -> G -> A -> D

Length:
159

Pheremone Map:
        A       B       C       D       E       F       G       H
A       0.0     1.37    0.56    2.17    3.03    0.2     1.66    0.5
B       1.37    0.0     2.43    0.0     0.03    2.07    0.61    3.89
C       0.56    2.43    0.0     0.0     2.49    3.1     0.75    0.0
D       2.17    0.0     0.0     0.0     0.01    0.0     3.65    4.86
E       3.03    0.03    2.49    0.01    0.0     1.08    0.07    1.6
F       0.2     2.07    3.1     0.0     1.08    0.0     3.71    0.0
G       1.66    0.61    0.75    3.65    0.07    3.71    0.0     0.0
H       0.5     3.89    0.0     4.86    1.6     0.0     0.0     0.0
```

**map5.txt**

```
Results:
--------

Best Path:
F -> B -> H -> C -> E -> I -> G -> A -> D -> J

Length:
209

Pheremone Map:
        A       B       C       D       E       F       G       H       I       J
A       0.0     0.0     0.0     2.97    1.2     1.69    0.0     2.63    0.57    0.11
B       0.0     0.0     0.0     2.17    0.0     4.16    0.0     3.67    0.0     0.0
C       0.0     0.0     0.0     0.16    4.24    2.81    0.0     3.48    0.0     0.0
D       2.97    2.17    0.16    0.0     0.0     0.0     0.0     0.0     0.0     5.34
E       1.2     0.0     4.24    0.0     0.0     0.0     0.0     0.0     5.53    0.0
F       1.69    4.16    2.81    0.0     0.0     0.0     1.14    0.0     0.0     0.01
G       0.0     0.0     0.0     0.0     0.0     1.14    0.0     0.0     4.42    5.41
H       2.63    3.67    3.48    0.0     0.0     0.0     0.0     0.0     0.35    0.02
I       0.57    0.0     0.0     0.0     5.53    0.0     4.42    0.35    0.0     0.0
J       0.11    0.0     0.0     5.34    0.0     0.01    5.41    0.02    0.0     0.0
```

**map6.txt**

```
Results:
--------

Best Path:
E -> I -> K -> J -> Z -> C -> U -> V -> L -> Y -> R -> S -> D -> H -> G -> B -> X -> W -> N -> O -> A -> P -> M -> T -> F -> Q

Length:
746

Pheremone Map:
        A       B       C       D       E       F       G       H       I       J       K       L       M       N       O       P       Q       R       S       T       U       V       W       X       Y       Z
A       0.0     0.01    0.02    2.02    0.17    0.05    0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.9     2.09    1.94    0.38    0.11    0.0     0.15    0.0     0.0     0.42    0.0     0.0     0.0
B       0.01    0.0     0.0     0.0     0.0     0.42    4.05    0.0     0.0     0.0     0.03    0.0     0.0     0.0     0.0     0.19    0.02    0.01    0.0     0.0     0.0     0.03    0.02    3.5     0.0     0.0
C       0.02    0.0     0.0     0.0     0.04    0.0     0.06    0.0     0.0     0.0     0.0     0.01    0.0     0.0     0.0     0.22    0.0     0.0     0.0     0.46    3.71    0.29    0.36    0.0     0.0     3.21
D       2.02    0.0     0.0     0.0     0.0     0.0     0.0     3.04    0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.47    0.0     2.84    0.01    0.0     0.0     0.0     0.0     0.01    0.0
E       0.17    0.0     0.04    0.0     0.0     0.1     0.08    0.0     2.64    0.19    0.0     0.0     0.02    0.0     0.03    0.06    0.0     0.87    0.42    0.14    0.4     0.0     0.03    2.96    0.0     0.0
F       0.05    0.42    0.0     0.0     0.1     0.0     0.17    1.23    0.15    0.0     0.0     0.0     0.0     0.32    0.34    0.59    0.96    0.69    0.0     1.53    0.0     0.09    0.26    0.21    0.0     0.49
G       0.0     4.05    0.06    0.0     0.08    0.17    0.0     2.09    0.47    0.0     0.0     0.0     0.0     0.89    0.0     0.1     0.15    0.07    0.0     0.09    0.0     0.0     0.11    0.0     0.0     0.0
H       0.0     0.0     0.0     3.04    0.0     1.23    2.09    0.0     0.0     0.0     0.0     1.5     0.0     0.57    0.0     0.0     0.0     0.01    0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0
I       0.0     0.0     0.0     0.0     2.64    0.15    0.47    0.0     0.0     0.0     1.93    0.0     0.03    0.0     0.0     0.09    1.6     0.1     0.01    0.38    0.0     0.0     0.85    0.01    0.0     0.0
J       0.0     0.0     0.0     0.0     0.19    0.0     0.0     0.0     0.0     0.0     3.03    0.0     0.0     0.0     1.09    0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     4.09
K       0.0     0.03    0.0     0.0     0.0     0.0     0.0     0.0     1.93    3.03    0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.16    0.0     0.0     0.0     0.0     0.0     3.23    0.0
L       0.0     0.0     0.01    0.0     0.0     0.0     0.0     1.5     0.0     0.0     0.0     0.0     0.19    0.0     0.0     0.0     0.01    0.0     0.0     0.0     0.0     2.51    0.1     0.0     4.05    0.0
M       0.0     0.0     0.0     0.0     0.02    0.0     0.0     0.0     0.03    0.0     0.0     0.19    0.0     0.0     0.0     2.65    1.21    1.13    0.0     2.45    0.0     0.0     0.76    0.0     0.0     0.0
N       0.9     0.0     0.0     0.0     0.0     0.32    0.89    0.57    0.0     0.0     0.0     0.0     0.0     0.0     1.64    0.39    0.32    0.08    0.42    0.06    0.0     0.0     2.7     0.0     0.0     0.0
O       2.09    0.0     0.0     0.0     0.03    0.34    0.0     0.0     0.0     1.09    0.0     0.0     0.0     1.64    0.0     0.24    0.0     0.0     0.0     1.98    0.0     0.39    0.47    0.0     0.0     0.0
P       1.94    0.19    0.22    0.0     0.06    0.59    0.1     0.0     0.09    0.0     0.0     0.0     2.65    0.39    0.24    0.0     0.2     0.02    0.07    0.43    0.0     0.0     0.21    0.0     0.05    0.06
Q       0.38    0.02    0.0     0.47    0.0     0.96    0.15    0.0     1.6     0.0     0.0     0.01    1.21    0.32    0.0     0.2     0.0     0.11    1.67    0.23    0.0     0.59    0.17    0.0     0.0     0.05
R       0.11    0.01    0.0     0.0     0.87    0.69    0.07    0.01    0.1     0.0     0.0     0.0     1.13    0.08    0.0     0.02    0.11    0.0     2.82    0.0     0.06    0.07    0.28    0.0     1.04    0.46
S       0.0     0.0     0.0     2.84    0.42    0.0     0.0     0.0     0.01    0.0     0.16    0.0     0.0     0.42    0.0     0.07    1.67    2.82    0.0     0.0     0.0     0.0     0.01    0.0     0.0     0.0
T       0.15    0.0     0.46    0.01    0.14    1.53    0.09    0.0     0.38    0.0     0.0     0.0     2.45    0.06    1.98    0.43    0.23    0.0     0.0     0.0     0.0     0.09    0.07    0.0     0.0     0.02
U       0.0     0.0     3.71    0.0     0.4     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.06    0.0     0.0     0.0     3.92    0.0     0.24    0.07    0.01
V       0.0     0.03    0.29    0.0     0.0     0.09    0.0     0.0     0.0     0.0     0.0     2.51    0.0     0.0     0.39    0.0     0.59    0.07    0.0     0.09    3.92    0.0     0.01    0.24    0.0     0.0
W       0.42    0.02    0.36    0.0     0.03    0.26    0.11    0.0     0.85    0.0     0.0     0.1     0.76    2.7     0.47    0.21    0.17    0.28    0.01    0.07    0.0     0.01    0.0     1.25    0.0     0.0
X       0.0     3.5     0.0     0.0     2.96    0.21    0.0     0.0     0.01    0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.24    0.24    1.25    0.0     0.0     0.0
Y       0.0     0.0     0.0     0.01    0.0     0.0     0.0     0.0     0.0     0.0     3.23    4.05    0.0     0.0     0.0     0.05    0.0     1.04    0.0     0.0     0.07    0.0     0.0     0.0     0.0     0.0
Z       0.0     0.0     3.21    0.0     0.0     0.49    0.0     0.0     0.0     4.09    0.0     0.0     0.0     0.0     0.0     0.06    0.05    0.46    0.0     0.02    0.01    0.0     0.0     0.0     0.0     0.0
```

**Update 10/22/19:**

The original maps above are unidirectional.  Below are the results with the same
configuration as above with maps 3-6.  Without having the same time to
definitively find the global optima for the provided maps, it appears our
configuration still performs near optimally with some maps performing better
than others based on the configuration's applicability to the graph.

**map3.txt**

```
Results:
--------

Best Path:
E -> B -> A -> C -> D

Length:
111

Pheremone Map:
        A       B       C       D       E
A       0.0     8.62    8.35    0.0     0.0
B       8.62    0.0     0.0     0.0     6.54
C       8.35    0.0     0.0     9.04    0.0
D       0.0     0.0     9.04    0.0     6.1
E       0.0     6.54    0.0     6.1     0.0
```

**map4.txt**

```
Results:
--------

Best Path:
C -> G -> D -> E -> H -> A -> F -> B

Length:
301

Pheremone Map:
        A       B       C       D       E       F       G       H
A       0.0     0.0     0.01    0.0     0.06    3.4     2.12    4.69
B       0.0     0.0     4.45    0.29    0.88    0.21    1.22    1.02
C       0.01    4.45    0.0     0.0     0.09    1.4     3.51    0.0
D       0.0     0.29    0.0     0.0     3.38    5.2     1.52    0.0
E       0.06    0.88    0.09    3.38    0.0     0.0     0.52    4.74
F       3.4     0.21    1.4     5.2     0.0     0.0     0.0     0.0
G       2.12    1.22    3.51    1.52    0.52    0.0     0.0     0.0
H       4.69    1.02    0.0     0.0     4.74    0.0     0.0     0.0
```

**map5.txt**

```
Results:
--------

Best Path:
I -> A -> F -> C -> J -> H -> E -> G -> D -> B

Length:
536

Pheremone Map:
        A       B       C       D       E       F       G       H       I       J
A       0.0     0.71    1.97    0.0     1.26    0.0     0.0     0.0     3.3     0.0
B       0.71    0.0     0.0     2.27    1.64    0.0     0.03    0.14    0.32    1.33
C       1.97    0.0     0.0     0.02    0.08    3.77    0.0     0.0     0.0     1.47
D       0.0     2.27    0.02    0.0     0.62    0.0     2.69    0.26    0.58    0.56
E       1.26    1.64    0.08    0.62    0.0     0.0     0.45    1.36    0.0     0.51
F       0.0     0.0     3.77    0.0     0.0     0.0     3.55    0.0     0.0     0.0
G       0.0     0.03    0.0     2.69    0.45    3.55    0.0     0.49    0.0     0.0
H       0.0     0.14    0.0     0.26    1.36    0.0     0.49    0.0     2.19    2.83
I       3.3     0.32    0.0     0.58    0.0     0.0     0.0     2.19    0.0     0.1
J       0.0     1.33    1.47    0.56    0.51    0.0     0.0     2.83    0.1     0.0
```

**map6.txt**

```
Results:
--------

Best Path:
T -> X -> H -> U -> M -> Z -> W -> S -> I -> F -> E -> K -> D -> Y -> L -> O -> C -> J -> Q -> R -> V -> A -> G -> P -> B -> N

Length:
746

Pheremone Map:
        A       B       C       D       E       F       G       H       I       J       K       L       M       N       O       P       Q       R       S       T       U       V       W       X       Y       Z
A       0.0     0.0     0.0     0.0     0.02    0.11    4.31    0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.07    0.0     0.05    0.0     0.0     0.57    4.88    0.0     0.0     0.0     0.0
B       0.0     0.0     0.04    0.0     2.22    0.04    0.0     0.0     0.05    0.12    0.0     0.24    0.0     4.91    0.0     1.87    0.0     0.0     0.54    0.0     0.0     0.0     0.0     0.0     0.0     0.0
C       0.0     0.04    0.0     0.08    0.2     0.01    0.0     0.0     0.0     3.3     0.01    0.0     0.0     0.0     3.85    0.38    0.0     1.07    0.05    0.0     0.01    0.0     0.0     0.48    0.15    0.24
D       0.0     0.0     0.08    0.0     0.0     0.0     0.0     0.0     0.0     0.66    4.06    0.1     2.5     0.0     0.0     0.01    0.0     0.02    0.0     0.0     0.0     0.0     0.0     0.0     2.54    0.0
E       0.02    2.22    0.2     0.0     0.0     1.09    0.0     0.32    1.98    0.0     2.14    0.19    0.01    0.17    0.07    0.66    0.04    0.02    0.03    0.45    0.14    0.0     0.07    0.0     0.0     0.0
F       0.11    0.04    0.01    0.0     1.09    0.0     0.0     0.14    3.41    0.09    0.05    0.38    0.0     1.14    0.0     0.37    1.47    0.48    0.05    0.19    0.12    0.04    0.17    0.04    0.07    0.01
G       4.31    0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.03    0.0     2.6     0.0     0.0     0.05    0.0     0.17    2.79    0.0     0.0     0.0     0.04    0.0     0.0     0.0     0.0     0.0
H       0.0     0.0     0.0     0.0     0.32    0.14    0.0     0.0     0.15    0.04    0.0     0.0     0.0     0.0     0.0     0.09    0.19    0.02    0.0     0.49    4.17    0.0     0.0     4.32    0.0     0.0
I       0.0     0.05    0.0     0.0     1.98    3.41    0.03    0.15    0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.05    0.0     0.0     4.31    0.0     0.0     0.0     0.0     0.0     0.0     0.0
J       0.0     0.12    3.3     0.66    0.0     0.09    0.0     0.04    0.0     0.0     0.0     0.0     0.03    0.0     0.09    0.15    2.79    0.0     2.0     0.45    0.0     0.0     0.04    0.0     0.0     0.0
K       0.0     0.0     0.01    4.06    2.14    0.05    2.6     0.0     0.0     0.0     0.0     0.01    0.0     0.0     0.32    0.0     0.0     0.59    0.14    0.0     0.09    0.0     0.0     0.0     0.0     0.0
L       0.0     0.24    0.0     0.1     0.19    0.38    0.0     0.0     0.0     0.0     0.01    0.0     0.0     0.01    1.86    0.03    0.0     1.28    0.35    0.2     0.17    0.0     0.01    0.0     4.98    0.0
M       0.0     0.0     0.0     2.5     0.01    0.0     0.0     0.0     0.0     0.03    0.0     0.0     0.0     0.0     0.0     0.03    0.0     0.0     0.0     0.0     2.67    0.0     0.0     0.0     0.0     4.82
N       0.0     4.91    0.0     0.0     0.17    1.14    0.05    0.0     0.0     0.0     0.0     0.01    0.0     0.0     0.0     0.34    0.0     0.02    0.0     0.04    0.04    2.67    0.0     0.27    0.13    0.0
O       0.0     0.0     3.85    0.0     0.07    0.0     0.0     0.0     0.0     0.09    0.32    1.86    0.0     0.0     0.0     3.28    0.0     0.0     0.0     0.58    0.0     0.0     0.0     0.0     0.0     0.0
P       0.07    1.87    0.38    0.01    0.66    0.37    0.17    0.09    0.05    0.15    0.0     0.03    0.03    0.34    3.28    0.0     0.03    0.21    0.0     0.16    0.17    0.0     0.34    0.0     0.58    0.5
Q       0.0     0.0     0.0     0.0     0.04    1.47    2.79    0.19    0.0     2.79    0.0     0.0     0.0     0.0     0.0     0.03    0.0     2.72    0.0     0.0     0.0     0.0     0.0     0.0     0.02    0.0
R       0.05    0.0     1.07    0.02    0.02    0.48    0.0     0.02    0.0     0.0     0.59    1.28    0.0     0.02    0.0     0.21    2.72    0.0     0.0     0.51    0.08    2.42    0.0     0.01    0.07    0.01
S       0.0     0.54    0.05    0.0     0.03    0.05    0.0     0.0     4.31    2.0     0.14    0.35    0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.02    0.0     0.0     2.55    0.0     0.0     0.0
T       0.0     0.0     0.0     0.0     0.45    0.19    0.0     0.49    0.0     0.45    0.0     0.2     0.0     0.04    0.58    0.16    0.0     0.51    0.02    0.0     0.04    0.0     1.94    4.67    0.0     0.0
U       0.57    0.0     0.01    0.0     0.14    0.12    0.04    4.17    0.0     0.0     0.09    0.17    2.67    0.04    0.0     0.17    0.0     0.08    0.0     0.04    0.0     0.0     0.0     0.0     1.19    0.0
V       4.88    0.0     0.0     0.0     0.0     0.04    0.0     0.0     0.0     0.0     0.0     0.0     0.0     2.67    0.0     0.0     0.0     2.42    0.0     0.0     0.0     0.0     0.03    0.0     0.0     0.0
W       0.0     0.0     0.0     0.0     0.07    0.17    0.0     0.0     0.0     0.04    0.0     0.01    0.0     0.0     0.0     0.34    0.0     0.0     2.55    1.94    0.0     0.03    0.0     0.06    0.16    4.43
X       0.0     0.0     0.48    0.0     0.0     0.04    0.0     4.32    0.0     0.0     0.0     0.0     0.0     0.27    0.0     0.0     0.0     0.01    0.0     4.67    0.0     0.0     0.06    0.0     0.06    0.03
Y       0.0     0.0     0.15    2.54    0.0     0.07    0.0     0.0     0.0     0.0     0.0     4.98    0.0     0.13    0.0     0.58    0.02    0.07    0.0     0.0     1.19    0.0     0.16    0.06    0.0     0.0
Z       0.0     0.0     0.24    0.0     0.0     0.01    0.0     0.0     0.0     0.0     0.0     0.0     4.82    0.0     0.0     0.5     0.0     0.01    0.0     0.0     0.0     0.0     4.43    0.03    0.0     0.0
```
