import tkinter as tk
from tkinter import messagebox
import json

class ChefsDelightApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Recipe Repository")

        # Initialize recipes
        self.recipes = self.load_recipes()

        # Create title label
        self.title_label = tk.Label(self.master, text="Recipe Repository", font=("Helvetica", 24), fg="#b03060")
        self.title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Create widgets
        self.recipe_listbox = tk.Listbox(self.master, width=40, height=10)
        self.recipe_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.add_button = tk.Button(self.master, text="Add Recipe", command=self.add_recipe, bg="red")
        self.add_button.grid(row=2, column=0, padx=5, pady=5)

        self.view_button = tk.Button(self.master, text="View Ingredients", command=self.view_recipe, bg="light blue")
        self.view_button.grid(row=2, column=1, padx=5, pady=5)

        self.edit_button = tk.Button(self.master, text="Edit Recipe", command=self.edit_recipe, bg="maroon", fg="white")
        self.edit_button.grid(row=3, column=0, padx=5, pady=5)

        self.delete_button = tk.Button(self.master, text="Delete Recipe", command=self.delete_recipe, bg="pink")
        self.delete_button.grid(row=3, column=1, padx=5, pady=5)

        self.quit_button = tk.Button(self.master, text="Quit", command=self.quit_app, bg="lavender")
        self.quit_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.update_recipe_listbox()

    def add_recipe(self):
        name = input("Enter recipe name: ")
        ingredients = input("Enter ingredients (separated by commas): ").split(',')
        self.recipes.append({'name': name, 'ingredients': ingredients})
        self.update_recipe_listbox()
        self.save_recipes()

    def view_recipe(self):
        selected_index = self.recipe_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            recipe = self.recipes[index]
            messagebox.showinfo(recipe['name'], '\n'.join(recipe['ingredients']))
        else:
            messagebox.showerror("Error", "Please select a recipe to view.")

    def edit_recipe(self):
        selected_index = self.recipe_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            recipe = self.recipes[index]
            new_name = input("Enter new name for the recipe: ")
            new_ingredients = input("Enter new ingredients for the recipe (separated by commas): ").split(',')
            self.recipes[index] = {'name': new_name, 'ingredients': new_ingredients}
            self.update_recipe_listbox()
            self.save_recipes()
        else:
            messagebox.showerror("Error", "Please select a recipe to edit.")

    def delete_recipe(self):
        selected_index = self.recipe_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.recipes[index]
            self.update_recipe_listbox()
            self.save_recipes()
        else:
            messagebox.showerror("Error", "Please select a recipe to delete.")

    def update_recipe_listbox(self):
        self.recipe_listbox.delete(0, tk.END)
        for recipe in self.recipes:
            self.recipe_listbox.insert(tk.END, recipe['name'])

    def save_recipes(self):
        with open('recipes.json', 'w') as f:
            json.dump(self.recipes, f)

    def load_recipes(self):
        try:
            with open('recipes.json', 'r') as f:
                recipes = json.load(f)
        except FileNotFoundError:
            recipes = []
        return recipes

    def quit_app(self):
        self.save_recipes()
        self.master.quit()

def main():
    root = tk.Tk()
    app = ChefsDelightApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()



