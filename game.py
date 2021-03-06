import tkinter as tk


class Game:
    def __init__(self):
        self.root = tk.Tk()

        self.set_window()
        self.create_frame()
        self.create_widgets()

        self.root.mainloop()

    # 창 설정
    def set_window(self):
        window_width = 400
        window_height = 600
        window_x = 100
        window_y = 100
        window_background = 'black'

        self.root.title('Flying Attack')
        self.root.geometry('{0}x{1}+{2}+{3}'.format(window_width, window_height, window_x, window_y))
        self.root.configure(bg=window_background)
        self.root.resizable(False, False)

    # 위젯 생성
    def create_widgets(self):
        self.widget_score()
        self.widget_heart()
        self.widget_bomb()
        self.widget_stage()

    # 점수 표시
    def widget_score(self):
        pass

    # 목숨 표시
    def widget_heart(self):
        pass

    # 폭탄 표시
    def widget_bomb(self):
        pass

    # 스테이지 표시
    def widget_stage(self):
        pass
