import tkinter as tk


class Temp:
    def __init__(self):
        self.root = tk.Tk()

        self.set_window()
        self.create_frame()
        self.create_widgets()

        self.root.mainloop()

    # 창 설정
    def set_window(self):
        self.window_width = 100
        self.window_height = 100
        window_x = 100
        window_y = 100
        window_background = 'white'

        self.root.title('Template')
        self.root.geometry('{0}x{1}+{2}+{3}'
                           .format(self.window_width, self.window_height, window_x, window_y))
        self.root.configure(bg=window_background)
        self.root.resizable(False, False)

    # 프레임 생성
    def create_frame(self):
        self.frame_temp1 = tk.Frame(self.root,
                                  width=self.window_width,
                                  height=(self.window_height * 0.2))
        self.frame_temp1.pack(fill='y')
        self.frame_temp2 = tk.Frame(self.root,
                                     width=self.window_width,
                                     height=(self.window_height * 0.8))
        self.frame_temp2.pack(fill='y')

    # 위젯 생성
    def create_widgets(self):
        self.widget_temp1()
        self.widget_temp2()

    # 위젯 1
    def widget_temp1(self):
        pass

    # 위젯 2
    def widget_temp2(self):
        pass
