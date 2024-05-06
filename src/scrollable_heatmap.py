from glob import glob
import numpy as np


def debugger(func):
    def wrapper(*args, **kwargs):
        print(f'args:{args}')
        print(f'kwargs:{kwargs}')
        results = func(*args, **kwargs)
        return results
    return wrapper
    

class ScrollableHeatmap:
    '''
    A scrollable heatmap, based on a collection of numpy arrays that already exist.

    The data files should be stored in .npy format.

    Arguments:
        t:          The initial frame to display (default 0)
    '''

    PATH_DATA = 'src/data/'

    def __init__(self,
                 t: int = 0
                 ):
        
        self.t = t
        
        # Get the frame data
        self._get_frames()

        # Set the initial frame
        self.set_current_frame(self.t)
        return
    
    def _get_frames(self) -> None:
        self.frames = glob(self.PATH_DATA + 'Frame_*.npy')
        self.frames.sort()
        return
    
    def set_current_frame(self,
                          t: int
                          ) -> None:
        '''
        Set the current frame
        '''
        self.cur_frame = np.load(self.frames[t])
        return
    
    #@debugger
    def get_subset(self,
                   x: int,
                   y: int,
                   w: int,
                   h: int,
                   t: int = None
                   ) -> np.ndarray:
        
        '''
        Returns a subset of the frame for the caller to display on their end

        If t is not provided, the data returned will be from the currently loaded frame.
        '''
        if t is not None:
            if self.t != t:
                self.set_current_frame(t)
        return self.cur_frame[x:x+w, y:y+h]