import tkinter as tk
from PIL import Image, ImageTk


class Tutorial:
    def __init__(self):
        self.root = tk.Toplevel()

        self.set_window()
        self.create_frame()
        self.create_widgets()

        self.root.mainloop()

    # 창 설정
    def set_window(self):
        self.window_width = 300
        self.window_height = 400
        window_x = 150
        window_y = 130
        window_background = 'white'

        self.root.title('Tutorial')
        self.root.geometry('{0}x{1}+{2}+{3}'.format(self.window_width, self.window_height, window_x, window_y))
        self.root.configure(bg=window_background)
        self.root.resizable(False, False)

    # 프레임 생성
    def create_frame(self):
        self.frame_tutorial = tk.Frame(self.root,
                                  width=self.window_width,
                                  height=(self.window_height * 0.8))
        self.frame_tutorial.grid(row=0, column=0, pady=(0, self.window_height*0.05))
        self.frame_arrow = tk.Frame(self.root,
                                     width=self.window_width,
                                     height=(self.window_height * 0.1))
        self.frame_arrow.grid(row=1, column=0)

    # 위젯 생성
    def create_widgets(self):
        self.widget_tutorial()
        self.widget_arrow()

    # 튜토리얼 이미지 위젯
    def widget_tutorial(self):
        images_tutorial = []
        size = (self.window_width * 0.9, self.window_height * 0.9)
        for i in range(5):
            image_tutorial = Image.open('image/tuto ('+str(i+1)+').png')
            image_tutorial.thumbnail(size, Image.ANTIALIAS)
            image_tutorial = ImageTk.PhotoImage(image_tutorial)
            images_tutorial.append(image_tutorial)
        label_tutorial = tk.Label(self.frame_tutorial, image=images_tutorial[0], bg='green')
        label_tutorial.image = images_tutorial[0]
        label_tutorial.pack()

    # 페이지 화살표 위젯
    def widget_arrow(self):
        images_arrow = []
        size = (self.window_width * 0.3, self.window_height * 0.1)
        for i in range(2):
            image_arrow = Image.open('image/arrow ('+str(i+1)+').png')
            image_arrow.thumbnail(size, Image.ANTIALIAS)
            image_arrow = ImageTk.PhotoImage(image_arrow)
            images_arrow.append(image_arrow)
            button_arrow = tk.Button(self.frame_arrow,
                                     image=image_arrow)
            button_arrow.image = image_arrow
            button_arrow.grid(row=0, column=i, padx=self.window_width*0.1)

# Tutorial()