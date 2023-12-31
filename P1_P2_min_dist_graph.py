import numpy as np
import matplotlib.pyplot as plt
from itertools import groupby, count
from matplotlib import ticker

peptide_a = 1
peptide_b = 3

x, y = [], []

# using the (minimum distance, timestep) tuple list
# found min distance using algorithm in gramacs repos
with open("new_min_1_2_trimer.txt") as f:
    for line in f:
        cols = line.split()

        if len(cols) == 2:
            x.append(float(cols[0]))
            y.append(float(cols[1]))
# tuple list of floats
both = zip(x, y)

# define threshold binding distance
thresh = 7

time_step = x[1] - x[0]

# define a time period for peptides to be classed as bound
percent_binding_thresh = 0.1

# number of frames in simulation
Frames = len(y)

# function for information to output from simulation data
# min dist, max dist, dist at start and end, frames and time frame number
def important_info():
    Min = min(y)
    Max = max(y)
    print("min dist between peptides = ", Min)
    print("max dist between peptides = ", Max)

    first_t_dist = y[0]
    print("dist at start = ", first_t_dist, "Angstroms")
    last_t_dist = y[-1]
    print("dist at end = ", last_t_dist, "Angstroms")

    print("Frames = ", len(y))

    Time = max(x) - min(x)
    print("Timeframe =", Time, "ps")

# function to define peptides as being bound
# find dists less than thresh
# find differences between these times for these distances
# isolate time bound for over 100 ns
# find number of frames actualy bound
# finally find % of simulation classed as bound
def time_bounded():
    print("BOUND = being within", thresh, "Angstroms of each other")

    less_than_thresh = []

    for items in both:
        if items[1] < thresh:
            less_than_thresh.append(items)

    thresh_times, thresh_dists = zip(*less_than_thresh)

    differences = np.diff(thresh_times)
    full_diff = np.insert(differences, 0, 0)

    full_diff = list(full_diff)

    positions_of_timeframe = []

    for idx, val in enumerate(full_diff):
        if val == 100:
            positions_of_timeframe.append(idx)

    c = count()
    val = max((list(g) for _, g in groupby(positions_of_timeframe, lambda a: a - next(c))), key=len)

    Frames_bound = len(val)

    percent_of_frames_bound = Frames_bound / Frames

    print("peptides classed as bound if they STAY bound for at least", round(percent_binding_thresh * 100),
          "% of total frames, or ", x[-1] * percent_binding_thresh, "ps")
    
    if percent_of_frames_bound > percent_binding_thresh:
        print("P", peptide_a, "and", "P", peptide_b, "WERE BOUND")
    else:
        print("P", peptide_a, "and", "P", peptide_b, "DID NOT BIND")

    print("TIME BOUND =", Frames_bound * time_step, "from total of", x[-1], "ps")
    print("percent of frames bound =", percent_of_frames_bound * 100, "%")

# plotting function for graph
def graph():
    plt.style.use('seaborn-whitegrid')
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title("P{a} - P{b}".format(a=peptide_a, b=peptide_b), fontsize=16)
    ax1.set_xlabel('t (ns)', fontsize=14)
    ax1.set_ylabel("$d_{min}$ ($\AA$)", fontsize=14)
    l = [i * 0.001 for i in x]
    print(l[5] - l[4])
    ax1.plot(x, y, c='blue', linewidth=1, label="raw data")
    # plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    # ax1.xaxis.major.formatter._useMathText = True

    plt.hlines(y=thresh, xmin=0, xmax=max(x), color='black', linestyle='--', zorder=3,
               label="Bonding Threshold of %.1f $\AA$" % thresh)
    # box = ax1.get_position()
    # ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    # ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    for axis in [ax1.yaxis]:
        axis.set_major_locator(ticker.MaxNLocator(prune='lower', integer=True))
    # plt.xlim(l[0], l[-1])
    # plt.ylim(0, 54)
    # fig.savefig("SA-I--P{a}-P{b} trimer thresh={c}A.pdf".format(a=peptide_a, b=peptide_b, c=thresh), bbox_inches='tight')
    plt.show()



important_info()
time_bounded()
graph()

input('Press ENTER to exit')
