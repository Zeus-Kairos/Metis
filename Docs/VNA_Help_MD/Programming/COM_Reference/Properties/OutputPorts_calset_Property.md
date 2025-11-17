##### Read-only

|

##### [About External Testset
Control](../../COM_Example_Programs/External_Testset_Control.htm)  
  
---|---  
  
## OutputPorts (Cal Set) Property

* * *

#### Description

|  Returns the port mapping for the Cal Set.  
---|---  
  
####  VB Syntax

|  portMap = calset.OutputPorts  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
portMap |  (String) Variable to store the returned string. The returned values are the physical ports. The POSITION of the returned values corresponds to the logical ports. For example, with an N44xx test set, if the returned string is "PNA 1,TS 2,PNA 2, TS 4" this means:

  * PNA 1 is assigned to logical port 1
  * TS 2 is assigned to logical port 2
  * PNA 2 is assigned to logical port 3
  * TS 4 is assigned to logical port 4

  
calset |  A [Cal Set](../Objects/CalSet_Object.md) object.  
  
#### Return Type

|  String  
  
#### Default

|  Depends on the test set.  
  
#### Example

|  portMap = calset.OutputPorts  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_OutputPorts(BSTR *mapping);  
  
#### Interface

|  ICalset5  
  
* * *

