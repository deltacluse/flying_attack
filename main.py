import tkinter as tk
from PIL import Image, ImageTk


class Main:
    def __init__(self, root):
        self.root = root
        self.set_window()
        self.create_widgets()

    # 창 설정
    def set_window(self):
        window_width = 400
        window_height = 600
        window_x = 100
        window_y = 100
        window_background = 'white'

        self.root.title('Flying Attack')
        self.root.geometry('{0}x{1}+{2}+{3}'.format(window_width, window_height, window_x, window_y))
        self.root.configure(bg=window_background)
        self.root.resizable(False, False)

    # 위젯 생성
    def create_widgets(self):
        self.widget_game_logo()
        self.widget_game_start()
        self.widget_tutorial()
        self.widget_version()

    # 게임 로고 라벨
    def widget_game_logo(self):
        size = 300, 150  # 원본 사이즈 : 520, 260
        image_game_logo = Image.open('game_logo.png')
        image_game_logo.thumbnail(size, Image.ANTIALIAS)
        image_game_logo = ImageTk.PhotoImage(image_game_logo)
        label_game_logo = tk.Label(self.root,
                                   image=image_game_logo,
                                   bg='white')
        label_game_logo.image = image_game_logo
        label_game_logo.pack(pady=(110,0))

    # 게임 시작 버튼
    def widget_game_start(self):
        button_game_start = tk.Button(self.root,
                                      bg='red',
                                      text='Game Start',
                                      font=('D2Coding', 25))
        button_game_start.pack(pady=(50, 0))

    # 튜토리얼 버튼
    def widget_tutorial(self):
        button_game_start = tk.Button(self.root,
                                      bg='blue',
                                      text='Tutorial',
                                      font=('D2Coding', 25))
        button_game_start.pack(pady=(10, 0))

    # 버전 라벨
    def widget_version(self):
        n_version = 0.01
        label_version = tk.Label(self.root,
                                 bg='green',
                                 text='Ver. ' + str(n_version),
                                 font=('D2Coding', 25))
        label_version.pack(pady=(100, 0))


if __name__ == '__main__':
    root = tk.Tk()
    main = Main(root)
    root.mainloop()
