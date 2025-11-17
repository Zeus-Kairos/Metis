# PowerMeterInterfaces Collection

* * *

Description

A collection object that provides a mechanism for accessing the
PowerMeterInterface objects.

The collection size is limited to one PowerMeterInterface object. By default,
that PowerMeterInterface object refers to GPIB, and to the GPIB address that
is currently set for the power meter on that VNA.

The power meter is specified by using the
[Path](../Properties/Path_Property.md) property.

### Accessing the PowerMeterInterfaces collection

Get a handle to a power meter object using the PowerMeterInterfaces
collection.

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
[Item](../Methods/Item_Method.md) |  Use to get a handle to a [PowerMeterInterface](PowerMeterInterface_Object.md) object in the collection.  
  
### Properties

|

### Description  
  
[Count](../Properties/Count_Property.md) |  Returns the number of objects in the collection.  
[Parent](../Properties/Parent_Property.md) |  Returns a handle to the SourcePowerCalibrator  
  
###  IPowerMeterInterfaces History

Interface |  Introduced with VNA Rev:  
---|---  
IPowerMeterInterfaces |  7.50  
  
* * *

