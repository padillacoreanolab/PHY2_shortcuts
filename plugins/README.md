In order to install these plugins copy and paste the .py scripts of the plugins you want into the file ~/.phy/plugins/

Edit ~/.phy/phy_config.py, and specify the plugin names to load in the GUI:

c.Plugins.dirs = [r'C:\Users\megha\.phy\plugins'] #make sure this is a path to your .phy/plugins folder
c.TemplateGUI.plugins = ['ISIViolationPlugin1ms', 'ISIViolationPlugin2ms']  # list of plugin names to load in the TemplateGUIs, specifically the name of the class in each plugin .py script (open them, it is the class NameOfPlugIn that is the first line of each .py script)
