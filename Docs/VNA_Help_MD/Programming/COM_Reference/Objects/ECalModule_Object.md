# ECalModule Object

* * *

Allows access to ECal modules that are connected to the VNA.

### Accessing the ECalModule object

Get a handle to a ECalModule object by using the ECalModules collection. This
is done through the CalManager object with the
app.[GetCalManager](../Methods/Get_CalManager_Method.md) Method.

Dim app As AgilentPNA835x.Application Set app =
CreateObject("AgilentPNA835x.Application", <analyzerName>) Dim pna pna.Preset
Const chanNum = 1 pna.Channels(chanNum).StopFrequency = 20E9 ' for a 20 GHz
ECal mod Const pnaPortNumber = 1 Const ecalCharacterizationNum = 0 Dim calMgr
Set calMgr = pna.GetCalManager Dim ecalPortNumber ' The returned ECal port
number is a 1-based number ' (1 = Port A, 2 = Port B, etc) ecalPortNumber =
calMgr.ECalModules(1).AutoOrient(chanNum, pnaPortNumber,
ecalCharacterizationNum) MsgBox "ECal port number attached to PNA port 1 = " &
ecalPortNumber  
---  
  
### See Also:

  * [ECalModules Collection](ECalModules_Collection.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Interface

[See History](CalSet_Object.md#Interface1) | 

### Description  
  
---|---|---  
[AutoOrient](../Methods/AutoOrient_Method.md) |  IECalModule |  Returns the orientation (which ECal port is connected to which VNA port) outside of the context of a calibration.  
  
### Properties

|

###

|

### Description  
  
None |  |   
  
###  IECalModule History

Interface |  Introduced with VNA Rev:  
---|---  
IECalModule |  8.50  
  
* * *

