##### Write/Read

|

##### [About External Testset
Control](../../../System/External_Testset_Control.htm)  
  
---|---  
  
## Label Property

* * *

#### Description

|  Sets or gets the display label for a given channel/testset combination. The
label appears in a status bar at the bottom of the VNA display when the
[ShowProperties](ShowProperties_Property.md) property is set to TRUE.  
---|---  
  
####  VB Syntax

|  tset.Label(chNum) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
tset |  A [TestsetControl](../Objects/TestsetControl_Object.md) object. Obtained from the [ExternalTestsets](../Objects/ExternalTestsets_Collection.md) collection.  
chNum |  (Integer) Channel number of the measurement.  
value |  (String) The text of the label.  
  
#### Return Type

|  String  
  
#### Default

|  None  
  
#### Examples

|  'The following sets the label for channel 5 corresponding to a given
testset object. testset1.label(5) = 'High-power output' [See External Testset
Program](../../COM_Example_Programs/External_Testset_Control.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Label(long channelNum, BSTR *pLabel);  
HRESULT put_Label(long channelNum, BSTR label);  
  
#### Interface

|  ITestsetControl

