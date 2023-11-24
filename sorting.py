import tkinter as tk
import random
import time


def bubble_sort(input_list, visualize=False, canvas=None):
    n = len(input_list)

    for i in range(n):
        for j in range(0, n-i-1):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
                if visualize:
                    update_canvas(canvas, input_list, j, 'purple', j+1, 'pink')
                    canvas.update()
                    time.sleep(0.1)

def insertion_sort(input_list, visualize=False, canvas=None):
    for i in range(1, len(input_list)):
        key = input_list[i]
        j = i - 1
        while j >= 0 and key < input_list[j]:
            input_list[j + 1] = input_list[j]
            j -= 1
        input_list[j + 1] = key
        if visualize:
            update_canvas(canvas, input_list, j+1, 'purple', i, 'pink')
            canvas.update()
            time.sleep(0.1)

def selection_sort(input_list, visualize=False, canvas=None):
    for i in range(len(input_list)):
        min_index = i
        for j in range(i + 1, len(input_list)):
            if input_list[j] < input_list[min_index]:
                min_index = j
        input_list[i], input_list[min_index] = input_list[min_index], input_list[i]
        if visualize:
            update_canvas(canvas, input_list, i, 'purple', min_index, 'pink')
            canvas.update()
            time.sleep(0.1)

def merge_sort(input_list, visualize=False, canvas=None):
    if len(input_list) > 1:
        mid = len(input_list) // 2
        left_half = input_list[:mid]
        right_half = input_list[mid:]

        merge_sort(left_half, visualize, canvas)
        merge_sort(right_half, visualize, canvas)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                input_list[k] = left_half[i]
                i += 1
            else:
                input_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            input_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            input_list[k] = right_half[j]
            j += 1
            k += 1

        if visualize:
            update_canvas(canvas, input_list, i+j, 'purple', i, 'pink')
            canvas.update()
            time.sleep(0.1)

def update_canvas(canvas, heights, first, color_first, second, color_second):
    canvas.delete("all")
    bar_width = canvas_width / len(heights)
    for i, height in enumerate(heights):
        x1, y1 = i * bar_width, canvas_height - height * scale_factor
        x2, y2 = x1 + bar_width, canvas_height

        if i == first:

            fill_color = color_first

        elif i == second:

            fill_color = color_second
        else:

            fill_color = 'lightblue'

        canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)

def start_visualization(input_list):
    algorithm = algorithm_var.get()
    sorting_algorithms[algorithm](input_list.copy(), visualize=True, canvas=canvas)

def reset(input_list):

    canvas.delete("all")
    update_canvas(canvas, input_list, None, 'purple', None, 'pink')
    canvas.update_idletasks()

def initialize_window(input_list):

    canvas.delete("all")
    update_canvas(canvas, input_list, None, 'purple', None, 'pink')
    canvas.update_idletasks()


root = tk.Tk()
root.title("Sorting Visualizer")

screen_height = root.winfo_screenheight()
canvas_height = int(screen_height * 0.8)

scale_factor = canvas_height / 20

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

canvas_width = root.winfo_screenwidth() - 20
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

algorithm_var = tk.StringVar(root)
algorithm_var.set("Bubble Sort")
algorithm_menu = tk.OptionMenu(button_frame, algorithm_var, "Bubble Sort", "Insertion Sort", "Selection Sort", "Merge Sort")
algorithm_menu.pack(side=tk.LEFT, padx=5)

start_button = tk.Button(button_frame, text="Start Visualization", command=lambda: start_visualization(initial_list))
start_button.pack(side=tk.LEFT, padx=5)

reset_button = tk.Button(button_frame, text="Reset", command=lambda: reset(initial_list))
reset_button.pack(side=tk.LEFT, padx=5)

initial_list = list(range(1, 21))  # Numbers from 1 to 20 exactly once
random.shuffle(initial_list)

sorting_algorithms = {
    'Bubble Sort': bubble_sort,
    'Insertion Sort': insertion_sort,
    'Selection Sort': selection_sort,
    'Merge Sort': merge_sort,
}

initialize_window(initial_list)
root.mainloop()
