##### Write/Read

|

##### [About Limits](../../../S4_Collect/Use_Limits_to_Test_Devices.md)  
  
---|---  
  
## Type (limit) Property

* * *

#### Description

|  Specifies the Limit Line type.  
---|---  
  
####  VB Syntax

|  limt(index).Type = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
limt |  A LimitSegment (object)  
index |  (variant) - Limit line number in the LimitTest collection  
value |  (enum NALimitSegmentType) \- Limit Line type. Choose from:  
0 - naLimitSegmentType_OFF \- turns limit line OFF  
1 - naLimitSegmentType_Maximum \- limit line fails with a data point ABOVE the
line  
2 - naLimitSegmentType_Minimum \- limit line fails with a data point BELOW the
line  
  
#### Return Type

|  Long Integer  
  
#### Default

|  0 - OFF  
  
#### Examples

|  Set limts = meas.LimitTest  
limts.Type = naLimitSegmentType_Maximum 'Write  
limitType = limts.Type 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_Type(tagNALimitSegmentType *pVal)  
HRESULT get_Type(tagNALimitSegmentType newVal)  
  
#### Interface

|  ILimitSegment

