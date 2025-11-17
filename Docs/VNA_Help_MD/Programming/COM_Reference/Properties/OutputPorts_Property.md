##### Write/Read

|

##### [About External Testset
Control](../../COM_Example_Programs/External_Testset_Control.htm)  
  
---|---  
  
## OutputPorts Property

* * *

#### Description

|  Sets or gets the port mappings for ALL ports. An invalid argument error
will occur if you attempt to set an illegal port combination. Refer to your
testset documentation for valid port combinations. Note: Do not confuse the
similar E5091.[OutputPort Property](OutputPort_Property.md), which sets or
gets the port mapping for a single port.  
---|---  
  
####  VB Syntax

|  tset.OutputPorts(chNum) = portList  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
tset |  A [TestsetControl](../Objects/TestsetControl_Object.md) object.  
chNum |  (Long) Channel number of the measurement.  
portList |  (String) A comma-separated list of port mappings. Spaces are ignored at the beginning and end of this text, and before or after commas. Space characters in other locations are not ignored.  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  [See External Testset
Program](../../COM_Example_Programs/External_Testset_Control.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_OutputPorts(long channelNum, BSTR *outPorts);  
HRESULT put_OutputPorts(long channelNum, BSTR outPorts);  
  
#### Interface

|  ITestsetControl

