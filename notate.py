import os, sys, sdl2
import sdl2.ext
from input import Input


def run():  # entrypoint from main.py
    sdl2.ext.init()
    
    window = sdl2.ext.Window("notate", size=(640, 480))  # TODO: figure out resizable windows (later)
    window.show()
    
    # event loop function
    return notate(window)
    
    
def notate(window):
    renderer = sdl2.ext.renderer.Renderer(window)
    font = sdl2.ext.ttf.FontTTF(
        font=os.path.join(os.path.curdir, "res", "Red_Hat_Display", "static", "RedHatDisplay-Regular.ttf"),
        size=20,
        color=(255, 255, 255)
    )
    text_input = Input()
    running = True
    
    # event loop
    while running:
        events = sdl2.ext.get_events()
        
        for event in events:
            match event.type:
                case sdl2.SDL_QUIT:
                    running = False
                case sdl2.SDL_KEYDOWN:
                    text_input.append(event.key.keysym.sym)
                    texture = font.render_text(text_input.text)
                    renderer.copy(texture)
                    renderer.present()
                    
        window.refresh()
        
    return 0
    