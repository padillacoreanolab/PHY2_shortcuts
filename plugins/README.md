## Getting started
Activate your phy2 environment and install phy:
conda activate phy2
pip install phy (into the command prompt/terminal)

## Finding your .phy folder
In order to install these plugins copy and paste the .py scripts of the plugins you want into the file ~/.phy/plugins/ 
- more specifically find or create a folder called plugins in your .phy folder and copy the scripts in this folder into the plugins folder (you can skip copying pasting the 1.5 ms ISI violdaiton script as we do not use it)

### Trouble shooting 
If there is no .phy folder, try launching phy with a phy file as if you were going to spike sort and see if it is generated then 

## Adding the PlugIns
Edit ~/.phy/phy_config.py, and specify the plugin names to load in the GUI:

```
c.Plugins.dirs = [r'C:\Users\megha\.phy\plugins'] #make sure this is a path to your .phy/plugins folder, obviously your Users folder is NOT megha

c.TemplateGUI.plugins = ['ISIViolationPlugin1ms', 'ISIViolationPlugin2ms']  # list of plugin names to load in the TemplateGUIs, specifically the name of the class in each plugin .py script (open them, it is the class NameOfPlugIn that is the first line of each .py script)
```
## Check to see if it worked
Now launch phy! 
