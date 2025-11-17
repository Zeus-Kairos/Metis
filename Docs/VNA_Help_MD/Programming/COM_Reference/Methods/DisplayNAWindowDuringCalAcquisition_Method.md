##### Write-only

|

##### [About Cal Window](../../../S3_Cals/Calibration_Wizard.md#CalWindow)  
  
---|---  
  
## DisplayNAWindowDuringCalAcquisition Method

* * *

#### Description

|  Set the 'show' state of the window to be displayed during a calibration.
When this command is sent, the specified window is 'flagged' to be shown
during calibration. The flag is cleared when the window is closed. A Preset or
Instrument State Recall also closes the window. If the same window number is
reopened, this command must be sent again to show the window during a
calibration. The flag is NOT saved with an instrument state. Send this command
for each additional window to show during a calibration.  
---|---  
  
####  VB Syntax

|  calMgr.DisplayNAWindowDuringCalAcquisition (winNum, State)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calMgr |  (object) - A [CalManager](../Objects/CalManager_Object.md) object  
winNum |  (long) \- Window number to show during a calibration. The calibration window will also be shown with this window. The window must already be created. Use [NaWindows.count](../Properties/Count_Property.md) or [app.WindowNumber](../Properties/WindowNumber_Property.md) to read existing window numbers.  
state |  (Boolean) Window state. Choose from: True \- Show the specified window during calibration. False \- Do NOT show the specified window during calibration.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Example

|  calMgr.DisplayNAWindowDuringCalAcquisition 2,True [See example using this
command](../../COM_Example_Programs/Show_Custom_Window_during_Calibration.htm)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT DisplayNAWindowDuringCalAcquisition( long WinNum, VARIANT_BOOL
bVal);  
  
#### Interface

|  ICalManager5  
  
* * *

