"""Plays white noise indefinitely. Requires an mp3 in the same directory as the script."""

import pygame


def run():
    """Loads mp3 and runs in infinite loop."""
    pygame.mixer.init()
    pygame.mixer.music.load("shhh.mp3")
    # -1 is the magic value that plays the mp3 infinitely
    pygame.mixer.music.play(-1)

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


if __name__ == "__main__":
    run()
