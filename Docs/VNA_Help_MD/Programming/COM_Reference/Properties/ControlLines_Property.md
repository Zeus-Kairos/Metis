##### Write/Read

|

##### [About E5091 Testset Control](../../../System/E5091_TestSet_Control.md)

##### [About External Testset
Control](../../../System/External_Testset_Control.htm)  
  
---|---  
  
## ControlLines Property

* * *

#### Description

|  Sets the control lines of the specified test set. Control lines, provided
through the front panel connector of a test set, are used to control external
equipment such as a part handler. See your test set documentation to learn
more about control lines.  
---|---  
  
####  VB Syntax

|  tset.ControlLines (chNum) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
tset |  A [TestsetControl](../Objects/TestsetControl_Object.md) object. OR An [E5091Testset](../Objects/E5091Testset_Object.md) object.  
chNum |  (Integer) Channel number of the measurement.  
value |  (Double) Data value used to set control lines. Values are obtained by adding weights from the following table that correspond to individual lines. |  Line |  Weight  
---|---  
1 |  1  
2 |  2  
3 |  4  
4 |  8  
5 |  16  
6 |  32  
7 |  64  
8 |  128  
  
  * The E5091A interprets SENS:MULT1:OUTP 0 as all lines LOW.

  * All "Z"and "H" series test sets interpret SENS:MULT1:OUTP 0 as all lines HIGH.

Refer to your test set documentation for setting control line values.  
  
#### Return Type

|  Variant  
  
#### Default

|  0  
  
#### Examples

|  'For a Z5623A K64 test set, the following sets line 3 and 4 OFF; all other
lines ON. testset1.ControlLines(2) = 12 [See E5091A Example
Program](../../COM_Example_Programs/E5091Testset_Control.htm) [See External
Testset Program](../../COM_Example_Programs/External_Testset_Control.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ControlLines(long channelNum, VARIANT *stateByte);  
HRESULT put_ControlLines(long channelNum, VARIANT stateByte);  
  
#### Interface

|  ITestsetControl IE5091Testset  
  
* * *

