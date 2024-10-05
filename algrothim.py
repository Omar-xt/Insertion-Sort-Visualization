from dataclasses import dataclass, field


@dataclass
class InsertionSort:
    arr: list[int]
    offset_x: int = 0
    offset_y: int = 200
    width: int = 20
    spacing: int = 5
    height_multiplier: int = 5
    window_size: tuple[int, int] = field(default_factory=tuple)

    # -- sorting options
    speed: int = 60
    loop_count: int = 0
    current_reverse_index: int = -1
    next_reverse_index: int = -2
    arr_is_sorted: bool = False
    is_reverse: bool = False
    sorting_is_paused: bool = False

    def __post_init__(self):
        self.current_index = 0
        self.next_index = 1

        if not len(self.window_size):
            return

        min_offset_x = self.window_size[0] / 20
        arr_width = len(self.arr) * (self.width + self.spacing)

        offx = (self.window_size[0] - arr_width) / 2

        if offx < min_offset_x:
            offx = min_offset_x

            max_width = self.window_size[0] - (min_offset_x * 2)

            self.spacing = 2

            self.width = (max_width / len(self.arr)) - self.spacing

        self.offset_x = offx
        self.offset_y = self.window_size[1] - 50

    def swap(self, i, j):
        temp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = temp

    def update(self, arr):
        self.arr = arr

        self.reset()
        self.__post_init__()

    def reset(self):
        self.current_reverse_index = -1
        self.next_reverse_index = -2
        self.arr_is_sorted = False
        self.is_reverse = False
        self.sorting_is_paused = True
        self.loop_count = 0

    def sort(self):
        loop_count = 0
        for i in range(len(self.arr)):
            if self.next_index == len(self.arr):
                break

            if self.arr[self.current_index] < self.arr[self.next_index]:
                self.current_index = self.next_index
                self.next_index += 1
                continue

            self.swap(self.current_index, self.next_index)
            loop_count += 1

            reverse_index = self.current_index

            for j in range(reverse_index - 1, -1, -1):
                if self.arr[reverse_index] > self.arr[j]:
                    break

                self.swap(j, reverse_index)

                reverse_index -= 1
                loop_count += 1

            self.current_index = self.next_index
            self.next_index += 1

        print(f"sorted in {loop_count} moves..!")

    def next_step(self):
        if self.arr_is_sorted:
            return

        if self.next_index == len(self.arr):
            self.arr_is_sorted = True
            print(f"sorted in {self.loop_count} moves.")
            return

        if self.is_reverse:
            if self.arr[self.current_reverse_index] > self.arr[self.next_reverse_index]:
                self.is_reverse = False
                return
            elif self.next_reverse_index == -1:
                self.is_reverse = False
                return

            self.swap(self.next_reverse_index, self.current_reverse_index)
            self.current_reverse_index = self.next_reverse_index
            self.next_reverse_index -= 1
            self.loop_count += 1
            return

        if self.arr[self.current_index] <= self.arr[self.next_index]:
            self.current_index = self.next_index
            self.next_index += 1
            return

        self.swap(self.current_index, self.next_index)
        self.loop_count += 1
        self.is_reverse = True
        self.current_reverse_index = self.current_index
        self.next_reverse_index = self.current_reverse_index - 1

    def run_sorting(self):
        if self.arr_is_sorted or self.sorting_is_paused:
            return

        self.next_step()

    def draw(self, app, py):
        for ind, item in enumerate(self.arr):
            color = "green"
            x = ind * (self.width + self.spacing) + self.offset_x
            height = item * self.height_multiplier
            if ind == self.current_index:
                color = "brown"
            if self.is_reverse and ind == self.current_reverse_index:
                color = "red"
            py.draw.rect(
                app,
                color,
                (x, self.offset_y - height, self.width, item * self.height_multiplier),
            )
