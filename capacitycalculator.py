import tkinter as tk

# Function to calculate capacity
def calculate_capacity():
    try:
        real_estate = float(real_estate_entry.get())
        income = float(income_entry.get()) * 5
        stock = float(stock_entry.get())
        other_assets = float(other_assets_entry.get())
        
        total_assets = real_estate + income + stock + other_assets
        percentage = slider.get() / 100
        capacity = total_assets * percentage
        
        result_label.config(text=f"Total Assets: ${total_assets:,.2f}\nCapacity ({slider.get()}%): ${capacity:,.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numeric values.")

# Function to reset all fields
def reset_fields():
    real_estate_entry.delete(0, tk.END)
    income_entry.delete(0, tk.END)
    stock_entry.delete(0, tk.END)
    other_assets_entry.delete(0, tk.END)
    slider.set(1)
    result_label.config(text="Total Assets:\nCapacity:")

# Create the main window
root = tk.Tk()
root.title("Prospect Research Capacity Calculator")

# Real Estate input
tk.Label(root, text="Total Real Estate Value:").grid(row=0, column=0, padx=10, pady=5)
real_estate_entry = tk.Entry(root)
real_estate_entry.grid(row=0, column=1, padx=10, pady=5)

# Income input
tk.Label(root, text="Income:").grid(row=1, column=0, padx=10, pady=5)
income_entry = tk.Entry(root)
income_entry.grid(row=1, column=1, padx=10, pady=5)

# Stock input
tk.Label(root, text="Stock Value:").grid(row=2, column=0, padx=10, pady=5)
stock_entry = tk.Entry(root)
stock_entry.grid(row=2, column=1, padx=10, pady=5)

# Other Assets input
tk.Label(root, text="Other Assets:").grid(row=3, column=0, padx=10, pady=5)
other_assets_entry = tk.Entry(root)
other_assets_entry.grid(row=3, column=1, padx=10, pady=5)

# Slider for capacity percentage
tk.Label(root, text="Capacity Percentage:").grid(row=4, column=0, padx=10, pady=5)
slider = tk.Scale(root, from_=1, to=10, orient='horizontal')
slider.grid(row=4, column=1, padx=10, pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_capacity)
calculate_button.grid(row=5, columnspan=2, pady=10)

# Reset button
reset_button = tk.Button(root, text="Reset", command=reset_fields)
reset_button.grid(row=6, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="Total Assets:\nCapacity:")
result_label.grid(row=7, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
