add_library("video")


def setup():
    size(900, 900)
    frameRate(30)
    background(0)
    
    global key_row, key_col
    global key_row_pressed, key_col_pressed
    global now_playing, footage
    global tile_width, tile_height
    
    key_row = ["a", "b", "c"]
    key_col = ["1", "2", "3"]
    
    key_row_pressed = [False] * len(key_row)
    key_col_pressed = [False] * len(key_col)
    
    now_playing = [[-1.0 for _ in key_row] for _ in key_col]
    
    footage = Movie(this, "grid_test.mov")
    footage.loop()
    
    tile_width = float(width) / len(key_col)
    tile_height = float(height) / len(key_row)


def draw():
    global now_playing
    
    for i, row_pressed in enumerate(key_row_pressed):
        if row_pressed:
            for j, col_pressed in enumerate(key_col_pressed):
                if col_pressed:
                    if now_playing[i][j] < 0.0:
                        now_playing[i][j] = 0.0

    for i in range(len(key_row)):
        for j in range(len(key_col)):
            if now_playing[i][j] >= 0:
                footage.jump(now_playing[i][j])
                if footage.available():
                    footage.read()
                    x_position = tile_width * (i - 1)
                    y_position = tile_height * (j - 1)
                    image(footage, x_position, y_position)
                now_playing[i][j] += 1.0 / frameRate
            
            if now_playing[i][j] >= footage.duration():
                background(0)
                now_playing[i][j] = -1                  


def keyPressed():
    global key_row, key_col
    global key_row_pressed, key_col_pressed
    
    if key in key_row:
        key_row_pressed[key_row.index(key)] = True
    elif key in key_col:
        key_col_pressed[key_col.index(key)] = True
    else:
        pass


def keyReleased():
    global key_row, key_col
    global key_row_pressed, key_col_pressed
    
    if key in key_row:
        key_row_pressed[key_row.index(key)] = False
    elif key in key_col:
        key_col_pressed[key_col.index(key)] = False
    else:
        pass
