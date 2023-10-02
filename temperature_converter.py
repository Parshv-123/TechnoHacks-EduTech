import tkinter as tk

def convert_temperature():
    try:
        temperature = float(entry.get())
        if var.get() == "Fahrenheit to Celsius":
            result.set(f"{(temperature - 32) * 5/9:.2f} °C")
        elif var.get() == "Celsius to Fahrenheit":
            result.set(f"{(temperature * 9/5) + 32:.2f} °F")
    except ValueError:
        result.set("Invalid input")

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")

# Create an entry field for temperature input
entry_label = tk.Label(window, text="Enter temperature:")
entry_label.pack()
entry = tk.Entry(window)
entry.pack()

# Create radio buttons to select the conversion direction
var = tk.StringVar()
var.set("Fahrenheit to Celsius")
radio_fahrenheit = tk.Radiobutton(window, text="Fahrenheit to Celsius", variable=var, value="Fahrenheit to Celsius")
radio_celsius = tk.Radiobutton(window, text="Celsius to Fahrenheit", variable=var, value="Celsius to Fahrenheit")
radio_fahrenheit.pack()
radio_celsius.pack()

# Create a button to perform the conversion
convert_button = tk.Button(window, text="Convert", command=convert_temperature)
convert_button.pack()

# Display the result
result = tk.StringVar()
result.set("")
result_label = tk.Label(window, textvariable=result)
result_label.pack()

# Start the GUI application
window.mainloop()
