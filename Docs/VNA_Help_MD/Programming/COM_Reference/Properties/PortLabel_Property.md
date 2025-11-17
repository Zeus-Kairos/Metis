##### Write/Read

|

##### [About Modifying Cal Kits](../../../S3_Cals/ModifyCalKits.md#calkitmod)  
  
---|---  
  
## PortLabel Property

* * *

#### Description

|  Sets and returns the label on the calibration kit Port for the calibration
wizard.  
---|---  
  
####  VB Syntax

|  calKit.Portlabel (portNum) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calKit |  A CalKit (object)  
portNum |  (long integer) \- number of the port to be labeled. Choose either 1 or 2  
value |  (string) - Label that is visible in the calibration wizard.  
  
#### Return Type

|  String  
  
#### Default

|  Depends on the Cal Kit.  
  
#### Examples

|  calKit.PortLabel = "MyCalKit" 'Write  
kitLabel = calKit.PortLabel 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PortLabel(long port, BSTR *pVal)  
HRESULT put_PortLabel(long port, BSTR newVal)  
  
#### Interface

|  ICalKit

