import os


PATH_DATA = 'src/data/'
PATH_IMG = 'src/img/'
PATHS = [PATH_DATA, PATH_IMG]

DIM_FULL = (300, 600)


def check_paths() -> None:
    '''
    Ensure all required directories exist.
    '''
    for path in PATHS:
        if not os.path.exists(path):
            os.mkdir(path)
    return

# Runs on any import - ensures the required directories exist.
check_paths()