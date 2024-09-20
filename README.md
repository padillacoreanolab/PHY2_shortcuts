# PHY2_shortcuts
A very small Repo that has some examples of shortcuts we can use for PHY2 so users do not have to use the terminal every time. 

## Windows:
* Make sure Anaconda is installed for all users of the device.
* Copy the `PHY2.bat` file into `C:\ProgramData\anaconda3\Scripts`
* NOTE: Change address to where your anaconda is located.

 After you copy file, open it with you document of choice (notepad works fine). Ensure the file path beginning that leads to the bat file matches the path on your computer. Edit it to match if it doesn't. Then save!
 
 Once this is copied, you can right click->"Send to"->"Desktop (Shortcut)" and this will generate a desktop shortcut that you can click on to launch PHY2 just as you would on megatron.
 
 When you click on the desktop terminal, if it is working properly it should read:
 
"Starting PHY2...

PHY2 environment activated...

Enter Params.py file path:"

and from there you paste the phy folder file path and click enter, and it will open the file. 

Note: if after "starting PHY2" the next line says it had a problem accessing phy, then the file path in the batch file (PHY2.bat) is not correct. 

## Installation commands
```
conda create -n phy2 -y cython dask h5py joblib matplotlib numpy pillow pip pyopengl pyqt pyqtwebengine pytest python qtconsole requests responses scikit-learn scipy traitlets 
conda activate phy2 
pip install git+https://github.com/cortex-lab/phy.git
```

## PlugIns 
Missing the 1ms and 2ms columns in your cluster view on phy? Please open the plugins folder and follow the readme in there. 
