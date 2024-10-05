import pygame as py

from algrothim import InsertionSort
import numpy as np

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

app = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = py.time.Clock()

arr = np.random.randint(2, 100, 30)

insertionSort = InsertionSort(arr, height_multiplier=5, window_size=app.get_size())


while True:
    for ev in py.event.get():
        if ev.type == py.QUIT:
            py.quit()
            exit()
        if ev.type == py.KEYDOWN:
            if ev.key == py.K_ESCAPE:
                py.quit()
                exit()
            if ev.key == py.K_s:
                insertionSort.sort()
            if ev.key == py.K_f:
                insertionSort.speed = 10 if insertionSort.speed == 60 else 60
            if ev.key == py.K_r:
                arr = np.random.randint(0, 100, 30)
                insertionSort.update(arr)
            if ev.key == py.K_n:
                insertionSort.next_step()
            if ev.key == py.K_g:
                insertionSort.sorting_is_paused = (
                    False if insertionSort.sorting_is_paused else True
                )

    app.fill(120)
    clock.tick(insertionSort.speed)

    insertionSort.run_sorting()

    insertionSort.draw(app, py)

    py.display.flip()
