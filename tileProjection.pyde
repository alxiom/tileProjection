add_library("video")
    

def setup():
    size(900, 900)
    frameRate(30)
    background(0)
    
    global row_key, col_key
    global rows, cols, grids
    global row_key_pressed, col_key_pressed
    global playing, footage
    global grid_width, grid_height
    global grid_image, last_frame
    
    row_key = ["a", "b", "c"]
    col_key = ["1", "2", "3"]
    
    rows = len(row_key)
    cols = len(col_key)
    grids = rows * cols
    
    row_key_pressed = [False] * rows
    col_key_pressed = [False] * cols
    
    playing = [-1.0] * grids
    
    footage = Movie(this, "grid_test.mov")
    footage.loop()
    
    grid_width = width / cols
    grid_height = height / rows
    
    grid_image = loadImage("grid_image.jpg")
    last_frame = [grid_image.get()] * grids 


def draw():
    global playing, last_frame
    
    background(grid_image)
    
    for r, r_pressed in enumerate(row_key_pressed):
        if r_pressed:
            for c, c_pressed in enumerate(col_key_pressed):
                if c_pressed:
                    if playing[r * rows + c] < 0.0:
                        playing[r * rows + c] = 0.0
    
    blendMode(SCREEN)
    for i in range(grids):
        if playing[i] >= 0:
            footage.jump(playing[i])
            x_position = grid_width * (int(i % cols) - 1)
            y_position = grid_height * (int(i / rows) - 1)
            if footage.available():
                footage.read()
                footage.mask(footage)
                image(footage, x_position, y_position)
                last_frame[i] = footage.get()
            else:
                image(last_frame[i], x_position, y_position)
        
            playing[i] += 1.0 / frameRate
        
        if playing[i] >= footage.duration():
            background(grid_image)
            last_frame[i] = grid_image.get()
            playing[i] = -1
    
    # grid tag text
    textSize(20)
    text("A1", 150, 150)
    text("A2", 450, 150)
    text("A3", 750, 150)
    text("B1", 150, 450)
    text("B2", 450, 450)
    text("B3", 750, 450)
    text("C1", 150, 750)
    text("C2", 450, 750)
    text("C3", 750, 750)


def keyPressed():
    global row_key, col_key
    global row_key_pressed, col_key_pressed
    
    if key in row_key:
        row_key_pressed[row_key.index(key)] = True
    elif key in col_key:
        col_key_pressed[col_key.index(key)] = True
    else:
        pass


def keyReleased():
    global row_key, col_key
    global row_key_pressed, col_key_pressed
    
    if key in row_key:
        row_key_pressed[row_key.index(key)] = False
    elif key in col_key:
        col_key_pressed[col_key.index(key)] = False
    else:
        pass
