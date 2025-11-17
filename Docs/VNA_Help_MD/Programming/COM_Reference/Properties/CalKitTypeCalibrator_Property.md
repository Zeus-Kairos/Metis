##### Write/Read

## CalKitType Property

* * *

#### Description

|  Sets and returns the name of the Cal Kit to use for unguided cal.  
---|---  
  
####  VB Syntax

|  cal.CalKitType (port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
cal |  [Calibrator](../Objects/Calibrator_Object.md) (object)  
port |  (Long) Currently unused  
value |  (String) Cal Kit name enclosed in quotes. Use [CalKitTypes](CalKitTypes_Property.md) to read a list of all available Cal Kits in the VNA.  
  
####  Return Type

|  String  
  
#### Default

|  Last kit selected  
  
#### Examples

|  cal.CalKitType(1)= "85052B"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_CalKitType(long port, BSTR calKit); HRESULT get_CalKitType(long
port, BSTR* pCalKit);  
  
#### Interface

|  ICalibrator10  
  
* * *

  

