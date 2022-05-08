import pyxel

SCREEN_WIDTH  = 128
SCREEN_HEIGHT = 128
FPS = 30

ASSET_FILENAME    = "bouquet.pyxres"
TRANSPARENT_COLOR = 0 # 透明色：黒
COUNT_OF_FLOWERS  = 5  # 表示させる花の総数
global restart_flag

# クリックした場所に花を表示させるクラス
class Flowers:
    def __init__(self):
        self.points = []
        self.flower_width = 24
        self.flower_height = 24
    def update(self, mouse_x, mouse_y):
        self.points.append([mouse_x-(self.flower_width/2), mouse_y-(self.flower_height/2)])
    def draw(self):
        for num in range(len(self.points)): 
            pyxel.blt(*self.points[num], 1, (num%2)*self.flower_width, 0, self.flower_width, self.flower_height,TRANSPARENT_COLOR)

# 配置できる花の残数を表示するクラス
class TextCount:
    def __init__(self):
        pass
    def update(self):
        pass
    def draw(self,count):
        pyxel.blt(98, 12, 1, 0, 32, 7, 7,TRANSPARENT_COLOR)
        pyxel.text(108, 14, "x"+count, 5)

# 初期画面のテキストを表示するクラス
class TextClick:
    def __init__(self):
        pass
    def update(self):
        pass
    def draw(self):
        if (pyxel.frame_count // 20 % 2) == 0:
            pyxel.text(10, 32, "Click where to put a flower", 5)
        else:
            pass

# 完了画面のテキストを表示するクラス
class TextHappy:
    
    def __init__(self):
        self.color = 8 # 濃ピンク
        self.count = -1
        self.frame = 0
        self.char  = ["H","a","p","p","y"," ","M","o","t","h","e","r","'","s"," ","D","a","y","!"] 

    def update(self):
        global restart_flag
        self.frame += 1
        if self.count < len(self.char):
            if (self.frame % 3) == 0:
                self.count += 1
        else:
            if self.frame > len(self.char)+90: 
                restart_flag = True
            if (self.frame // 15 % 3) == 0:
                self.color = 8 # 濃ピンク
            if (self.frame // 15 % 3) == 1:
                self.color = 14 # 薄ピンク
            if (self.frame // 15 % 3) == 2:
                self.color = 10 # 黄色

    def draw(self):
        global restart_flag
        for num in range(self.count):
            pyxel.text((num*4)+27, 20, self.char[num], self.color)
        if restart_flag: 
            pyxel.text(31, 32, "Click to restart", 5)

class App:

    def __init__(self):
        global restart_flag
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, fps=FPS)
        pyxel.load(ASSET_FILENAME)
        restart_flag = False
        self.count = COUNT_OF_FLOWERS
        self.text_count = TextCount()
        self.text_click = TextClick()
        self.text_happy = TextHappy()
        self.flowers = Flowers()
        pyxel.run(self.update, self.draw)

    def update(self):
        global restart_flag
        if self.count > 0:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.count -= 1
                self.flowers.update(pyxel.mouse_x, pyxel.mouse_y)
        else:
            self.text_happy.update()
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and restart_flag:
                self.flowers = Flowers()
                self.text_happy = TextHappy()
                self.count = COUNT_OF_FLOWERS
                restart_flag = False

    def draw(self):
        pyxel.blt(0, 0, 0, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT,TRANSPARENT_COLOR)

        self.flowers.draw()

        if self.count > 0:
            if self.count == COUNT_OF_FLOWERS:
                self.text_click.draw()
            else:
                pass
            self.text_count.draw(str(self.count))
            pyxel.mouse(True)
        else:
            self.text_happy.draw()
            # pyxel.mouse(False)

App()