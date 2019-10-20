from configparser import (
    ConfigParser
)

from main import (
    main
)

from swarm_traveling_salesman import (
    print_tour
)


# code obtained from
#     https://www.pythoncentral.io/pythons-range-function-explained/
def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

num_ants = 1
num_maps = 6

# run many tests of many different configurations and report best parameters for
# each map file at the end
for i in range(num_maps):
    best_path = None
    config = ConfigParser()
    map_file = "maps/map" + str(i+1) + ".txt"
    for alpha in frange(0, 2, 0.5):
        for beta in frange(0, 2, 0.5):
            for rho in frange(0, 0.5, 0.1):
                for num_iters in range(50, 101, 10):
                    config['PARAMETERS'] = {'map':               map_file,
                                            'alpha':             alpha,
                                            'beta':              beta,
                                            'rho':               rho,
                                            'num_ants_per_city': num_ants,
                                            'num_iterations':    num_iters}
                    with open('config.ini', 'w') as configfile:
                        config.write(configfile)
                        configfile.close()

                    path = main('config.ini')

                    if best_path is None or \
                                    path.length < best_path.length:
                        best_path = path.copy()
    
    # report results
    print("Results for map/map" + str(i+1) + ".txt")
    print("------------------------")
    print("    Path:")
    print("        ", end="")
    print_tour(best_path)
    print("    Length: " + str(best_path.length))
    print("\n")    
