class DraggableForm:
    def __init__(self, title):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.bind("<Button-1>", self.on_dragStart)
        self.root.bind("<B1-Motion>", self.on_drag)
        self.root.bind("<ButtonRelease-1>", self.on_drag_ends)
        # self.root.overrideredirect(True)  # Remove window decorations (title bar, minimize, maximize, close buttons)

        self.form_dragging_status = False  # Flag to track if the form is being dragged
        self.x_start = 0  # Initial x offset
        self.y_start = 0  # Initial y offset

    def on_dragStart(self, event):
        if not self.form_dragging_status:
            self.x_start = event.x
            self.y_start = event.y

    def on_drag(self, event):
        self.x_diff = event.x - self.x_start
        self.y_diff = event.y - self.y_start
        self.root.geometry(
            "+{0}+{1}".format(
                self.root.winfo_x() + self.x_diff, self.root.winfo_y() + self.y_diff
            )
        )
        self.form_dragging_status = True

    def on_drag_ends(self, event):
        self.form_dragging_status = False

    def run(self):
        self.root.mainloop()
