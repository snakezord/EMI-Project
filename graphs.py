import csv
import matplotlib.pyplot as plt
import numpy as np
import operator

DIRECTORY = "/Users/romanzhydyk/Desktop/MEI/projeto/newdata/outputs"
ALGORITHMS = ['bubble', 'insertion', 'merge', 'quick']
INITIAL_PROBABILITY = 0.01
PROBABILITY_ITERATOR = 0.1
PROBABILITY_MAX = 0.95
N_OUTPUT_FOLDERS = 10
N_OUTPUTS_MAX = 10000
DATA = {}

def get_data():
    for algo in ALGORITHMS:  # a ler as pastas dos algoritmos
        prob = INITIAL_PROBABILITY
        while prob < PROBABILITY_MAX:  # a ler as pastas das probabilidades
            out = 1
            new_dict = {}
            while out <= N_OUTPUT_FOLDERS:  # a ler as pastas dos outputs
                j = 0
                k = 0
                n = 100
                while n < N_OUTPUTS_MAX:  # a ler os ficheiros nas pastas de outputs
                    if 0 < n < 1000:
                        n = 100 + 100 * j
                        j += 1
                    if 1000 <= n <= 10000:
                        n = 1000 + 500 * k
                        k += 1
                    dir = DIRECTORY + "/" + algo + "/" + str("{0:.2f}".format(prob)) + "/" + "output" + str(out) + "/"
                    file_name = "data_" + str(n) + ".out"
                    file_dir = dir + file_name
                    with open(file_dir) as data_file:
                        line = 0
                        data = csv.reader(data_file)
                        for row in data:
                            line += 1
                            if line == 4:
                                largest_sub_seq = int(row[0])
                                if n not in new_dict:
                                    new_dict[n] = [largest_sub_seq, [largest_sub_seq]]
                                else:
                                    new_dict[n][0]+=largest_sub_seq
                                    new_dict[n][1].append(largest_sub_seq)
                out += 1
            new_dict = {x: [float("{0:.2f}".format(new_dict[x][0] / N_OUTPUT_FOLDERS)), new_dict[x][1]] for x in new_dict}  # calculo da media para cada output
            prob = float("{0:.2f}".format(prob))
            if algo not in DATA:
                DATA[algo] = {prob: new_dict}
            else:
                DATA[algo].update({prob: new_dict})
            prob += PROBABILITY_ITERATOR

def draw_largest_sub_seq_prob():
    y = [i for i in DATA['bubble'].keys()]
    for algo in ALGORITHMS:
        x = [DATA[algo][prob][2000][0] for prob in DATA[algo]]
        plt.plot(x, y, label=algo)
    plt.legend()
    plt.title("Grafico de maior sub-seq com prob para 2000 Elementos")
    plt.xlabel('Maior Sub seq')
    plt.ylabel('Probabilidade')
    plt.show()
    return

def draw_N_largest_sub_seq():
    count=INITIAL_PROBABILITY
    while count < PROBABILITY_MAX:
        prob = float("{0:.2f}".format(count))
        for algo in ALGORITHMS:
            x = list(DATA[algo][prob].keys())
            y = [x[0] for x in DATA[algo][prob].values()]
            Xi = [np.std(x[1])for x in DATA[algo][prob].values()] #Desvio padrão para cada N
            plt.plot(x, y, label=algo)
            upper_bound = list(map(operator.add, y, Xi))
            lower_bound = list(map(operator.sub, y, Xi))
            plt.fill_between(x, lower_bound, upper_bound, alpha = 0.2)
            plt.legend()
        plt.title("Grafico de sub-sequencia maior com prob: " + str(prob))
        plt.xlabel('N elementos')
        plt.ylabel('Maior sub-sequencia')
        plt.show()
        count+=PROBABILITY_ITERATOR
    return

get_data()
draw_largest_sub_seq_prob()
#draw_N_largest_sub_seq()