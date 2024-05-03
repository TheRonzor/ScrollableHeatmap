import src.constants as c

import os
import numpy as np
from IPython.display import clear_output
from scipy.signal import convolve2d as conv


class DataGenerator:
    def __init__(self):
        '''
        Generates the fake data upon class instantiation
        '''
        frame=None
        for t in range(N_FRAMES):
            clear_output(wait=True)
            print(f'Generating frame {t+1}')
            frame = self.get_next_frame(frame)
            self.save_frame(frame, t)
        return

    def get_next_frame(self,
                       arr: np.ndarray = None
                      ) -> np.ndarray:
        '''
        Some old cellular automata code (just so we have something to look at)
        '''
        if arr is None:
            arr = np.zeros(shape=(DIMS))
            for r in [2,3,4]:
                arr[DIMS[0]//r, DIMS[1]//r] = 1
            arr = np.random.random(size=DIMS) < 0.001
        n = 5
        kernel = np.array([
            [1,1,1],
            [1,0,1],
            [1,1,1]
            ])
        new_arr = conv(arr, kernel, 'same') % n
        return new_arr

    def save_frame(self,
                   arr: np.ndarray, 
                   t: int
                  ) -> None:

        path_out = PATH_DATA + f'Frame_{t}.npy'
        if os.path.exists(path_out):
            os.remove(path_out)
        np.save(path_out, arr)
        return