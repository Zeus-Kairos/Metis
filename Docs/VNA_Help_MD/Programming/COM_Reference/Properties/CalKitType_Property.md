##### Write/Read

|

##### [About Modifying Cal Kits](../../../S3_Cals/ModifyCalKits.md#calkitmod)  
  
---|---  
  
## CalKitType Property

* * *

#### Description

|  Sets and returns a calibration kit type to be used for UNGUIDED calibration
and for cal kit modification. To get a handle to this kit, use
[app.ActiveCalKit](Active_Cal_Kit_Property.md). Although an unlimited number
of cal kits can be imported into the VNA, ONLY mechanical cal kits #1 through
#95 can be accessed. There is also a [CalKitType](CalKitType_fca_Property.md)
property for use during a Guided, SMC, and VMC Calibration.  
---|---  
  
####  VB Syntax

|  object.CalKitType = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  [calkit](../Objects/calKit_Object.md) (object) or [Application](../Objects/Application_Object.md) (object) Note: app.CalKitType and calkit.calKitType perform exactly the same function.  
value |  (enum naCalKit) - Calibration Kit type. Choose from: 1 - naCalKit_User1  
2 - naCalKit_User2  
3 - naCalKit_User3  
4 - naCalKit_User4  
..  
..  
..  
94 - naCalKit_User94  
95 - naCalKit_User95 These enumerated values correspond with the calibration
kit ID on the [Advanced Cal Kit Modify dialog
box](../../../S3_Cals/ModifyCalKits.htm#modmenu). To change the cal kit name,
use [Name property](Name_CalKit_Property.md). Note: Always check the list of
available cal kits using [CalKitTypes](CalKitTypes_Property.md) to ensure
that the correct cal kit is selected.  
  
#### Return Type

|  NACalKit  
  
#### Default

|  Not Applicable  
  
#### Examples

|  calkit.CalKitType = naCalKit_User27  
kitype = app.CalKitType  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_CalKitType(tagNACalKit *pVal);  
HRESULT put_CalKitType(tagNACalKit newVal);  
  
#### Interface

|  IApplication  
ICalKit  
  
* * *

