##### Write/Read

|

##### [About External Testset
Control](../../COM_Example_Programs/External_Testset_Control.htm)  
  
---|---  
  
## SelectPort Property

* * *

#### Description

|  Sets and returns a port mapping for a single port. If this command creates
a conflict with an existing port, the VNA will resolve the conflict. Note:
This command is currently not supported for the Z5623AK44.  
---|---  
  
####  VB Syntax

|  tset.SelectPort(chNum, portNum) = portValue  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
tset |  A [TestsetControl](../Objects/TestsetControl_Object.md) object.  
chNum |  (Long) Channel number of the measurement.  
portNum |  (Long) Physical port number to map.  
portValue |  (Long) Logical port value to assign  
  
#### Return Type

|  Long  
  
#### Default

|  Not Applicable  
  
#### Examples

|  [See External Testset
Program](../../COM_Example_Programs/External_Testset_Control.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SelectPort(long channelNum, long PortNum long *outPort);  
HRESULT put_SelectPort(long channelNum, long PortNum long outPort);  
  
#### Interface

|  ITestsetControl

