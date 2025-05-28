import matplotlib.pyplot as plt

#Data necessary for plotting:

Individuals=["level 0","level 1","level 2","level 3","level 4"]



D={
        "level 0": [],
        "level 1": [],
        "level 2": [],
        "level 3": [],
        "level 4": []
    }
def data_dict(Distribution):

    # this function collects the distribution data in a dictionary in order to use it later for plotting
    D["level 0"].append(Distribution[0])
    D["level 1"].append(Distribution[1])
    D["level 2"].append(Distribution[2])
    D["level 3"].append(Distribution[3])
    D["level 4"].append(Distribution[4])

#Now we start plotting
def plot_function(Dict,Generations):

    time_periods = list(range(0,Generations))
    fig, ax = plt.subplots(figsize=(10, 6))

    # create plot
    bottom = [0] * len(time_periods)
    for individual in Individuals:
        ax.bar(time_periods, Dict[individual], bottom=bottom, label=individual)
        bottom = [bottom[i] + Dict[individual][i] for i in range(len(time_periods))]

    # set a name for title and axis
    ax.set_xlabel('Generations')
    ax.set_ylabel('Distribution')
    ax.set_title('Evolving Population')
    ax.legend()

    # Show diagramm
    plt.xticks(time_periods)
    plt.tight_layout()
    plt.show()

#other diagramm

def plot_line_chart(Dict, Generations):
    time_periods = list(range(Generations))  # X-axis: Generation numbers

    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))

    # Loop through each individual level and plot a line for each one
    for individual in Individuals:
        ax.plot(time_periods, Dict[individual], label=individual)

    # Set labels and title for the axes
    ax.set_xlabel('Generations')
    ax.set_ylabel('Number of Individuals')
    ax.set_title('Growth Curve')

    # Add a legend to identify each line by color
    ax.legend()

    # Display the chart
    plt.tight_layout()
    plt.show()


#Function calculates the area of the individual colours in the säulendiagramm

def calculate_area_proportions(Dict):
    # Berechne die Summe aller Werte über alle Farben und Generationen
    total_area = sum(sum(Dict[individual]) for individual in Dict)

    # Berechne den Anteil für jede Farbe
    area_proportions = {}
    for individual in Dict:
        individual_area = sum(Dict[individual])
        area_proportions[individual] = individual_area / total_area

    return area_proportions

