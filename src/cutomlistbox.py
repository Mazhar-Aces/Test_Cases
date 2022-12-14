from tkinter import *


class CustomListBox(Listbox):

    def __init__(self, master=None, *args, **kwargs):
        Listbox.__init__(self, master, *args, **kwargs)

        self.bg = "white"
        self.fg = "black"
        self.h_bg = "lightblue"
        self.h_fg = "black"

        self.current = -1  # current highlighted item

        self.fill()

        self.bind("<Motion>", self.on_motion)
        self.bind("<Leave>", self.on_leave)

    def fill(self, number=[]):
        """Fills the listbox with some numbers"""
        for i,j in enumerate(number):
            self.insert(END, j)
            self.itemconfig(i, {"bg": self.bg})
            self.itemconfig(i, {"fg": self.fg})

    def reset_colors(self):
        """Resets the colors of the items"""
        for i,item in enumerate(self.get(0, END)):
            self.itemconfig(i, {"bg": self.bg})
            self.itemconfig(i, {"fg": self.fg})

    def set_highlighted_item(self, index):
        """Set the item at index with the highlighted colors"""
        self.itemconfig(index, {"bg": self.h_bg})
        self.itemconfig(index, {"fg": self.h_fg})    

    def on_motion(self, event):
        """Calls everytime there's a motion of the mouse"""
        # print(self.current)
        index = self.index("@%s,%s" % (event.x, event.y))
        print(index,'  ',self.current)
        if self.current != -1 and self.current != index:
            self.reset_colors()
            self.set_highlighted_item(index)
        elif self.current == -1:
            self.set_highlighted_item(index)
        self.current = index

    def on_leave(self, event):
        self.reset_colors()
        self.current = -1


if __name__ == "__main__":
    root = Tk()
    itemlist = ['a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d']
    My_list_object = CustomListBox(root)
    My_list_object.pack()
    My_list_object.fill(number=itemlist)

    root.mainloop()