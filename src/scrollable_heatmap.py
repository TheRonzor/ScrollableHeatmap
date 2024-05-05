from glob import glob
import numpy as np

class ScrollableHeatmap:
    '''
    A scrollable heatmap, based on a collection of numpy arrays that already exist.

    Arguments:
        t:          The intial frame to display (default 0)
    '''
    PATH_DATA = 'src/data/'

    def __init__(self,
                 t: int = 0,
                 all_frames: bool = False
                 ):
        
        self.t = t
        self._all_frames = all_frames
        
        # Get the frame data. Method based on the value passed for all_frames
        self._get_frames()

        # Set the initial frame
        self.set_current_frame(t)
        return
    
    def _get_frames(self) -> None:
        self.frames = glob(self.PATH_DATA + 'Frame_*.npy')
        return
    
    def set_current_frame(self,
                          t: int
                          ) -> None:
        '''
        Set the current frame
        '''
        self.cur_frame = np.load(self.frames[t])
        return
    
    def get_subset(self,
                   x: int,
                   y: int,
                   w: int,
                   h: int
                   ) -> np.ndarray:
        '''
        Returns a subset of the currently loaded frame for the caller to display on their end
        '''
        return self.cur_frame[x:x+w, y:y+h]