import dateutil.parser
import numpy as np

def sort_log(log_string):
    lines = np.asarray(log_string.split('\n')[:-1])
    times = [dateutil.parser.parse(line[1:27]) for line in lines]
    sort_indexes = np.argsort(times)
    print('\n'.join(lines[sort_indexes]))
