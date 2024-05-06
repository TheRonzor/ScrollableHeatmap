import os
import numpy as np
from glob import glob
from IPython.display import clear_output
from scipy.signal import convolve2d as conv

class DataGenerator:
    def __init__(self,
                 n_frames: int,
                 dimensions: tuple[int, int],
                 path_out: str
                 ):
        '''
        Generates the fake data upon class instantiation
        '''
        self.path_out = path_out
        self.dimensions = dimensions

        # For padding frame names with leading zeros. Plus 2 for good measure.
        self.n_digits = len(str(n_frames))+2

        # Ensure output directory exists
        self._check_path_out()

        # Ensure output directory is clear
        self._clear_path_out()
        
        # Create initial frame
        frame = self._get_init_frame()
        self._save_frame(frame, 0)

        # Create the rest of the frames
        for t in range(n_frames):
            # Report progress
            clear_output(wait=True)
            print(f'Generating frame {t+1}')

            # Get the next frame
            frame = self._get_next_frame(frame)
            
            # Save the frame as an .npy
            self._save_frame(frame, t+1)
        return
    
    def _check_path_out(self) -> None:
        '''
        Ensures the output directory exists
        '''
        if not os.path.exists(self.path_out):
            os.mkdir(self.path_out)
        return
    
    def _clear_path_out(self) -> None:
        '''
        Clears existing files from the output directory
        '''
        files = glob(self.path_out + 'Frame_*.npy')
        for file in files:
            os.remove(file)
        return
    
    def _get_init_frame(self) -> np.ndarray:
        
        '''
        Creates the initial frame as a random array with a
        small fraction of cells set to 1, and the rest to 0.
        '''
        arr = np.random.random(size=self.dimensions) < 0.001
        return arr

    def _get_next_frame(self,
                        arr: np.ndarray
                        ) -> np.ndarray:
        '''
        Some old cellular automata code 
        (just so we have something to look at. It propagates.)
        ''' 
        n = 5
        kernel = np.array([
            [1,1,1],
            [1,0,1],
            [1,1,1]
            ])
        new_arr = conv(arr, kernel, 'same') % n
        return new_arr

    def _save_frame(self,
                    arr: np.ndarray,
                    t: int
                    ) -> None:
        '''
        Saves an array as an .npy file.
        Deletes any existing file with the same name first.
        '''
        label = str(t).zfill(self.n_digits)
        path_frame = self.path_out + f'Frame_{label}.npy'
        if os.path.exists(path_frame):
            os.remove(path_frame)
        np.save(path_frame, arr)
        return