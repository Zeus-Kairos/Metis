##### Write/Read

|

##### [About Dynamic Uncertainty](../../../S3_Cals/Dynamic_Uncertainty.md)  
  
---|---  
  
## Cable Property

* * *

#### Description

|  Sets and returns the name of the cable that is assigned to the port object
for Dynamic Uncertainty.  
---|---  
  
####  VB Syntax

|  port.Cable = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
port |  A [Port](../Objects/Port_Object.md) (object)  
value |  (String) \- Cable name.  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  port.Cable = "MyNewCable" 'Write the value  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Cable([out,retval] BSTR *pCableName); HRESULT put_Cable([in]
BSTR cableName);  
  
#### Interface

|  IPort  
  
* * *

