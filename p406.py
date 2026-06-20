import customtkinter as ctk
from tkinter import messagebox
from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId
from PIL import Image, ImageDraw
import requests
import io
import re


def round_corners(img, radius=20):
    """Apply rounded corners to a PIL image"""
    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0, 0), img.size], radius=radius, fill=255)
    img.putalpha(mask)
    return img

# from sqlalchemy.testing.suite.test_reflection import users

PRIMARY_COLOR = "#00b894"   # teal green
SECONDARY_COLOR = "#0984e3" # blue
DARK_BG = "#022c43"
CARD_BG = "#063b4c"
LIGHT_TEXT = "white"

# MongoDB Setup
client = MongoClient("mongodb://localhost:27017/")
db = client["Cart"]
member = db["member"]
categories = db["categories"]
products = db["products"]
items = db["cart_items"]
orders = db["my_orders"]


# App class using CustomTkinter
class ModernMongoApp:

    def __init__(self, root):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("black_white_theme.json")

        self.root = root
        self.root.title("🛍 Login")
        self.root.geometry("1190x840")
        self.root.configure(bg="#0b2c3d")
        self.show_pass = False

        self.frame = ctk.CTkFrame(root, corner_radius=25, fg_color="#022c43")
        self.frame.pack(expand=True, padx=60, pady=60, fill="both")

        self.build_login_ui()

    def add_signup_button_to_login(self):
        """Add this code below your login button in your main login window"""
        ctk.CTkButton(
            self.frame,  # or whatever frame contains your login button
            text="📝 Sign Up",
            width=200,
            height=45,
            command=self.show_signup_form,
            font=("Arial", 16, "bold"),
            fg_color="green",
            text_color="white",
            hover_color="#006600"
        ).pack(pady=10)

    def show_signup_form(self):
        """Show the sign-up form"""
        self.frame.destroy()
        self.signup_frame = ctk.CTkFrame(self.root, corner_radius=25, fg_color="#022c43")
        self.signup_frame.pack(expand=True, padx=60, pady=60, fill="both")

        # Header
        header_frame = ctk.CTkFrame(self.signup_frame, fg_color="transparent")
        header_frame.pack(fill="x", pady=(10, 20), padx=30)

        ctk.CTkLabel(header_frame, text="📝 Create New Account", font=("Arial", 28, "bold"), text_color="white").pack()

        # Main form container
        form_container = ctk.CTkFrame(self.signup_frame, fg_color="#063b4c", corner_radius=15)
        form_container.pack(pady=20, padx=40, fill="both", expand=True)

        # Form fields
        fields_frame = ctk.CTkFrame(form_container, fg_color="transparent")
        fields_frame.pack(pady=30, padx=30, fill="both", expand=True)

        # Username field
        ctk.CTkLabel(fields_frame, text="Username:", font=("Arial", 16, "bold"), text_color="white").pack(anchor="w",
                                                                                                          pady=(0, 5))
        self.signup_username = ctk.CTkEntry(fields_frame, width=400, height=40, font=("Arial", 14))
        self.signup_username.pack(pady=(0, 15))

        # Password field
        ctk.CTkLabel(fields_frame, text="Password:", font=("Arial", 16, "bold"), text_color="white").pack(anchor="w",pady=(0, 5))
        self.signup_password = ctk.CTkEntry(fields_frame, width=400, height=40, font=("Arial", 14), show="*")
        self.signup_password.pack(pady=(0, 15))

        # Confirm Password field
        ctk.CTkLabel(fields_frame, text="Confirm Password:", font=("Arial", 16, "bold"), text_color="white").pack(
            anchor="w", pady=(0, 5))
        self.signup_confirm_password = ctk.CTkEntry(fields_frame, width=400, height=40, font=("Arial", 14), show="*")
        self.signup_confirm_password.pack(pady=(0, 15))

        # Phone Number field
        ctk.CTkLabel(fields_frame, text="Phone Number:", font=("Arial", 16, "bold"), text_color="white").pack(
            anchor="w",
            pady=(0, 5))
        self.signup_pnumber = ctk.CTkEntry(fields_frame, width=400, height=40, font=("Arial", 14))
        self.signup_pnumber.pack(pady=(0, 15))

        # Email field
        ctk.CTkLabel(fields_frame, text="Email:", font=("Arial", 16, "bold"), text_color="white").pack(anchor="w",
                                                                                                       pady=(0, 5))
        self.signup_email = ctk.CTkEntry(fields_frame, width=400, height=40, font=("Arial", 14))
        self.signup_email.pack(pady=(0, 20))

        # Buttons frame
        buttons_frame = ctk.CTkFrame(fields_frame, fg_color="transparent")
        buttons_frame.pack(pady=20)

        # Sign Up button
        ctk.CTkButton(
            buttons_frame,
            text="Create Account",
            width=180,
            height=45,
            command=self.create_account,
            font=("Arial", 16, "bold"),
            fg_color="green",
            text_color="white",
            hover_color="#006600"
        ).pack(side="left", padx=10)

        # Back to Login button
        ctk.CTkButton(
            buttons_frame,
            text="Back to Login",
            width=180,
            height=45,
            command=self.back_to_login,
            font=("Arial", 16, "bold"),
            fg_color="gray",
            text_color="white",
            hover_color="#666666"
        ).pack(side="left", padx=10)

    def validate_email(self, email):
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def validate_phone(self, phone):
        """Validate phone number (basic validation)"""
        # Remove spaces and dashes
        phone = phone.replace(" ", "").replace("-", "")
        # Check if it's all digits and has reasonable length
        return phone.isdigit() and 10 <= len(phone) <= 15

    def create_account(self):
        """Create a new user account"""
        # Get all field values
        username = self.signup_username.get().strip()
        password = self.signup_password.get().strip()
        confirm_password = self.signup_confirm_password.get().strip()
        pnumber = self.signup_pnumber.get().strip()
        email = self.signup_email.get().strip()

        # Validation
        if not all([username, password, confirm_password, pnumber, email]):
            messagebox.showerror("Error", "Please fill in all fields")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        if len(password) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters long")
            return

        if not self.validate_email(email):
            messagebox.showerror("Error", "Please enter a valid email address")
            return

        if not self.validate_phone(pnumber):
            messagebox.showerror("Error", "Please enter a valid phone number")
            return

        # Check if username already exists
        if member.find_one({"username": username}):
            messagebox.showerror("Error", "Username already exists. Please choose a different username.")
            return

        # Check if email already exists
        if member.find_one({"email": email}):
            messagebox.showerror("Error", "Email already registered. Please use a different email.")
            return

        try:
            # Create new user document
            new_user = {
                "_id": ObjectId(),  # Generate new ObjectId
                "username": username,
                "password": password,  # Note: In production, you should hash passwords
                "pnumber": pnumber,
                "email": email
            }

            # Insert into database
            member.insert_one(new_user)

            messagebox.showinfo("Success",
                                f"Account created successfully!\nUsername: {username}\nYou can now log in with your credentials.")

            # Clear form fields
            self.signup_username.delete(0, "end")
            self.signup_password.delete(0, "end")
            self.signup_confirm_password.delete(0, "end")
            self.signup_pnumber.delete(0, "end")
            self.signup_email.delete(0, "end")

            # Go back to login
            self.back_to_login()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to create account: {str(e)}")

    def back_to_login(self):
        self.signup_frame.destroy()
        self.frame = ctk.CTkFrame(self.root, corner_radius=25, fg_color="#022c43")
        self.frame.pack(expand=True, padx=60, pady=60, fill="both")

        self.build_login_ui()



    def build_login_ui(self):

        ctk.CTkLabel(self.frame, text="USER LOGIN", font=("Arial", 28, "bold"), text_color="white").pack(pady=(40, 30))

        user_row = ctk.CTkFrame(self.frame, fg_color="#063b4c", corner_radius=25)
        user_row.pack(pady=15, padx=60, fill="x")
        ctk.CTkLabel(user_row, text="👤", font=("Arial", 22), width=50, text_color="white").pack(side="left", padx=10)
        self.username = ctk.CTkEntry(user_row, placeholder_text="Username", font=("Arial", 16), height=45)
        self.username.pack(side="left", expand=True, fill="x")

        pass_row = ctk.CTkFrame(self.frame, fg_color="#063b4c", corner_radius=25)
        pass_row.pack(pady=15, padx=60, fill="x")
        self.lock_icon = ctk.CTkLabel(pass_row, text="🔒", font=("Arial", 22), width=50, text_color="white")
        self.lock_icon.pack(side="left", padx=10)
        self.password = ctk.CTkEntry(pass_row, placeholder_text="Password", font=("Arial", 16), height=45, show="*")
        self.password.pack(side="left", expand=True, fill="x")

        self.pass_toggle = ctk.CTkButton(
            pass_row,
            text="🔒",
            width=30,
            height=30,
            command=self.toggle_password,
            fg_color="#063b4c",
            hover_color="#0a3c50",
            text_color="white",
            font=("Arial", 18)
        )
        self.pass_toggle.pack(side="right", padx=5)

        ctk.CTkButton(
            self.frame,
            text="LOGIN",
            command=self.login_user,
            font=("Arial", 18, "bold"),
            width=300,
            height=55,
            fg_color="white",
            text_color="black",
            hover_color="#d6d6d6"
        ).pack(pady=(30, 20))

        ctk.CTkButton(
            self.frame,  # or whatever frame contains your login button
            text="📝 Sign Up",
            width=200,
            height=45,
            command=self.show_signup_form,
            font=("Arial", 16, "bold"),
            fg_color="green",
            text_color="white",
            hover_color="#006600"
        ).pack(pady=10)

    def toggle_password(self):
        if self.show_pass:
            self.password.configure(show="*")
            self.pass_toggle.configure(text="🔒")
            self.lock_icon.configure(text="🔒")
        else:
            self.password.configure(show="")
            self.pass_toggle.configure(text="🔓")
            self.lock_icon.configure(text="🔓")
        self.show_pass = not self.show_pass

    def login_user(self):
        self.logged_in_user = self.username.get()
        password = self.password.get()

        if self.logged_in_user.lower() == "admin" and password == "admin":
            self.show_admin_dashboard()
            return

        user = member.find_one({"username": self.logged_in_user, "password": password})  # fixed line

        if user:
            messagebox.showinfo("Login Success", f"✅ Welcome, {user['username']}!")
            self.show_categories()
        else:
            messagebox.showerror("Error", "❌ Invalid credentials.")

    def logout_user(self):
        confirm = messagebox.askyesno("Logout", f"Are you sure you want to logout ?")
        if confirm:
            self.logged_in_user = None  # Clear user session

            # Clear all widgets from root
            for widget in self.root.winfo_children():
                widget.destroy()

            # Reset window title
            self.root.title("🛍 Login")

            # Recreate the original login frame
            self.frame = ctk.CTkFrame(self.root, corner_radius=25, fg_color="#022c43")
            self.frame.pack(expand=True, padx=60, pady=60, fill="both")

            # Build the login UI (this method already exists)
            self.build_login_ui()

    def show_admin_dashboard(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("Admin Dashboard")

        # Main layout
        main_frame = ctk.CTkFrame(self.root, fg_color="#1a1a1a")
        main_frame.pack(fill="both", expand=True, padx=40, pady=30)

        # Header
        header_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        header_frame.pack(fill="x", pady=(0, 20))

        ctk.CTkLabel(
            header_frame,
            text="🛠️ Admin Dashboard",
            font=("Arial", 26, "bold"),
            text_color="white"
        ).pack(side="left")

        # ✅ Single Logout Button
        logout_btn = ctk.CTkButton(
            header_frame,
            text="🚪 Logout",
            fg_color="red",
            hover_color="#cc0000",
            text_color="white",
            command=self.logout_user,
            width=80,
            height=35,
            font=("Arial", 14, "bold")
        )
        logout_btn.pack(side="right", padx=10)

        # Options Grid
        grid_frame = ctk.CTkFrame(main_frame, fg_color="#262626", corner_radius=12)
        grid_frame.pack(fill="both", expand=True, padx=20, pady=20)

        grid_frame.columnconfigure((0, 1), weight=1)
        grid_frame.rowconfigure((0, 1), weight=1)

        # ✅ Smaller Buttons
        admin_buttons = [
            ("👥 Manage Members", self.manage_members),
            ("📦 Manage Categories", self.manage_categories()),
            ("🧾 View Orders", self.view_all_orders),
        ]

        for i, (text, command) in enumerate(admin_buttons):
            btn = ctk.CTkButton(
                grid_frame,
                text=text,
                command=command,
                font=("Arial", 18, "bold"),
                width=240,
                height=60,
                fg_color="white",
                text_color="black",
                hover_color="#e0e0e0"
            )
            btn.grid(row=i // 2, column=i % 2, padx=30, pady=20, sticky="nsew")

    def manage_members(self):
        members_window = ctk.CTkToplevel(self.root)
        members_window.title("All Members")
        members_window.geometry("800x500")
        members_window.configure(fg_color="#000000")
        members_window.deiconify()
        members_window.lift()
        members_window.attributes("-topmost", True)
        members_window.after(100, lambda: members_window.attributes("-topmost", False))
        members_window.focus_set()

        heading = ctk.CTkLabel(members_window, text="👥 All Members", font=("Arial", 22, "bold"), text_color="white")
        heading.pack(pady=15)

        scroll_frame = ctk.CTkScrollableFrame(members_window, width=760, height=400, fg_color="#1a1a1a",
                                              corner_radius=10)
        scroll_frame.pack(padx=20, pady=10)

        headers = ["Username", "Email", "Phone", "Role"]
        for col, text in enumerate(headers):
            ctk.CTkLabel(scroll_frame, text=text, font=("Arial", 14, "bold"), text_color="#00ffff").grid(row=0,
                                                                                                         column=col,
                                                                                                         padx=10,
                                                                                                         pady=8)

        try:
            members = list(self.member.find())
            for i, member in enumerate(members, start=1):
                ctk.CTkLabel(scroll_frame, text=member.get("Username", "-"), text_color="white").grid(row=i, column=0,
                                                                                                      padx=10, pady=5)
                ctk.CTkLabel(scroll_frame, text=member.get("Email", "-"), text_color="white").grid(row=i, column=1,
                                                                                                   padx=10, pady=5)
                ctk.CTkLabel(scroll_frame, text=member.get("Phone", "-"), text_color="white").grid(row=i, column=2,
                                                                                                   padx=10, pady=5)
                ctk.CTkLabel(scroll_frame, text=member.get("Role", "-"), text_color="white").grid(row=i, column=3,
                                                                                                  padx=10, pady=5)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch members: {e}")

    def manage_categories(self):
        def view_products_for_category(cat_id, cat_name):
            product_window = ctk.CTkToplevel(self.root)
            product_window.title(f"Products in {cat_name}")
            product_window.geometry("800x600")
            product_window.configure(fg_color="#000000")
            product_window.deiconify()
            product_window.lift()
            product_window.attributes("-topmost", True)
            product_window.after(100, lambda: product_window.attributes("-topmost", False))
            product_window.focus_set()

            def refresh_products():
                for widget in product_frame.winfo_children():
                    widget.destroy()

                headers = ["Product Name", "Price", "", "", ""]
                for col, text in enumerate(headers):
                    ctk.CTkLabel(product_frame, text=text, font=("Arial", 14, "bold"), text_color="#00ffff").grid(row=0,
                                                                                                                  column=col,
                                                                                                                  padx=10,
                                                                                                                  pady=8)

                all_products = list(products.find({"category_id": cat_id}))
                for i, prod in enumerate(all_products, start=1):
                    ctk.CTkLabel(product_frame, text=prod.get("product_name", "-"), text_color="white").grid(row=i,
                                                                                                             column=0,
                                                                                                             padx=10,
                                                                                                             pady=5)
                    ctk.CTkLabel(product_frame, text=f"₹{prod.get('price', '-')}", text_color="white").grid(row=i,
                                                                                                            column=1,
                                                                                                            padx=10,
                                                                                                            pady=5)

                    ctk.CTkButton(
                        product_frame, text="Edit", width=60, font=("Arial", 12),
                        command=lambda p=prod: open_edit_product(p)
                    ).grid(row=i, column=2, padx=5)

                    ctk.CTkButton(
                        product_frame, text="Delete", width=60, fg_color="red", font=("Arial", 12),
                        command=lambda pid=prod["_id"]: delete_product(pid)
                    ).grid(row=i, column=3, padx=5)

            def open_edit_product(prod):
                add_win = ctk.CTkToplevel(product_window)
                add_win.title("Edit Product")
                add_win.geometry("400x250")
                add_win.configure(fg_color="#1a1a1a")
                add_win.deiconify()
                add_win.lift()
                add_win.attributes("-topmost", True)
                add_win.after(100, lambda: add_win.attributes("-topmost", False))
                add_win.focus_set()

                name_var = ctk.StringVar(value=prod.get("product_name", ""))
                price_var = ctk.DoubleVar(value=prod.get("price", 0))

                ctk.CTkLabel(add_win, text="Product Name", text_color="white").pack(pady=5)
                name_entry = ctk.CTkEntry(add_win, textvariable=name_var)
                name_entry.pack(pady=5)

                ctk.CTkLabel(add_win, text="Price", text_color="white").pack(pady=5)
                price_entry = ctk.CTkEntry(add_win, textvariable=price_var)
                price_entry.pack(pady=5)

                def update_product():
                    add_win.deiconify()
                    add_win.lift()
                    add_win.attributes("-topmost", True)
                    add_win.after(100, lambda: add_win.attributes("-topmost", False))
                    add_win.focus_set()
                    products.update_one({"_id": prod["_id"]},
                                        {"$set": {"product_name": name_var.get(), "price": price_var.get()}})
                    messagebox.showinfo("Success", "Product updated successfully!")
                    add_win.destroy()
                    refresh_products()

                ctk.CTkButton(add_win, text="Update", command=update_product).pack(pady=10)

            def delete_product(pid):
                products.delete_one({"_id": pid})
                messagebox.showinfo("Deleted", "Product deleted successfully")
                refresh_products()

            def open_add_product():
                add_win = ctk.CTkToplevel(product_window)
                add_win.title("Add Product")
                add_win.geometry("400x250")
                add_win.configure(fg_color="#1a1a1a")
                add_win.deiconify()
                add_win.lift()
                add_win.attributes("-topmost", True)
                add_win.after(100, lambda: add_win.attributes("-topmost", False))
                add_win.focus_set()

                name_var = ctk.StringVar()
                price_var = ctk.StringVar()

                ctk.CTkLabel(add_win, text="Product Name", text_color="white").pack(pady=5)
                name_entry = ctk.CTkEntry(add_win, textvariable=name_var)
                name_entry.pack(pady=5)

                ctk.CTkLabel(add_win, text="Price", text_color="white").pack(pady=5)
                price_entry = ctk.CTkEntry(add_win, textvariable=price_var)
                price_entry.pack(pady=5)

                def add_product():
                    add_win.deiconify()
                    add_win.lift()
                    add_win.attributes("-topmost", True)
                    add_win.after(100, lambda: add_win.attributes("-topmost", False))
                    add_win.focus_set()
                    name = name_var.get().strip()
                    try:
                        price = float(price_var.get())
                    except ValueError:
                        messagebox.showerror("Invalid Input", "Please enter a valid price (e.g. 99.99).")
                        return

                    if not name:
                        messagebox.showerror("Input Error", "Product name cannot be empty.")
                        return

                    new_product = {
                        "product_name": name,
                        "price": price,
                        "category_id": cat_id
                    }
                    products.insert_one(new_product)
                    messagebox.showinfo("Added", "Product added successfully!")
                    add_win.destroy()
                    refresh_products()

                ctk.CTkButton(add_win, text="Add", command=add_product).pack(pady=10)

            heading = ctk.CTkLabel(product_window, text=f"🚖 Products in {cat_name}", font=("Arial", 22, "bold"),
                                   text_color="white")
            heading.pack(pady=10)

            add_button = ctk.CTkButton(product_window, text="➕ Add Product", command=open_add_product)
            add_button.pack(pady=5)

            product_frame = ctk.CTkScrollableFrame(product_window, width=760, height=450, fg_color="#1a1a1a",
                                                   corner_radius=10)
            product_frame.pack(padx=20, pady=10)

            refresh_products()

        categories_window = ctk.CTkToplevel(self.root)
        categories_window.title("All Categories")
        categories_window.geometry("700x500")
        categories_window.configure(fg_color="#000000")
        categories_window.deiconify()
        categories_window.lift()
        categories_window.attributes("-topmost", True)
        categories_window.after(100, lambda: categories_window.attributes("-topmost", False))
        categories_window.focus_set()

        heading = ctk.CTkLabel(categories_window, text="📂 All Categories", font=("Arial", 22, "bold"),
                               text_color="white")
        heading.pack(pady=15)

        scroll_frame = ctk.CTkScrollableFrame(categories_window, width=660, height=400, fg_color="#1a1a1a",
                                              corner_radius=10)
        scroll_frame.pack(padx=20, pady=10)

        headers = ["Category Name", "Description", ""]
        for col, text in enumerate(headers):
            ctk.CTkLabel(scroll_frame, text=text, font=("Arial", 14, "bold"), text_color="#00ffff").grid(row=0,
                                                                                                         column=col,
                                                                                                         padx=10,
                                                                                                         pady=8)

        try:
            all_categories = list(categories.find())
            for i, cat in enumerate(all_categories, start=1):
                ctk.CTkLabel(scroll_frame, text=cat.get("category_name", "-"), text_color="white").grid(row=i, column=0,
                                                                                                        padx=10, pady=5)
                ctk.CTkLabel(scroll_frame, text=cat.get("description", "-"), text_color="white").grid(row=i, column=1,
                                                                                                      padx=10, pady=5)
                ctk.CTkButton(
                    scroll_frame,
                    text="View",
                    command=lambda cid=cat["_id"], cname=cat.get("category_name", ""): view_products_for_category(cid,
                                                                                                                  cname),
                    font=("Arial", 14),
                    width=80,
                    height=35,
                    fg_color="white",
                    text_color="black",
                    hover_color="#d6d6d6"
                ).grid(row=i, column=2, padx=10, pady=5)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch categories: {e}")

    def manage_orders(self):
        order_window = ctk.CTkToplevel(self.root)
        order_window.title("All Orders")
        order_window.geometry("900x500")
        order_window.configure(fg_color="#000000")
        order_window.deiconify()
        order_window.lift()
        order_window.attributes("-topmost", True)
        order_window.after(100, lambda: order_window.attributes("-topmost", False))
        order_window.focus_set()

        heading = ctk.CTkLabel(order_window, text="📦 All Orders", font=("Arial", 22, "bold"), text_color="white")
        heading.pack(pady=15)

        scroll_frame = ctk.CTkScrollableFrame(order_window, width=860, height=400, fg_color="#1a1a1a",
                                              corner_radius=10)
        scroll_frame.pack(padx=20, pady=10)

        headers = ["Order ID", "Username", "Product", "Quantity", "Total Price"]
        for col, text in enumerate(headers):
            header = ctk.CTkLabel(scroll_frame, text=text, font=("Arial", 14, "bold"), text_color="#00ffff")
            header.grid(row=0, column=col, padx=10, pady=8)

        try:
            orders = list(self.db.my_orders.find())
            for i, order in enumerate(orders, start=1):
                ctk.CTkLabel(scroll_frame, text=str(order.get("_id", "-")), text_color="white").grid(row=i, column=0,
                                                                                                     padx=10, pady=5)
                ctk.CTkLabel(scroll_frame, text=order.get("username", "-"), text_color="white").grid(row=i, column=1,
                                                                                                     padx=10, pady=5)
                ctk.CTkLabel(scroll_frame, text=order.get("product_name", "-"), text_color="white").grid(row=i,
                                                                                                         column=2,
                                                                                                         padx=10,
                                                                                                         pady=5)
                ctk.CTkLabel(scroll_frame, text=str(order.get("quantity", "-")), text_color="white").grid(row=i,
                                                                                                          column=3,
                                                                                                          padx=10,
                                                                                                          pady=5)
                ctk.CTkLabel(scroll_frame, text="₹" + str(order.get("total_price", "-")), text_color="white").grid(
                    row=i, column=4, padx=10, pady=5)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch orders: {e}")

    def view_all_orders(self):
        admin_window = ctk.CTkToplevel(self.root)
        admin_window.title("📦 All Orders")
        admin_window.geometry("1000x600")
        admin_window.configure(fg_color="#022c43")
        admin_window.deiconify()
        admin_window.lift()
        admin_window.attributes("-topmost", True)
        admin_window.after(100, lambda: admin_window.attributes("-topmost", False))
        admin_window.focus_set()

        ctk.CTkLabel(admin_window, text="📦 All Orders", font=("Arial", 24, "bold"), text_color="white").pack(pady=20)

        frame = ctk.CTkScrollableFrame(admin_window, fg_color="#022c43")
        frame.pack(fill="both", expand=True, padx=0, pady=0)

        headers = ctk.CTkFrame(frame, fg_color="#063b4c")
        headers.pack(fill="x", pady=(0, 5), padx=10)

        ctk.CTkLabel(headers, text="Order ID", font=("Arial", 14, "bold"), text_color="white", width=160).pack(
            side="left", padx=(10, 0))
        ctk.CTkLabel(headers, text="Product Name", font=("Arial", 14, "bold"), text_color="white", width=180).pack(
            side="left", padx=(10, 0))
        ctk.CTkLabel(headers, text="Qty", font=("Arial", 14, "bold"), text_color="white", width=80).pack(side="left",
                                                                                                         padx=(10, 0))
        ctk.CTkLabel(headers, text="Price", font=("Arial", 14, "bold"), text_color="white", width=100).pack(side="left",
                                                                                                            padx=(
                                                                                                            10, 0))
        ctk.CTkLabel(headers, text="Amount", font=("Arial", 14, "bold"), text_color="white", width=100).pack(
            side="left", padx=(10, 0))
        ctk.CTkLabel(headers, text="Date", font=("Arial", 14, "bold"), text_color="white", width=200).pack(side="left",
                                                                                                           padx=(10, 0))

        for order in orders.find():
            order_date = order.get("order_date")
            formatted_date = order_date.strftime("%d-%m-%Y %H:%M") if isinstance(order_date, datetime) else str(
                order_date)

            row = ctk.CTkFrame(frame, fg_color="#0a3c50")
            row.pack(fill="x", padx=10, pady=5)

            ctk.CTkLabel(row, text=str(order.get("_id")), font=("Arial", 13), text_color="white", width=160).pack(
                side="left", padx=(10, 0), pady=3)
            ctk.CTkLabel(row, text=order.get("product_name", ""), font=("Arial", 13), text_color="white",
                         width=180).pack(side="left", padx=(10, 0), pady=3)
            ctk.CTkLabel(row, text=str(order.get("quantity", "")), font=("Arial", 13), text_color="white",
                         width=80).pack(side="left", padx=(10, 0), pady=3)
            ctk.CTkLabel(row, text=str(order.get("price", "")), font=("Arial", 13), text_color="white", width=100).pack(
                side="left", padx=(10, 0), pady=3)
            ctk.CTkLabel(row, text=str(order.get("total", "")), font=("Arial", 13), text_color="white", width=100).pack(
                side="left", padx=(10, 0), pady=3)
            ctk.CTkLabel(row, text=formatted_date, font=("Arial", 13), text_color="white", width=200).pack(side="left",
                                                                                                           padx=(10, 0),
                                                                                                           pady=3)

    def show_categories(self):
        self.frame.destroy()

        self.cat_frame = ctk.CTkFrame(self.root, corner_radius=25, fg_color="#022c43")
        self.cat_frame.pack(expand=True, padx=60, pady=60, fill="both")

        top_row = ctk.CTkFrame(self.cat_frame, fg_color="transparent")
        top_row.pack(fill="x", pady=(10, 20), padx=30)

        ctk.CTkLabel(top_row, text="📦 Select a Category", font=("Arial", 28, "bold"), text_color="white").pack(
            side="left")

        # Add Logout Button for regular member
        ctk.CTkButton(
            top_row,
            text="🚪 Logout",
            width=100,
            height=45,
            command=self.logout_user,  # Same logout method
            font=("Arial", 16, "bold"),
            fg_color="red",
            text_color="white",
            hover_color="#cc0000"
        ).pack(side="right", padx=10)

        ctk.CTkButton(
            top_row,
            text="📜 My Orders",
            width=140,
            height=45,
            command=self.view_my_orders,
            font=("Arial", 18),
            fg_color="white",
            text_color="black",
            hover_color="#d6d6d6"
        ).pack(side="right", padx=10)

        ctk.CTkButton(
            top_row,
            text="🛒 Cart",
            width=100,
            height=45,
            command=self.view_cart,
            font=("Arial", 18),
            fg_color="white",
            text_color="black",
            hover_color="#d6d6d6"
        ).pack(side="right", padx=10)

        # Category box
        # cat_box = ctk.CTkFrame(self.cat_frame, fg_color="#063b4c", corner_radius=15)
        # cat_box.pack(pady=10, padx=40, fill="x")
        #
        # all_categories = list(categories.find())
        # for cat in all_categories:
        #     ctk.CTkLabel(cat_box, text="• " + cat["category_name"], font=("Arial", 18), text_color="white", anchor="w",
        #                  justify="left").pack(anchor="w", padx=20, pady=5)
        #
        # self.cat_frame.update_idletasks()
        # total_height = cat_box.winfo_height() + 310
        # self.cat_frame.configure(height=total_height)

        input_row = ctk.CTkFrame(self.cat_frame, fg_color="transparent")
        input_row.pack(pady=(20, 10))

        self.cat_options = [cat["category_name"] for cat in categories.find()]
        self.cat_var = ctk.StringVar(value=self.cat_options[0] if self.cat_options else "")

        ctk.CTkLabel(input_row, text="Select Category:", font=("Arial", 16), text_color="white", width=200).pack(
            side="left", padx=(0, 10))
        self.cat_dropdown = ctk.CTkOptionMenu(input_row, variable=self.cat_var, values=self.cat_options, width=400)
        self.cat_dropdown.pack(side="left")

        ctk.CTkButton(
            self.cat_frame,
            text="Show Products",
            command=self.show_products,
            font=("Arial", 14),
            width=180,
            height=45,
            fg_color="white",
            text_color="black",
            hover_color="#d6d6d6"
        ).pack(pady=(10, 20))

        self.result_frame = ctk.CTkScrollableFrame(self.cat_frame, fg_color="#0a3c50", corner_radius=15, width=890,
                                                   height=300)
        self.result_frame.pack(fill="both", expand=True, padx=40, pady=10)

    def show_products(self):
        # Clear previous results
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        # Get selected category
        name = self.cat_var.get().strip()
        category = categories.find_one({"category_name": {"$regex": f"^{name}$", "$options": "i"}})

        if not category:
            ctk.CTkLabel(self.result_frame, text="❌ Category not found.", text_color="red").pack(pady=10)
            return

        cat_id = category["_id"]
        self.products_list = list(products.find({"category_id": cat_id}))

        if self.products_list:
            for p in self.products_list:
                # Card container
                row = ctk.CTkFrame(self.result_frame, fg_color="#0f3a52", corner_radius=15)
                row.pack(fill="x", pady=15, padx=30)  # ✅ more padding

                # Product Image (with rounded corners)
                img_url = p.get("image_url")
                if img_url:
                    try:
                        response = requests.get(img_url)
                        pil_img = Image.open(io.BytesIO(response.content)).convert("RGBA")
                        pil_img = pil_img.resize((100, 100))  # Resize first
                        pil_img = round_corners(pil_img, radius=5)  # ✅ Rounded corners

                        ctk_img = ctk.CTkImage(light_image=pil_img, size=(100, 100))
                        img_label = ctk.CTkLabel(row, image=ctk_img, text="")
                        img_label.image = ctk_img
                        img_label.pack(side="left", padx=15, pady=15)
                    except:
                        ctk.CTkLabel(row, text="❌ Img", text_color="red").pack(side="left", padx=15)

                # Product Info
                info_frame = ctk.CTkFrame(row, fg_color="transparent")
                info_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

                ctk.CTkLabel(info_frame, text=p["product_name"],
                             font=("Arial", 18, "bold"), text_color="white").pack(anchor="w")
                ctk.CTkLabel(info_frame, text=f"₹{p['price']}",
                             font=("Arial", 16), text_color="#00ffcc").pack(anchor="w", pady=(5, 0))

                # Add to Cart button
                ctk.CTkButton(
                    row,
                    text="🛒 Add to Cart",
                    command=lambda prod_name=p['product_name']: self.add_to_cart(prod_name)
                ).pack(side="right", padx=20, pady=20)

        else:
            ctk.CTkLabel(self.result_frame, text="⚠️ No products found.",
                         font=("Arial", 15), text_color="white").pack()

    def add_to_cart(self, product_name):
        quantity = 1  # Default quantity since there's no slider

        # Find the product in the list (case-insensitive match)
        product = next(
            (p for p in self.products_list if p['product_name'].lower() == product_name.lower()),
            None
        )

        if not product:
            messagebox.showerror("Error", "Product not found in this category.")
            return

        total = product["price"] * quantity

        cart_item = {
            "username": self.logged_in_user,
            "product_name": product["product_name"],
            "price": product["price"],
            "quantity": quantity,
            "total": total
        }

        items.insert_one(cart_item)

        messagebox.showinfo(
            "Success",
            f"Added to cart: {product['product_name']} × {quantity} = ₹{total}"
        )

        # Optionally clear/reset cart data
        self.cart_data = []

    def view_cart(self):
        def delete_item(item_id, row_frame):
            items.delete_one({"_id": item_id})
            row_frame.destroy()
            refresh_cart()

        def refresh_cart():
            for widget in body_frame.winfo_children():
                widget.destroy()
            subtotal = 0
            updated_items = list(items.find({"username": self.logged_in_user}))
            for item in updated_items:
                row = ctk.CTkFrame(body_frame, fg_color="#0a3c50", corner_radius=12)
                row.pack(fill="x", padx=20, pady=6, ipady=8)

                ctk.CTkButton(
                    row, text="🗑", width=45, height=45,
                    fg_color="#9b111e", hover_color="#b31b1b",
                    font=("Arial", 16, "bold"), text_color="white",
                    command=lambda iid=item["_id"], r=row: delete_item(iid, r)
                ).pack(side="left", padx=10)

                ctk.CTkLabel(row, text=item["product_name"], font=("Arial", 15), text_color="white",
                             anchor="w", width=240).pack(side="left", padx=(5, 10))

                ctk.CTkLabel(row, text=str(item["quantity"]), font=("Arial", 15), text_color="white",
                             anchor="center", width=80).pack(side="left", padx=(0, 10))

                ctk.CTkLabel(row, text=f"₹{item['total']}", font=("Arial", 15, "bold"), text_color="#00ffcc",
                             anchor="e", width=100).pack(side="right", padx=(10, 20))

                subtotal += item["total"]

            subtotal_label.configure(text=f"🧾 Subtotal: ₹{subtotal}")

        def clear_cart():
            items.delete_many({"username": self.logged_in_user})
            refresh_cart()

        cart_window = ctk.CTkToplevel(self.root)
        cart_window.title("🛒 Your Cart")
        cart_window.geometry("760x600")
        cart_window.configure(fg_color="#022c43")

        cart_window.deiconify()  # ⬅ Ensure it's not minimized
        cart_window.lift()  # Bring to front
        cart_window.attributes("-topmost", True)
        cart_window.after(100, lambda: cart_window.attributes("-topmost", False))
        cart_window.focus_set()  # ⬅ Force focus

        ctk.CTkLabel(cart_window, text="🛒 Your Cart Items", font=("Arial", 24, "bold"), text_color="white").pack(
            pady=20)

        btn_frame = ctk.CTkFrame(cart_window, fg_color="transparent")
        btn_frame.pack(pady=10)

        checkout_btn = ctk.CTkButton(btn_frame, text="✔ Checkout", fg_color="#00b300", hover_color="#009900", width=120,
                                     command=lambda: self.checkout_cart(refresh_cart)
                                     )
        clear_btn = ctk.CTkButton(btn_frame, text="🧹 Clear Cart", fg_color="red", hover_color="#cc0000", width=120,
                                  command=clear_cart)
        refresh_btn = ctk.CTkButton(
            btn_frame,
            text="🔄 Refresh",
            fg_color="white",
            hover_color="#d6d6d6",
            text_color="black",
            width=120,
            command=self.view_cart
        )

        checkout_btn.grid(row=0, column=0, padx=10)
        clear_btn.grid(row=0, column=1, padx=10)
        refresh_btn.grid(row=0, column=2, padx=10)

        header_frame = ctk.CTkFrame(cart_window, fg_color="#063b4c", height=40)
        header_frame.pack(fill="x", padx=20)

        ctk.CTkLabel(header_frame, text="", width=45).pack(side="left")
        ctk.CTkLabel(header_frame, text="Product Name", font=("Arial", 16, "bold"), text_color="white", anchor="w",
                     width=240, padx=10).pack(side="left", padx=(0, 5))
        ctk.CTkLabel(header_frame, text="Qty", font=("Arial", 16, "bold"), text_color="white", width=100,
                     padx=10).pack(side="left", padx=(0, 5))
        ctk.CTkLabel(header_frame, text="Amount (₹)", font=("Arial", 16, "bold"), text_color="white", width=100,
                     anchor="e", padx=10).pack(side="right", padx=10)

        body_frame = ctk.CTkScrollableFrame(cart_window, fg_color="#022c43", height=340)
        body_frame.pack(fill="both", expand=True, padx=20, pady=10)

        subtotal_label = ctk.CTkLabel(cart_window, text="🧾 Subtotal: ₹0", font=("Arial", 18, "bold"),
                                      text_color="white")
        subtotal_label.pack(pady=(5, 15))

        refresh_cart()

    def checkout_cart(self, refresh_callback=None):
        cart_items = list(items.find({"username": self.logged_in_user}))

        if not cart_items:
            messagebox.showinfo("Cart", "🛒 Your cart is empty.")
            return

        for item in cart_items:
            order = item.copy()
            order["order_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            orders.insert_one(order)

        items.delete_many({"username": self.logged_in_user})
        self.cart_data = []
        messagebox.showinfo("Success", "✅ Order placed successfully!")

        # 🔄 Call the refresh function to update UI
        if refresh_callback:
            refresh_callback()

    def view_my_orders(self):
        order_window = ctk.CTkToplevel(self.root)
        order_window.title("📜 My Orders")
        order_window.geometry("900x550")
        order_window.configure(fg_color="#022c43")
        order_window.deiconify()  # Ensure it's not minimized
        order_window.lift()  # Bring to front
        order_window.attributes("-topmost", True)
        order_window.after(100, lambda: order_window.attributes("-topmost", False))
        order_window.focus_set()  # Set focus to it

        ctk.CTkLabel(order_window, text="📜 Your Orders", font=("Arial", 24, "bold"), text_color="white").pack(pady=20)

        frame = ctk.CTkScrollableFrame(order_window, fg_color="#022c43")
        frame.pack(fill="both", expand=True, padx=20, pady=10)

        headers = ctk.CTkFrame(frame, fg_color="#063b4c")
        headers.pack(fill="x", pady=(0, 5))

        ctk.CTkLabel(headers, text="Product Name", font=("Arial", 14, "bold"), text_color="white", width=200).pack(
            side="left")
        ctk.CTkLabel(headers, text="Qty", font=("Arial", 14, "bold"), text_color="white", width=80).pack(side="left")
        ctk.CTkLabel(headers, text="Price", font=("Arial", 14, "bold"), text_color="white", width=100).pack(side="left")
        ctk.CTkLabel(headers, text="Amount", font=("Arial", 14, "bold"), text_color="white", width=100).pack(
            side="left")
        ctk.CTkLabel(headers, text="Date", font=("Arial", 14, "bold"), text_color="white", width=200).pack(side="left")

        for order in orders.find({"username": self.logged_in_user}):
            row = ctk.CTkFrame(frame, fg_color="#0a3c50")
            row.pack(fill="x", pady=3, padx=5, ipady=6)

            ctk.CTkLabel(row, text=order.get("product_name", ""), font=("Arial", 13), text_color="white",
                         width=200).pack(side="left")
            ctk.CTkLabel(row, text=str(order.get("quantity", "")), font=("Arial", 13), text_color="white",
                         width=80).pack(side="left")
            ctk.CTkLabel(row, text=str(order.get("price", "")), font=("Arial", 13), text_color="white", width=100).pack(
                side="left")
            ctk.CTkLabel(row, text=str(order.get("total", "")), font=("Arial", 13), text_color="white", width=100).pack(
                side="left")
            ctk.CTkLabel(row, text=order.get("order_date", ""), font=("Arial", 13), text_color="white", width=200).pack(
                side="left")


# Run
root = ctk.CTk()
app = ModernMongoApp(root)
root.mainloop()
