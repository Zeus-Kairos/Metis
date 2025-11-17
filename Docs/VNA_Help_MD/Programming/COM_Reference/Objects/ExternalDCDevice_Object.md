# ExternalDCDevice Object

* * *

Description

The ExternalDCDevice object allows you to set unique properties for a DC Meter
or DC Source.

### Accessing the ExternalDCDevice Object

You can obtain a handle to a ExternalDCDevice Object through
[ExtendedProperties](../Properties/ExtendedProperties_Property.md)

dim app Set app = CreateObject("AgilentPNA835x.Application") dim
externalDevices Set externalDevices = app.ExternalDevices dim devicecount
devicecount = externalDevices.count '******** Configure a DC Meter
************ externalDevices.Add "MyDCMeter" dim newExtDCMeter Set
newExtDCMeter = externalDevices.Item("MyDCMeter") newExtDCMeter.DeviceType =
"DC Meter" newExtDCMeter.Driver = "DCMeter" 'newExtDCMeter.Active = True
newExtDCMeter.IOConfiguration= "GPIB0::16::INSTR" dim extDCMtr Set extDCMtr =
newExtDCMeter.ExtendedProperties extDCMtr.PointDwell = .05 '******** Configure
a DC Supply ************ externalDevices.Add "MyDCSupply" dim newExtDCSupply
Set newExtDCSupply = externalDevices.Item("MyDCSupply")
newExtDCSupply.DeviceType = "DC Source" newExtDCSupply.Driver = "DCSource"
'newExtDCSupply.Active = True newExtDCSupply.IOConfiguration=
"GPIB0::16::INSTR" dim extDCSupply Set extDCSupply =
newExtDCSupply.ExtendedProperties extDCSupply.PointDwell = .05  
---  
  
### See Also:

[Configure an External
Device](../../../System/Configure_an_External_Device.htm)

[The VNA Object Model](The_Analyzer_Object_Model.md)

### Methods

|

### Interface

See History | 

### Description  
  
---|---|---  
None |  |   
  
### Properties

|

###

|

### Description  
  
[AbortSweepCmd](../Properties/AbortSweepCmd_Property.md) | IExternalDCDevice3 | Sets and returns the Abort Sweep command for an external DC Source and an external DC Meter.  
[AfterSweepCmd](../Properties/AfterSweepCmd_Property.md) | IExternalDCDevice3 | Sets and returns the After Sweep command for an external DC Source and an external DC Meter.  
[BeforeSweepCmd](../Properties/BeforeSweepCmd_Property.md) | IExternalDCDevice3 | Sets and returns the Before Sweep command for an external DC Source and an external DC Meter.  
[CurrentLimit](../Properties/CurrentLimit.md) | IExternalDCDevice2 | Sets and returns the current limit value.  
[DCCorrection](../Properties/DCCorrection_Property.md) | IExternalDCDevice | Sets and returns correction ON/OFF.  
[DCOffset](../Properties/DCOffset_Property.md) | IExternalDCDevice | Sets and returns the offset correction value.  
[DCScale](../Properties/DCScale_Property.md) | IExternalDCDevice | Sets and returns the scale correction value.  
[DCType](../Properties/DCType_Property.md) | IExternalDCDevice | Sets and returns the DC Type (Units).h  
[ErrorQuery](../Properties/ErrorQuery_Property.md) | IExternalDCDevice3 | Sets and returns the Error Query command for an external DC Source and an external DC Meter.  
[ExitCmd](../Properties/ExitCmd_Property.md) | IExternalDCDevice3 | Sets and returns the Disable I/O command for an external DC Source and an external DC Meter.  
[IDQuery](../Properties/IDQuery_Property.md) | IExternalDCDevice3 | Sets and returns the ID Query command for an external DC Source and an external DC Meter.  
[InitCmd](../Properties/InitCmd_Property.md) | IExternalDCDevice3 | Sets and returns the Enable I/O command for an external DC Source and an external DC Meter.  
[LimitCmd](../Properties/LimitCmd_Property.md) | IExternalDCDevice4 | Sets and returns the limit type (current or voltage) of the external DC Source.  
[MaxOutput](../Properties/MaxOutput_Property.md) | IExternalDCDevice3 | Sets and returns the Define Max As value for an external DC Source.  
[MaxOutputState](../Properties/MaxOutputState_Property.md) | IExternalDCDevice3 | Sets and returns the Define Max As ON/OFF state for an external DC Source.  
[MinOutput](../Properties/MinOutput_Property.md) | IExternalDCDevice3 | Sets and returns the Define Min As value for an external DC Source.  
[MinOutputState](../Properties/MinOutputState_Property.md) | IExternalDCDevice3 | Sets and returns the Define Min As ON/OFF state for an external DC Source.  
[PointCmd](../Properties/PointCmd_Property.md) | IExternalDCDevice3 | Sets and returns the Point Read Commands for an external DC Source or Point Set Commands for an external DC Meter.  
[PointDwell](../Properties/PointDwell_Property.md) | IExternalDCDevice | Sets and returns the "Dwell Before/After Point" value.  
[SweepDwell](../Properties/SweepDwell_Property.md) | IExternalDCDevice | Sets and returns the "Dwell Before Sweep" value.  
[VoltageLimit](../Properties/VoltageLimit.md) | IExternalDCDevice2 | Sets and returns the voltage limit value.  
  
### ExternalDCDevice History

Interface | Introduced with VNA Rev:  
---|---  
IExternalDCDevice | 9.5  
IExternalDCDevice2 | 12.70  
IExternalDCDevice3 | 12.80  
IExternalDCDevice4 | 13.25  
  
* * *

* * *

