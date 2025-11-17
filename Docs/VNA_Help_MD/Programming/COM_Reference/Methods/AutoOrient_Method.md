##### Write-only

|

##### [About ECal Orientation](../../../S3_Cals/Using_ECal.md#Orient)  
  
---|---  
  
## AutoOrient Method

* * *

#### Description

|  Returns the ECal port that is connected to the specified VNA port. A
calibration does not have to be in process.  
---|---  
  
####  VB Syntax

|  ecalPortNumber = ecal.AutoOrient (chanNum, pnaPort, ecalCharNum)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
ecalPortNumber |  (Long) Variable to store the returned ECal port number that is connected to the specified VNA port number. The returned ECal port number is a 1-based number: 1 = Port A, 2 = Port B, 3 = Port C, 4 = Port D. Zero (0) is returned when the auto-orientation routine is unable to resolve the orientation.  
ecal |  A [ECalModule Object](../Objects/ECalModule_Object.md) (object)  
chanNum |  (Long) Channel number that contains the frequency range that will be calibrated.  
PNAPort |  (Long) VNA port number.  
ecalCharNum |  (Long) User Characterization number that matches the physical adapters/fixtures that are on the ECal module. This aids in determining the orientation of the ECal module. Choose from: 0 Factory characterization (no adapters - data that was stored in the ECal module by Keysight) 1 User characterization #1 2 User characterization #2 ...and so forth up to: 12 User characterization #12  
  
#### Return Type

|  Long Integer  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim app As AgilentPNA835x.Application Set app =
CreateObject("AgilentPNA835x.Application", <analyzerName>) Dim pna pna.Preset
Const chanNum = 1 pna.Channels(chanNum).StopFrequency = 20E9 ' for a 20 GHz
ECal mod Const pnaPortNumber = 1 Const ecalCharacterizationNum = 0 Dim calMgr
Set calMgr = pna.GetCalManager Dim ecalPortNumber ' The returned ECal port
number is a 1-based number ' (1 = Port A, 2 = Port B, etc) ecalPortNumber =
calMgr.ECalModules(1).AutoOrient(chanNum, pnaPortNumber,
ecalCharacterizationNum) MsgBox "ECal port number attached to PNA port 1 = " &
ecalPortNumber  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT AutoOrient( long channel, long pnaPortNumber, long
characterization, long *pECalPortNumber);  
  
#### Interface

|  IECalModule  
  
* * *

  

