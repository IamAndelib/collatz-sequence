import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt


def collatz(limit):
    '''Generate Collatz sequence for a number'''
    sequence = [limit]
    while limit != 1:
        if limit % 2 == 0:
            limit = limit // 2
        else:
            limit = 3 * limit + 1
        sequence.append(limit)
    return sequence


def run_collatz(event=None):
    input_value = entry.get()
    if not input_value.isdigit():
        messagebox.showerror("Invalid Input", "Please enter a positive integer.")
        return

    user_lim = int(input_value)

    x_axis = []
    y_axis = []
    x2_axis = []
    y2_axis = []

    longest_sequence = []
    highest_number = 0
    highest_number_sequence = []

    output_text.delete("1.0", tk.END)

    for i in range(1, user_lim + 1):
        current_seq = collatz(i)
        if len(current_seq) > len(longest_sequence):
            longest_sequence = current_seq
        if max(current_seq) > highest_number:
            highest_number = max(current_seq)
            highest_number_sequence = current_seq

        output_text.insert(tk.END, f"{i}: {current_seq}\n\n")
        x_axis.append(i)
        y_axis.append(len(current_seq))
        x2_axis.append(i)
        y2_axis.append(max(current_seq))

    output_text.insert(tk.END, f"\nLongest sequence: {longest_sequence} "
                               f"(Starting at {longest_sequence[0]}, length {len(longest_sequence)})\n")
    output_text.insert(tk.END, f"Highest number in any sequence: {highest_number} "
                               f"(From {highest_number_sequence[0]})\n")

    # Plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.bar(x_axis, y_axis)
    ax1.set_xlabel('Numbers')
    ax1.set_ylabel('Length of Sequence')
    ax1.set_title('Number vs Sequence Length')

    ax2.plot(x2_axis, y2_axis)
    ax2.set_xlabel('Numbers')
    ax2.set_ylabel('Highest Number in Sequence')
    ax2.set_title('Number vs Max Value in Sequence')

    plt.tight_layout()
    plt.show()


# Tkinter GUI setup
root = tk.Tk()
root.title("Centered GUI Example")

# Main wrapper frame (fills the window)
main_frame = tk.Frame(root)
main_frame.pack(expand=True)

# Sub-frame to hold centered content
center_frame = tk.Frame(main_frame)
center_frame.pack()

# Label
label = tk.Label(center_frame, text="Enter an upper limit:")
label.pack(pady=5)

# Entry
entry = tk.Entry(center_frame, width=10)
entry.pack(pady=5)

# Button
run_button = tk.Button(center_frame, text="Run", command=run_collatz)
run_button.pack(pady=5)

# Bind <Return> key (Enter) to the run_collatz function
entry.bind("<Return>", run_collatz)

# Output text
output_text = tk.Text(center_frame, width=100, wrap="word")
output_text.pack(pady=5)

root.mainloop()
