# Saving/Recalling Setting

  * Saving Setting

  * Recalling Setting

  * Compatibility of State Files

[Other topics about Storing Data and Setting](Storing_Data_and_Setting.md)

## Saving Setting

The setting of TDR can be saved and recalled. The state file of TDR
measurements has .tdr file extension.

  1. Setup your configuration which you want to save.

  2. Click File in the tool bar.

  3. Select Save State from menu, then the Save State As dialog is displayed.

  4. Type desired file name.

  5. Click Save.

When you use 2-channel measurement in the Advanced Mode, the channel 2 setting
is also saved in the .tdr file.

## Recalling Setting

  1. Click File in the tool bar.

  2. Select Recall State from menu, then the Recall State As dialog is displayed.

  3. Select the file name of state file whose file extension is .tdr.

  4. Click Open.

## Compatibility of State Files

### Compatibility between Mode

The following table shows the compatibility of state file between mode.

Mode | Recalling  
---|---  
Basic | Advanced  
Saved File By | Basic | Y | N  
Advanced | N | Y  
  
Y: Recall is possible.

N: Recall is not possible.

