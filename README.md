# PHY2_shortcuts
A very small Repo that has some examples of shortcuts we can use for PHY2 so users do not have to use the terminal every time. 

## Windows:
* Make sure Anaconda is installed for all users of the device.
* Copy the `PHY2.bat` file into `C:\ProgramData\anaconda3\Scripts`
* NOTE: Change address to where your anaconda is located.

## Installation commands
```
conda create -n phy2 -y cython dask h5py joblib matplotlib numpy pillow pip pyopengl pyqt pyqtwebengine pytest python qtconsole requests responses scikit-learn scipy traitlets 
conda activate phy2 
pip install git+https://github.com/cortex-lab/phy.git
```