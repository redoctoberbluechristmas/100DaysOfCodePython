from tkinter import *



window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)


def miles_to_km():
    km_value = float(miles_entry.get()) * 1.61
    output_label.config(text=f"{km_value}")
    #miles_value = int(miles_entry.get())
    #return miles_value * 1.61


# Miles input (Entry)
miles_entry = Entry(width=30)
miles_entry.grid(column=1, row=0)

# Cosmetic stuff. (Labels)
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Output (Label)
output_label = Label(text="")
output_label.grid(column=1, row=1)

# Calculate button (Button)
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)









window.mainloop()


