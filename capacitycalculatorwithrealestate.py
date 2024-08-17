import tkinter as tk

# Function to update the total real estate field from the side calculator
def update_real_estate():
    try:
        re1 = float(real_estate1_entry.get()) if real_estate1_entry.get() else 0
        re2 = float(real_estate2_entry.get()) if real_estate2_entry.get() else 0
        re3 = float(real_estate3_entry.get()) if real_estate3_entry.get() else 0
        re4 = float(real_estate4_entry.get()) if real_estate4_entry.get() else 0
        re5 = float(real_estate5_entry.get()) if real_estate5_entry.get() else 0
        total_real_estate = re1 + re2 + re3 + re4 + re5
        real_estate_entry.delete(0, tk.END)
        real_estate_entry.insert(0, f"{total_real_estate:.2f}")
    except ValueError:
        pass  # Ignore errors for empty or invalid entries

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

    # Reset the side calculator fields
    real_estate1_entry.delete(0, tk.END)
    real_estate2_entry.delete(0, tk.END)
    real_estate3_entry.delete(0, tk.END)
    real_estate4_entry.delete(0, tk.END)
    real_estate5_entry.delete(0, tk.END)

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

# Side calculator for Real Estate values
tk.Label(root, text="Real Estate Calculator").grid(row=0, column=2, padx=10, pady=5)
tk.Label(root, text="Real Estate 1:").grid(row=1, column=2, padx=10, pady=5)
real_estate1_entry = tk.Entry(root)
real_estate1_entry.grid(row=1, column=3, padx=10, pady=5)

tk.Label(root, text="Real Estate 2:").grid(row=2, column=2, padx=10, pady=5)
real_estate2_entry = tk.Entry(root)
real_estate2_entry.grid(row=2, column=3, padx=10, pady=5)

tk.Label(root, text="Real Estate 3:").grid(row=3, column=2, padx=10, pady=5)
real_estate3_entry = tk.Entry(root)
real_estate3_entry.grid(row=3, column=3, padx=10, pady=5)

tk.Label(root, text="Real Estate 4:").grid(row=4, column=2, padx=10, pady=5)
real_estate4_entry = tk.Entry(root)
real_estate4_entry.grid(row=4, column=3, padx=10, pady=5)

tk.Label(root, text="Real Estate 5:").grid(row=5, column=2, padx=10, pady=5)
real_estate5_entry = tk.Entry(root)
real_estate5_entry.grid(row=5, column=3, padx=10, pady=5)

# Bind events to update real estate field whenever the side calculator changes
for entry in [real_estate1_entry, real_estate2_entry, real_estate3_entry, real_estate4_entry, real_estate5_entry]:
    entry.bind("<KeyRelease>", lambda event: update_real_estate())

# Run the main loop
root.mainloop()
