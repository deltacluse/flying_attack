import tkinter as tk


class Develop:
    def __init__(self):
        self.root = tk.Tk()

        self.set_window()
        self.create_frame()
        self.create_widgets()

        self.root.mainloop()

    # 창 설정
    def set_window(self):
        self.window_width = 300
        self.window_height = 500
        window_x = 150
        window_y = 130
        window_background = 'white'

        self.root.title('Develop & Version')
        self.root.geometry('{0}x{1}+{2}+{3}'
                           .format(self.window_width, self.window_height, window_x, window_y))
        self.root.configure(bg=window_background)
        self.root.resizable(False, False)

    # 프레임 생성
    def create_frame(self):
        self.frame_developer = tk.Frame(self.root,
                                  width=self.window_width,
                                  height=(self.window_height * 0.2))
        self.frame_developer.grid(row=0, column=0)
        self.frame_version = tk.Frame(self.root,
                                     width=self.window_width,
                                     height=(self.window_height * 0.8))
        self.frame_version.grid(row=1, column=0)

    # 위젯 생성
    def create_widgets(self):
        self.widget_developer()
        self.widget_version()

    # 개발자 소개
    def widget_developer(self):
        pass

    # 버전 소개
    def widget_version(self):
        pass
