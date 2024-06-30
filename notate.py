import os, sys, sdl2
import sdl2.ext
from input import Input


def run():  # entrypoint from main.py
    sdl2.ext.init()
    
    window = sdl2.ext.Window("notate", size=(640, 480))  # TODO: figure out resizable windows (later)
    window.show()
    
    # event loop function
    return notate(window)
    
    
def load_comps(window):
    renderer = sdl2.ext.renderer.Renderer(window, logical_size=(640, 480))
    renderer.color = (0, 0, 0)

    sprite_factory = sdl2.ext.SpriteFactory(renderer=renderer)
    
    font = sdl2.ext.ttf.FontTTF(
        font=os.path.join(os.path.curdir, "res", "Red_Hat_Display", "static", "RedHatDisplay-Regular.ttf"),
        size=120,
        color=(255, 255, 255)
    )

    text_input = Input()

    return renderer, sprite_factory, font, text_input


def notate(window):
    renderer, sprite_factory, font, text_input = load_comps(window)

    running = True
    
    # event loop
    while running:
        events = sdl2.ext.get_events()
        
        for event in events:
            match event.type:
                case sdl2.SDL_QUIT:
                    running = False
                case sdl2.SDL_KEYDOWN:
                    # print(event.key.keysym.sym)  # for debug stuff
                    text_input.handle_char(event.key.keysym.sym)

        texture = sprite_factory.from_surface(
            font.render_text(
                text_input.get_text() if text_input.text else "This document is empty...",
                width=640
            ),
            free=True
        )

        renderer.clear()
        renderer.copy(texture)
        renderer.present()
                    
        window.refresh()
        
    return 0
    