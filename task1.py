import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from functools import partial
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def create_gui():
    global window
    window = tk.Tk()
    label_modes = tk.Label(window, text = 'Choose number of modes')
    entry_modes = tk.Entry()
    label_samples = tk.Label(window, text = 'Choose number of samples')
    entry_samples = tk.Entry()
        
    print(entry_modes.get(), entry_samples.get())
    plot_with_arg = partial(logic_loop, entry_modes = entry_modes, entry_samples = entry_samples, window=window)
    
    button = tk.Button(window, text="create plot", width=20, command=plot_with_arg)
    label_modes.pack()
    entry_modes.pack()
    label_samples.pack()
    entry_samples.pack()
    button.pack()
    
    tk.mainloop()
    
def create_plot(class0, class1):
    class0_modes = class0[0]
    class0_samples = class0[1]
    class1_modes = class1[0]
    class1_samples = class1[1]
    plot = plt.figure()
    scatter = plot.add_subplot(111)
    scatter.scatter(*class0_modes.T, c = 'red', marker = "P")
    scatter.scatter(*class0_samples.T, c = 'red', marker = '*')
    scatter.scatter(*class1_modes.T, c = 'blue', marker = "P")
    scatter.scatter(*class1_samples.T, c = 'blue', marker = '*')
    
    return plot
    
def create_class(number_of_modes, number_of_samples):
    total_class_samples = []
    class_modes = 10*np.random.rand(number_of_modes, 2)
    for x in class_modes:
        class_samples = np.random.normal(loc=x, size=(number_of_samples, 2))
        for y in class_samples:
            total_class_samples.append(x + y)

    return class_modes, np.array(total_class_samples)

def logic_loop(entry_modes, entry_samples, window):
    try:
        number_of_modes = int(entry_modes.get())
    except:
        number_of_modes = 2
    try:
        number_of_samples = int(entry_samples.get())
    except:
        number_of_samples = 5
    print(number_of_modes, number_of_samples)
    class0 = create_class(number_of_modes, number_of_samples)
    class1 = create_class(number_of_modes, number_of_samples)
    plot = create_plot(class0, class1)
    canvas = FigureCanvasTkAgg(plot, window)
    canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    refresh_button = tk.Button(window, text="refresh", width=20, command=refresh)
    refresh_button.pack()
    
def refresh():
    window.destroy()
    create_gui() 
    
def main():
    create_gui()
    
if __name__ == "__main__":
    main()