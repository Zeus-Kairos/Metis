##### Read-only

## GetCalKitTypeString Method

* * *

#### Description

|  Returns ECal module model number and serial number based on the index
number of the attached ECal modules.  
---|---  
  
####  VB Syntax

|  ECalID = cal.GetCalKitTypeString (module)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
ECalID |  (string) \- variable to store the returned ECal module ID information.  
cal |  A [Calibrator](../Objects/Calibrator_Object.md) (object)  
module |  (long integer)  ECal module. Choose from modules 1 through 8 Use [IsECALModuleFoundEx](../Properties/IsECALModuleFoundEx_Property.md) to determine the number of modules connected to the VNA  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  info = cal.GetCalKitTypeString(2) Example return string: "N4691-60003 ECal
01234"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT GetCalKitTypeString(long moduleNumber, BSTR* info);  
  
#### Interface

|  ICalibrator8  
  
* * *

