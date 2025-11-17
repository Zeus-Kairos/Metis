##### Write-only

|

##### [About Cal Window](../../../S3_Cals/Calibration_Wizard.md#CalWindow)  
  
---|---  
  
## AllowChannelToSweepDuringCalAcquisition Method

* * *

#### Description

|  Specifies the channel to sweep during a Calibration. When this command is
sent, the SwpChan channel is 'flagged' to be swept during calibration. The
flag is cleared when the channel is deleted, if the Measurement Class is
changed, or if all measurements are deleted from the channel. If the same
channel number is recreated, this command must be sent again to sweep the
channel during a calibration. The flag is NOT saved with an instrument state.
A Preset or Instrument State Recall deletes the channel.  
---|---  
  
####  VB Syntax

|  calMgr.AllowChannelToSweepDuringCalAcquisition (CalChan, SwpChan, State)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calMgr |  (object) - A [CalManager](../Objects/CalManager_Object.md) object  
CalChan |  (long) \- Channel to be calibrated.  
SwpChan |  (long) \- The channel to sweep when waiting to measure a standard. This channel must already exist with at least one measurement in the channel. If this channel is in continuous sweep mode, it must have the same attenuator settings and path configuration (PNA-X only).  
state |  (Boolean) \- Channel sweep state. Choose from: True \- Sweep the channel during calibration. False \- Do NOT sweep the channel during calibration.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Example

|  calMgr.AllowChannelToSweepDuringCalAcquisition 2,1,True [See example using
this
command](../../COM_Example_Programs/Show_Custom_Window_during_Calibration.htm)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT AllowChannelToSweepDuringCalAcquisition ( long CalChannel, long
SwpChannel, VARIANT_BOOL bVal);  
  
#### Interface

|  ICalManager5  
  
* * *

