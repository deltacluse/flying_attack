import tkinter as tk
from PIL import Image, ImageTk

import window_develop as dev
import window_tutorial as tuto


class Main:
    def __init__(self):
        self.root = tk.Tk()

        self.set_window()
        self.create_frame()
        self.create_widgets()

        self.root.mainloop()

    # 창 설정
    def set_window(self):
        self.window_width = 400
        self.window_height = 600
        window_x = 100
        WINDOW_Y = 100
        window_background = 'white'

        self.root.title('Flying Attack')
        self.root.geometry('{0}x{1}+{2}+{3}'
                           .format(self.window_width, self.window_height, window_x, WINDOW_Y))
        self.root.configure(bg=window_background)
        self.root.resizable(False, False)

    # 프레임 생성
    def create_frame(self):
        self.frame_top = tk.Frame(self.root,
                                  width=self.window_width,
                                  height=(self.window_height/3))
        self.frame_top.grid(row=0, column=0)
        self.frame_middle = tk.Frame(self.root,
                                     width=self.window_width,
                                     height=(self.window_height/3))
        self.frame_middle.grid(row=1, column=0)
        self.frame_bottom = tk.Frame(self.root,
                                     width=self.window_width,
                                     height=(self.window_height/3))
        self.frame_bottom.grid(row=2, column=0)

    # 위젯 생성
    def create_widgets(self):
        self.widget_game_logo()
        self.widget_game_start()
        self.widget_tutorial()
        self.widget_version()
        self.widget_developer()

    # 게임 로고 라벨
    def widget_game_logo(self):
        size = 300, 150  # 원본 사이즈 : 520, 260
        image_game_logo = Image.open('game_logo.png')
        image_game_logo.thumbnail(size, Image.ANTIALIAS)
        image_game_logo = ImageTk.PhotoImage(image_game_logo)
        label_game_logo = tk.Label(self.frame_top,
                                   image=image_game_logo,
                                   bg='white')
        label_game_logo.image = image_game_logo
        label_game_logo.pack(pady=(110,0))

    # 게임 시작 버튼
    def widget_game_start(self):
        button_game_start = tk.Button(self.frame_middle,
                                      bg='red',
                                      text='Game Start',
                                      font=('D2Coding', 25))
        button_game_start.pack(pady=(50, 0))

    # 튜토리얼 버튼
    def widget_tutorial(self):
        button_game_start = tk.Button(self.frame_middle,
                                      bg='blue',
                                      text='Tutorial',
                                      font=('D2Coding', 25),
                                      command=lambda : tuto.Tutorial())
        button_game_start.pack(pady=(10, 0))

    # 버전 라벨
    def widget_version(self):
        n_version = 0.01
        label_version = tk.Label(self.frame_bottom,
                                 bg='white',
                                 text='Ver. ' + str(n_version),
                                 font=('D2Coding', 25))
        label_version.grid(row=0, column=0)

    # 제작자 버튼
    def widget_developer(self):
        button_developer = tk.Button(self.frame_bottom,
                                     bg='green',
                                     text='Develop',
                                     font=('D2Coding', 15),
                                     command=lambda: dev.Develop())
        button_developer.grid(row=0, column=1, padx=(30,0))


if __name__ == '__main__':
    main = Main()
