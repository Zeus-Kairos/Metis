##### Write/Read

|

##### [About Segment Sweep](../../../S1_Settings/Sweep.md#segment)  
  
---|---  
  
## AllowArbitrarySegments Property

* * *

#### Description

|  Enables you to setup a segment sweep with arbitrary frequencies. The start
and stop frequencies of each segment can overlap other segments. Also, each
segment can have a start frequency that is greater than its stop frequency
which causes a reverse sweep over that segment. Learn more about [Arbitrary
Segment Sweep](../../../S1_Settings/Sweep.htm#Arbitrary).  
---|---  
  
####  VB Syntax

|  segs.AllowArbitrarySegments = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
segs |  A [Segments](../Objects/Segments_Collection.md) collection (object)  
value |  (boolean)  
True \- Allows the setup of arbitrary segment sweep. False \- Prevents the
setup of arbitrary segment sweep.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  segs.AllowArbitrarySegments = True 'Write  
AllowArbSegs = AllowArbitrarySegments 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_AllowArbitrarySegments(VARIANT_BOOL *pVal) HRESULT
put_AllowArbitrarySegments(VARIANT_BOOL newVal)  
  
#### Interface

|  ISegments3

