import matplotlib.pyplot as plt

def plot_metrics(overtalk, silence):
    labels = ['Overtalk %', 'Silence %']
    values = [overtalk, silence]
    plt.bar(labels, values, color=['red', 'blue'])
    plt.ylabel('Percentage')
    plt.title('Call Quality Metrics')
    plt.show()