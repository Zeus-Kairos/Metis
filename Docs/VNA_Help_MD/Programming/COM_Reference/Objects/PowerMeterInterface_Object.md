# PowerMeterInterface Object

* * *

Description

Contains the properties used to select a power meter and sensor to be used for
a source power calibration.

Note: This object replaces the [PowerMeterGPIBAddress
Property](../Properties/PowerMeterGPIBAddress_Property.htm).

### Accessing the PowerMeterInterface object

Get a handle to a power meter object using the
[PowerMeterInterfaces](PowerMeterInterfaces_Collection.md) collection.

Dim app As AgilentPNA835x.Application Set app =
CreateObject("AgilentPNA835x.Application", <analyzerName>) Dim
pwrMtrInterfaces As PowerMeterInterfaces Set pwrMtrInterfaces =
app.SourcePowerCalibrator.PowerMeterInterfaces If pwrMtrInterfaces.Count > 0
Then Dim pwrMtrInterface As PowerMeterInterface Set pwrMtrInterface =
pwrMtrInterfaces(1) pwrMtrInterface.Path = naUSB pwrMtrInterface.Locator =
Agilent Technologies,U2000A,MY12345678 End If  
---  
  
### See Also:

  * [Source Power Calibration](../../../S3_Cals/PwrCalibration.md#SourceDiag)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|  
---|---  
None |   
  
### Properties

|

### Description  
  
[Path](../Properties/Path_Property.md) |  Specifies the interface to use: GPIB, USB, LAN  
[Locator](../Properties/Locator_Property.md) |  Specifies the location (address) of the power meter/sensor.  
  
###  IPowerMeterInterface History

Interface |  Introduced with VNA Rev:  
---|---  
IPowerMeterInterface |  7.50  
  
* * *

