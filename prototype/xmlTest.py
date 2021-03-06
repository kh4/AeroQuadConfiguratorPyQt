'''
Created on Nov 12, 2012

@author: Ted Carancho
'''

import xml.etree.ElementTree as ET
xml = ET.parse('xmlTest.xml')

# Get individual settings
print(xml.find("./Settings/DefaultComPort").text)
print(float(xml.find("./Settings/BootUpDelay").text))
print(float(xml.find("./Settings/CommTimeOut").text))

# Get all subpanel names
subPanelNames = xml.findall("./Subpanels/Subpanel")
for subPanelName in subPanelNames:
    print(subPanelName.get("Name"))
    
#G Get individual subpanel name
print(subPanelNames[0].get("Name"))

# Get individual subpanel values
subPanelName="Serial Monitor"
subPanelValue="Path"
xpath="./Subpanels/Subpanel/[@Name='" + subPanelName +"']/" + subPanelValue
print(xml.find(xpath).text)


"""
root = tree.getroot()

# Setup xml objects
subpanelRoot = root.find('Subpanels')
subpanelList = subpanelRoot.findall('Subpanel')

# Create list of subpanel names for menu
subpanelNames = [individualPanel.get('Name') for individualPanel in subpanelList]

# When user selects subpanel name, lookup subpanel index to access path and class
selectedPanel = "Serial Monitor"
#selectedPanel = "Template"
subpanelIndex = subpanelNames.index(selectedPanel)
subpanel = subpanelList[subpanelIndex]

print(subpanel.find('Path').text)
print(subpanel.find('Class').text)
"""

'''
settings = root.find('Settings')
print(settings.find('DefaultComPort').text)
print(float(settings.find("BootUpDelay").text))
print(float(settings.find('CommTimeOut').text))
'''