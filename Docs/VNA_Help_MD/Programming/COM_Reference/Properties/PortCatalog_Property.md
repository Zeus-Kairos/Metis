##### Read-only

|

##### [About External Testset
Control](../../../System/External_Testset_Control.htm)  
  
---|---  
  
## PortCatalog Property

* * *

#### Description

|  Returns a comma-separated list of the Output port selections that are
available for a given logical input port. Read the number of input ports for
the test set using [NumberOfPorts
Property](NumberOfPorts_Testset_Property.htm).  
---|---  
  
####  VB Syntax

|  value = tset.PortCatalog(logPort)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (String) Variable to store the returned information.  
tset |  A [TestsetControl](../Objects/TestsetControl_Object.md) object.  
logPort |  (Long) Logical Input port number for which to return valid output ports.  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = testset1.PortCatalog 2 [See External Testset
Program](../../COM_Example_Programs/External_Testset_Control.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PortCatalog(long inputPort, BSTR *outPort);  
  
#### Interface

|  ITestsetControl  
  
* * *

