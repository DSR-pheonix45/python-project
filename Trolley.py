from functools import lru_cache
import tkinter as tk

coins = (1, 2, 5, 10, 20, 50, 100, 200)

@lru_cache(maxsize=None)
def n_ways(target, max_coin):
    if target == 0:
        return 1
    if target > 0:
        return sum(n_ways(target - coin, coin) for coin in coins if coin <= max_coin if target - coin >= 0)
    raise ValueError

def solve_trolley_problem(target, max_coin):
    return n_ways(target, max_coin)

def generate_gui():
    root = tk.Tk()
    root.title("Trolley Problem Solver")

    target_label = tk.Label(root, text="Enter target amount:")
    target_label.pack()

    target_entry = tk.Entry(root)
    target_entry.pack()

    max_coin_label = tk.Label(root, text="Enter maximum coin value:")
    max_coin_label.pack()

    max_coin_entry = tk.Entry(root)
    max_coin_entry.pack()

    def solve_problem():
        target = int(target_entry.get())
        max_coin = int(max_coin_entry.get())
        result = solve_trolley_problem(target, max_coin)
        result_label.config(text=f"There are {result} ways to make {target}p with coins up to {max_coin}p.")

    solve_button = tk.Button(root, text="Solve", command=solve_problem)
    solve_button.pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()

generate_gui() 