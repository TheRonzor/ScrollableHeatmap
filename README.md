## Scrollable Heatmap

Data for each time interval are referred to as "frames", and are stored in the ``data`` folder with names like Frame0001.npy, Frame0002.npy, etc. The .npy files are binary files containing numpy arrays (this format should be fast to load, compared to .csv files). Name your files however you want - the current behavior is to assume that they are in chronological order when sorted alphabetically.

You'll want to make sure that your arrays are precompiled from the raw data, and saved as .npy files using numpy.save().

Files included:

- src/
    - data_generator.py: Not very important. It just creates some fake data (it's some old cellular automata code I had laying around)
    - scrollable_heatmap.py: Contains the ScrollableHeatmap class. By itself, this does not plot anything. It loads data from the .npy files, and has a method called get_subset(), where you can specify the portion of the array you want to have displayed in the heatmap
- data/
    - a directory containing the heatmap data (.npy files)

- Implementation.ipynb: Jupyter notbook that implements this using ipywidgets.

I implemented this in a jupyter notebook for now using ipywidgets, but it should be easy to integrate with Dash, Streamlit, etc. You just need to write a function that provides input to the ``ScrollableHeatmap.get_subset()`` function, and it will return the array of data to display in the heatmap. If using Streamlit, you'll almost certainly want to make use of the session_state and/or cache decorators (@st.cache_data, @st.cache_resource) to avoid unnecesary reloading of the same data.

More info here:

Caching in Streamlit: https://docs.streamlit.io/develop/concepts/architecture/caching

Session State in Streamlit: https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state


### How it works
Upon instantiation, the ScrollableHeatmap class gathers a list of files in the data folder and loads the first one. The get_subset() function takes as input, x, y, w, h, t, where (x,y) are the lower-left coordinates, (w,h) are the width and height, and t is 'time', where a separate file exists for each value of t. Whenever a different value of t is passed, it will load the appropriate data file. If the same value of t is passed as the previous call, it will just subset the existing array without reloading it. It then returns the subset of the array which can be passed to any plotting function/library you choose.