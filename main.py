

import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

class BookTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Tracker Pro")
        self.root.geometry("750x550")
        
        self.books = []
        self.file_path = "books.json"
        
        self.setup_ui()
        self.load_data()

    def setup_ui(self):
        