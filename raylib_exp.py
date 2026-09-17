from pyray import  * 
init_window(800, 400, "Hello window")
while not window_should_close():
    begin_drawing()
    clear_background(WHITE)
    draw_text("Hello world!", 90, 200, 200, BLUE)
    end_drawing()
close_window()
