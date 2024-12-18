import tkinter as tk
from tkinter import messagebox
import os

FILE_NAME = "employees.txt"

def load_employees():
    """Load employee data from a file."""
    employees = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            for line in file:
                emp_data = line.strip().split(',')
                employees.append({
                    'id': emp_data[0],
                    'name': emp_data[1],
                    'age': emp_data[2],
                    'department': emp_data[3]
                })
    return employees

def save_employees(employees):
    """Save employee data to a file."""
    with open(FILE_NAME, 'w') as file:
        for emp in employees:
            file.write(f"{emp['id']},{emp['name']},{emp['age']},{emp['department']}\n")

def validate_id(emp_id):
    """Validate if Employee ID is numeric."""
    if not emp_id.isdigit():
        messagebox.showerror("Error", "Employee ID must be numeric!")
        return False
    return True

class EmployeeManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.configure(bg="#f0f8ff")  # Light blue background
        self.employees = load_employees()

        # Main Frame
        self.main_frame = tk.Frame(root, padx=10, pady=10, bg="#f0f8ff")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Buttons with colors and styling
        button_font = ("Arial", 12, "bold")
        button_bg = "#4caf50"  # Green
        button_fg = "white"  # White text

        tk.Button(self.main_frame, text="Add Employee", command=self.add_employee_window, font=button_font, bg=button_bg, fg=button_fg).pack(fill=tk.X, pady=5)
        tk.Button(self.main_frame, text="View Employees", command=self.view_employees_window, font=button_font, bg=button_bg, fg=button_fg).pack(fill=tk.X, pady=5)
        tk.Button(self.main_frame, text="Update Employee", command=self.update_employee_window, font=button_font, bg=button_bg, fg=button_fg).pack(fill=tk.X, pady=5)
        tk.Button(self.main_frame, text="Delete Employee", command=self.delete_employee_window, font=button_font, bg=button_bg, fg=button_fg).pack(fill=tk.X, pady=5)
        tk.Button(self.main_frame, text="Exit", command=self.exit_application, font=button_font, bg="#f44336", fg=button_fg).pack(fill=tk.X, pady=5)  # Red for Exit

    def add_employee_window(self):
        """Open a window to add a new employee."""
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Employee")
        add_window.configure(bg="#e3f2fd")  # Light blue background

        label_font = ("Arial", 10, "bold")

        tk.Label(add_window, text="Employee ID:", font=label_font, bg="#e3f2fd").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(add_window, text="Name:", font=label_font, bg="#e3f2fd").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(add_window, text="Age:", font=label_font, bg="#e3f2fd").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(add_window, text="Department:", font=label_font, bg="#e3f2fd").grid(row=3, column=0, padx=5, pady=5)

        emp_id = tk.Entry(add_window)
        name = tk.Entry(add_window)
        age = tk.Entry(add_window)
        department = tk.Entry(add_window)

        emp_id.grid(row=0, column=1, padx=5, pady=5)
        name.grid(row=1, column=1, padx=5, pady=5)
        age.grid(row=2, column=1, padx=5, pady=5)
        department.grid(row=3, column=1, padx=5, pady=5)

        def add_employee():
            new_emp = {
                'id': emp_id.get().strip(),
                'name': name.get().strip(),
                'age': age.get().strip(),
                'department': department.get().strip()
            }

            if not validate_id(new_emp['id']):
                return

            if not new_emp['name'] or not new_emp['age'] or not new_emp['department']:
                messagebox.showerror("Error", "All fields are required!")
                return

            if any(emp['id'] == new_emp['id'] for emp in self.employees):
                messagebox.showerror("Error", "Employee ID already exists!")
                return

            self.employees.append(new_emp)
            save_employees(self.employees)
            messagebox.showinfo("Success", "Employee added successfully!")
            add_window.destroy()

        tk.Button(add_window, text="Add", command=add_employee, font=("Arial", 10, "bold"), bg="#4caf50", fg="white").grid(row=4, columnspan=2, pady=10)

    def view_employees_window(self):
        """Open a window to view all employees."""
        view_window = tk.Toplevel(self.root)
        view_window.title("View Employees")
        view_window.configure(bg="#fff3e0")  # Light orange background

        if not self.employees:
            tk.Label(view_window, text="No employees found.", font=("Arial", 12, "bold"), bg="#fff3e0").pack(pady=10)
            return

        for i, emp in enumerate(self.employees):
            tk.Label(view_window, text=f"ID: {emp['id']}, Name: {emp['name']}, Age: {emp['age']}, Department: {emp['department']}", font=("Arial", 10), bg="#fff3e0").pack(anchor=tk.W, padx=10, pady=2)

    def update_employee_window(self):
        """Open a window to update employee details."""
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Employee")
        update_window.configure(bg="#fce4ec")  # Light pink background

        tk.Label(update_window, text="Enter Employee ID to Update:", font=("Arial", 10, "bold"), bg="#fce4ec").grid(row=0, column=0, padx=5, pady=5)
        emp_id_entry = tk.Entry(update_window)
        emp_id_entry.grid(row=0, column=1, padx=5, pady=5)

        def update_employee():
            emp_id = emp_id_entry.get().strip()
            if not validate_id(emp_id):
                return
            for emp in self.employees:
                if emp['id'] == emp_id:
                    tk.Label(update_window, text="New Name:", font=("Arial", 10, "bold"), bg="#fce4ec").grid(row=1, column=0, padx=5, pady=5)
                    tk.Label(update_window, text="New Age:", font=("Arial", 10, "bold"), bg="#fce4ec").grid(row=2, column=0, padx=5, pady=5)
                    tk.Label(update_window, text="New Department:", font=("Arial", 10, "bold"), bg="#fce4ec").grid(row=3, column=0, padx=5, pady=5)

                    new_name = tk.Entry(update_window)
                    new_age = tk.Entry(update_window)
                    new_department = tk.Entry(update_window)

                    new_name.grid(row=1, column=1, padx=5, pady=5)
                    new_age.grid(row=2, column=1, padx=5, pady=5)
                    new_department.grid(row=3, column=1, padx=5, pady=5)

                    def save_update():
                        emp['name'] = new_name.get().strip() or emp['name']
                        emp['age'] = new_age.get().strip() or emp['age']
                        emp['department'] = new_department.get().strip() or emp['department']
                        save_employees(self.employees)
                        messagebox.showinfo("Success", "Employee updated successfully!")
                        update_window.destroy()

                    tk.Button(update_window, text="Save", command=save_update, font=("Arial", 10, "bold"), bg="#4caf50", fg="white").grid(row=4, columnspan=2, pady=10)
                    return
            messagebox.showerror("Error", "Employee ID not found!")

        tk.Button(update_window, text="Find", command=update_employee, font=("Arial", 10, "bold"), bg="#2196f3", fg="white").grid(row=5, columnspan=2, pady=10)

    def delete_employee_window(self):
        """Open a window to delete an employee."""
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Employee")
        delete_window.configure(bg="#fbe9e7")  # Light peach background

        tk.Label(delete_window, text="Enter Employee ID to Delete:", font=("Arial", 10, "bold"), bg="#fbe9e7").grid(row=0, column=0, padx=5, pady=5)
        emp_id_entry = tk.Entry(delete_window)
        emp_id_entry.grid(row=0, column=1, padx=5, pady=5)

        def delete_employee():
            emp_id = emp_id_entry.get().strip()
            if not validate_id(emp_id):
                return
            for i, emp in enumerate(self.employees):
                if emp['id'] == emp_id:
                    del self.employees[i]
                    save_employees(self.employees)
                    messagebox.showinfo("Success", "Employee deleted successfully!")
                    delete_window.destroy()
                    return
            messagebox.showerror("Error", "Employee ID not found!")

        tk.Button(delete_window, text="Delete", command=delete_employee, font=("Arial", 10, "bold"), bg="#f44336", fg="white").grid(row=1, columnspan=2, pady=10)

    def exit_application(self):
        """Exit the application."""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.destroy()

if __name__ == "__main__":import tkinter as tk
from tkinter import messagebox
import os

FILE_NAME = "employees.txt"

def load_employees():
    """Load employee data from a file."""
    employees = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            for line in file:
                emp_data = line.strip().split(',')
                employees.append({
                    'id': emp_data[0],
                    'name': emp_data[1],
                    'age': emp_data[2],
                    'department': emp_data[3]
                })
    return employees

def save_employees(employees):
    """Save employee data to a file."""
    with open(FILE_NAME, 'w') as file:
        for emp in employees:
            file.write(f"{emp['id']},{emp['name']},{emp['age']},{emp['department']}\n")

def is_valid_age(age):
    """Validate the age is a positive integer."""
    try:
        age = int(age)
        return age > 0
    except ValueError:
        return False

def is_valid_name(name):
    """Validate that the name only contains alphabets and spaces."""
    return all(c.isalpha() or c.isspace() for c in name)

class EmployeeManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.configure(bg="#f0f8ff")  # Light blue background
        self.employees = load_employees()

        # Main Frame
        self.main_frame = tk.Frame(root, padx=10, pady=10, bg="#f0f8ff")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Buttons with colors and styling
        button_font = ("Arial", 12, "bold")
        button_bg = "#4caf50"  # Green
        button_fg = "white"  # White text

        tk.Button(self.main_frame, text="Add Employee", command=self.add_employee_window, font=button_font, bg=button_bg, fg=button_fg).pack(fill=tk.X, pady=5)
        tk.Button(self.main_frame, text="View Employees", command=self.view_employees_window, font=button_font, bg=button_bg, fg=button_fg).pack(fill=tk.X, pady=5)
        tk.Button(self.main_frame, text="Update Employee", command=self.update_employee_window, font=button_font, bg=button_bg, fg=button_fg).pack(fill=tk.X, pady=5)
        tk.Button(self.main_frame, text="Delete Employee", command=self.delete_employee_window, font=button_font, bg=button_bg, fg=button_fg).pack(fill=tk.X, pady=5)
        tk.Button(self.main_frame, text="Exit", command=self.exit_application, font=button_font, bg="#f44336", fg=button_fg).pack(fill=tk.X, pady=5)  # Red for Exit

    def add_employee_window(self):
        """Open a window to add a new employee."""
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Employee")
        add_window.configure(bg="#e3f2fd")  # Light blue background

        label_font = ("Arial", 10, "bold")

        tk.Label(add_window, text="Employee ID:", font=label_font, bg="#e3f2fd").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(add_window, text="Name:", font=label_font, bg="#e3f2fd").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(add_window, text="Age:", font=label_font, bg="#e3f2fd").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(add_window, text="Department:", font=label_font, bg="#e3f2fd").grid(row=3, column=0, padx=5, pady=5)

        emp_id = tk.Entry(add_window)
        name = tk.Entry(add_window)
        age = tk.Entry(add_window)
        department = tk.Entry(add_window)

        emp_id.grid(row=0, column=1, padx=5, pady=5)
        name.grid(row=1, column=1, padx=5, pady=5)
        age.grid(row=2, column=1, padx=5, pady=5)
        department.grid(row=3, column=1, padx=5, pady=5)

        def add_employee():
            new_emp = {
                'id': emp_id.get().strip(),
                'name': name.get().strip(),
                'age': age.get().strip(),
                'department': department.get().strip()
            }

            if not new_emp['id'] or not new_emp['name'] or not new_emp['age'] or not new_emp['department']:
                messagebox.showerror("Error", "All fields are required!")
                return

            if not new_emp['id'].isdigit():
                messagebox.showerror("Error", "Employee ID must be a valid integer!")
                return

            if not is_valid_name(new_emp['name']):
                messagebox.showerror("Error", "Name must only contain letters and spaces!")
                return

            if not is_valid_age(new_emp['age']):
                messagebox.showerror("Error", "Age must be a positive integer!")
                return

            if any(emp['id'] == new_emp['id'] for emp in self.employees):
                messagebox.showerror("Error", "Employee ID already exists!")
                return

            self.employees.append(new_emp)
            save_employees(self.employees)
            messagebox.showinfo("Success", "Employee added successfully!")
            add_window.destroy()

        tk.Button(add_window, text="Add", command=add_employee, font=("Arial", 10, "bold"), bg="#4caf50", fg="white").grid(row=4, columnspan=2, pady=10)

    def view_employees_window(self):
        """Open a window to view all employees."""
        view_window = tk.Toplevel(self.root)
        view_window.title("View Employees")
        view_window.configure(bg="#fff3e0")  # Light orange background

        if not self.employees:
            tk.Label(view_window, text="No employees found.", font=("Arial", 12, "bold"), bg="#fff3e0").pack(pady=10)
            return

        for i, emp in enumerate(self.employees):
            tk.Label(view_window, text=f"ID: {emp['id']}, Name: {emp['name']}, Age: {emp['age']}, Department: {emp['department']}", font=("Arial", 10), bg="#fff3e0").pack(anchor=tk.W, padx=10, pady=2)

    def update_employee_window(self):
        """Open a window to update employee details."""
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Employee")
        update_window.configure(bg="#fce4ec")  # Light pink background

        tk.Label(update_window, text="Enter Employee ID to Update:", font=("Arial", 10, "bold"), bg="#fce4ec").grid(row=0, column=0, padx=5, pady=5)
        emp_id_entry = tk.Entry(update_window)
        emp_id_entry.grid(row=0, column=1, padx=5, pady=5)

        def update_employee():
            emp_id = emp_id_entry.get().strip()
            for emp in self.employees:
                if emp['id'] == emp_id:
                    tk.Label(update_window, text="New Name:", font=("Arial", 10, "bold"), bg="#fce4ec").grid(row=1, column=0, padx=5, pady=5)
                    tk.Label(update_window, text="New Age:", font=("Arial", 10, "bold"), bg="#fce4ec").grid(row=2, column=0, padx=5, pady=5)
                    tk.Label(update_window, text="New Department:", font=("Arial", 10, "bold"), bg="#fce4ec").grid(row=3, column=0, padx=5, pady=5)

                    new_name = tk.Entry(update_window)
                    new_age = tk.Entry(update_window)
                    new_department = tk.Entry(update_window)

                    new_name.grid(row=1, column=1, padx=5, pady=5)
                    new_age.grid(row=2, column=1, padx=5, pady=5)
                    new_department.grid(row=3, column=1, padx=5, pady=5)

                    def save_update():
                        if not is_valid_name(new_name.get().strip()):
                            messagebox.showerror("Error", "Name must only contain letters and spaces!")
                            return

                        if not is_valid_age(new_age.get().strip()):
                            messagebox.showerror("Error", "Age must be a positive integer!")
                            return

                        emp['name'] = new_name.get().strip() or emp['name']
                        emp['age'] = new_age.get().strip() or emp['age']
                        emp['department'] = new_department.get().strip() or emp['department']
                        save_employees(self.employees)
                        messagebox.showinfo("Success", "Employee updated successfully!")
                        update_window.destroy()

                    tk.Button(update_window, text="Save", command=save_update, font=("Arial", 10, "bold"), bg="#4caf50", fg="white").grid(row=4, columnspan=2, pady=10)
                    return
            messagebox.showerror("Error", "Employee ID not found!")

        tk.Button(update_window, text="Find", command=update_employee, font=("Arial", 10, "bold"), bg="#2196f3", fg="white").grid(row=5, columnspan=2, pady=10)

    def delete_employee_window(self):
        """Open a window to delete an employee."""
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Employee")
        delete_window.configure(bg="#fbe9e7")  # Light peach background

        tk.Label(delete_window, text="Enter Employee ID to Delete:", font=("Arial", 10, "bold"), bg="#fbe9e7").grid(row=0, column=0, padx=5, pady=5)
        emp_id_entry = tk.Entry(delete_window)
        emp_id_entry.grid(row=0, column=1, padx=5, pady=5)

        def delete_employee():
            emp_id = emp_id_entry.get().strip()
            for i, emp in enumerate(self.employees):
                if emp['id'] == emp_id:
                    del self.employees[i]
                    save_employees(self.employees)
                    messagebox.showinfo("Success", "Employee deleted successfully!")
                    delete_window.destroy()
                    return
            messagebox.showerror("Error", "Employee ID not found!")

        tk.Button(delete_window, text="Delete", command=delete_employee, font=("Arial", 10, "bold"), bg="#f44336", fg="white").grid(row=1, columnspan=2, pady=10)

    def exit_application(self):
        """Exit the application."""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagementApp(root)
    root.mainloop()

    root = tk.Tk()
    app = EmployeeManagementApp(root)
    root.mainloop()
