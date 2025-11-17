# ExternalSMUDevice Object

* * *

Description

ExternalSMUDevice objects allow you to set properties and methods for each
external SMU device.

### Accessing the ExternalDevice Object

Obtain a handle to an External Device by specifying an item in the [External
Devices collection.](ExternalDevices_Collection.htm)

dim app Set app = CreateObject("AgilentPNA835x.Application") dim
externalSMUDevices Set externalDevices = app.ExternalDevices dim devicecount
devicecount = externalDevices.count externalDevices.Add "NewSMU" dim
newExternalSMUDevice Set newExternalSMUDevice = externalDevices.Item("NewSMU")
newExternalSMUDevice.DeviceType = "SMU" newExternalSMUDevice.Active = True
newExternalSMUDevice.IOConfiguration= "GPIB0::14::INSTR"
newExternalSMUDevice.IOEnable = true dim extSMU Set extSMU =
newExternalSMUDevice.ExtendedProperties extSMU.PointDwell = .05  
---  
  
### See Also:

[The VNA Object Model](The_Analyzer_Object_Model.md)

Learn how to [Configure an External SMU
Device](../../../System/Configure_an_External_SMU.htm)

### Methods

|

### Interface

[See History](ExternalDevice_Object.md#History) | 

### Description  
  
---|---|---  
None |  |   
  
### Properties

|

###

|

### Description  
  
[ChanActive](../Properties/ChanActive_Property.md) | IExternalSMUDevice | Sets and returns the state of activation for an external device.  
  
### ExternalSMUDevice History

Interface | Introduced with VNA Rev:  
---|---  
IExternalSMUDevice | 12.85  
  
* * *

