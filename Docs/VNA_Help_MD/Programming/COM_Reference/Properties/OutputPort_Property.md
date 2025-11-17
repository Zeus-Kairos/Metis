##### Write/Read

|

##### [About Testset Control](../../../System/E5091_TestSet_Control.md)  
  
---|---  
  
## OutputPort Property

* * *

#### Description

|  Switches an input to one of the valid outputs on the specified E5091A. The following are valid input/output combinations. If a combination other than these are sent, an invalid argument error will occur. |  Input |  Valid Outputs  
---|---  
1 |  A  
T1\- If Port 2 already is connected to T1, then Port 2 will be switched to
T2.)  
2 |  T1 \- If Port 1 already is connected to T1, then Port 1 will be switched to A.  
T2  
3 |  R1+  
R2+  
R3+ If option 007 (7port), R2 is selected.  
4 |  R1-  
R2-  
R3- If option 007 (7port), R2 is selected.  
  
Note: Do not confuse the similar Testset.[OutputPorts
Property](OutputPorts_Property.htm), which sets or gets the port mapping for
ALL ports.  
  
####  VB Syntax

|  testsets(1).OutputPort (chNum,input) = output  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
testsets(1) |  An item from [Testsets](../Objects/E5091Testset_Collection.md) (collection) Learn how to [identify a testset in the collection.](../Objects/E5091Testset_Collection.md)  
chNum |  (Long) Channel number of the measurement.  
input |  (Long) Testset Input port. Choose from 1|2|3|4.  
output |  (Enum as NAE5091OutputPort) Output port to switch to specified Input. Choose from: 0 or naE5091PortA -  Port A 1 or naE5091PortT1 - Port T1 2 or naE5091PortT2 - Port T2 3 or naE5091PortR1 - Port R1 4 or naE5091PortR2 - Port R2 5 or naE5091PortR3 - Port R3  
  
#### Return Type

|  Enum  
  
#### Default

|  Not Applicable  
  
#### Examples

|  [See Example Program](../../COM_Example_Programs/E5091Testset_Control.md)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_OutputPort(long channelNum, long inputPort, E5091OutputPort
*outPort);  
HRESULT put_OutputPort(long channelNum, long inputPort, E5091OutputPort
outPort);  
  
#### Interface

|  IE5091Testsets

