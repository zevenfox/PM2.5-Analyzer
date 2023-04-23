import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Define the GUI
class Application(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("Data Processing Application")
        self.parent.geometry("500x500")
        self.create_widgets()


    def create_widgets(self):
        self.label_output = tk.Label(self.parent, text="")
        self.label_output.pack()
        # Create the browse button
        self.choose_file_label = tk.Label(self.parent, text="Choose a CSV file from your computer")
        self.choose_file_label.pack()
        self.browse_button = tk.Button(self.parent, text="Choose File", command=self.browse_file)
        self.browse_button.pack()
        # Create the input widgets
        self.label_year = tk.Label(self.parent, text="Choose year:")
        self.label_year.pack()
        self.var_year = tk.StringVar(self.parent)
        self.var_year.set("2010")
        self.option_year = tk.OptionMenu(self.parent, self.var_year, "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017")
        self.option_year.pack()

        self.label_output = tk.Label(self.parent, text="")
        self.label_output.pack()

        # Create the plot type radio buttons
        self.label_plot_type = tk.Label(self.parent, text="Choose plot type:")
        self.label_plot_type.pack()
        self.var_plot_type = tk.StringVar(self.parent)
        self.var_plot_type.set("Histogram")
        self.radio_histogram = tk.Radiobutton(self.parent, text="Histogram", variable=self.var_plot_type, value="Histogram")
        self.radio_histogram.pack()
        self.radio_everyday = tk.Radiobutton(self.parent, text="Everyday graph", variable=self.var_plot_type, value="Everyday")
        self.radio_everyday.pack()

        # Create the processing button
        self.button_process = tk.Button(self.parent, text="Plot Graph", command=self.process_data)
        self.button_process.pack()

        self.label_outline = tk.Label(self.parent, text="")
        self.label_outline.pack()

        self.avg_pm25_label = tk.Label(self.parent, text="Average PM2.5: ")
        self.avg_pm25_label = tk.Label(self.parent, text="Average PM2.5: ")
        self.avg_pm25_label.pack()
        self.max_pm25_label = tk.Label(self.parent, text="Maximum PM2.5: ")
        self.max_pm25_label.pack()
        self.min_pm25_label = tk.Label(self.parent, text="Minimum PM2.5: ")
        self.min_pm25_label.pack()
        self.std_pm25_label = tk.Label(self.parent, text="Standard Deviation PM2.5: ")
        self.std_pm25_label.pack()
        self.var_pm25_label = tk.Label(self.parent, text="Variance PM2.5: ")
        self.var_pm25_label.pack()

        self.analyze_button = tk.Button(self.parent, text="Analyze", command=self.analyze_data, state=tk.DISABLED)
        self.analyze_button.pack()

        # Create the output widgets
        self.label_output = tk.Label(self.parent, text="")
        self.label_output.pack()

        self.button_quit = tk.Button(self.parent, text="Quit", command=root.destroy)
        self.button_quit.pack()

    def browse_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.analyze_button.config(state=tk.NORMAL)


    def process_data(self):
        # Get the year value from the input widget
        year = int(self.var_year.get())

        # Read the CSV file
        df = pd.read_csv(self.file_path)

        # Process the data using NumPy and/or Pandas
        data = df[str(year)].values
        data = data[~np.isnan(data)]

        # Plot the data using Matplotlib
        if self.var_plot_type.get() == "Histogram":
            plt.hist(data, bins=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
            plt.xlabel("Range of pm2.5")
            plt.ylabel("Number of countries")
            plt.title(f"Histogram of pm2.5 values for {year}")
            plt.show()
        elif self.var_plot_type.get() == "Everyday":
            # plt.plot(df["Country Name"], df[str(year)])
            data = df[["Country Name", str(year)]].dropna()
            plt.plot(data["Country Name"], data[str(year)])
            plt.xlabel("Country")
            plt.ylabel("pm2.5 value")
            plt.title(f"Everyday graph of pm2.5 values for {year}")
            plt.xticks(rotation=90)
            plt.show()


    def analyze_data(self):
        df = pd.read_csv(self.file_path)
        year = int(self.var_year.get())
        data = df[str(year)].values
        data = data[~np.isnan(data)]
        self.label_outline["text"] = f"Data for {year} has been analyzed: "
        self.avg_pm25_label["text"] = f"Average PM2.5: {np.mean(data)}"
        self.max_pm25_label["text"] = f"Maximum PM2.5: {np.max(data)}"
        self.min_pm25_label["text"] = f"Minimum PM2.5: {np.min(data)}"
        self.std_pm25_label["text"] = f"Standard Deviation PM2.5: {np.std(data)}"
        self.var_pm25_label["text"] = f"Variance PM2.5: {np.var(data)}"



# Run the GUI
root = tk.Tk()
app = Application(parent=root)
app.mainloop()
