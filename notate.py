import sys
import sdl2
import sdl2.ext


def run():  # entrypoint from main.py
    sdl2.ext.init()
    
    window = sdl2.ext.Window("notate", size=(640, 480))  # TODO: figure out resizable windows (later)
    window.show()
    
    # event loop function
    return notate(window)
    
    
def notate(window):
    running = True
    
    # event loop
    while running:
        events = sdl2.ext.get_events()
        
        for event in events:
            match event.type:
                case sdl2.SDL_QUIT:
                    running = False
                case sdl2.SDL_KEYDOWN:
                    pass
                    
        window.refresh()
        
    return 0
    