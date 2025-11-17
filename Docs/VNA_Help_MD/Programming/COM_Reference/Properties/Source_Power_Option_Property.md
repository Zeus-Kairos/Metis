##### Write/Read

|

##### [About Source Power](../../../S1_Settings/Power_Level.md)  
  
---|---  
  
## SourcePowerOption Property

* * *

#### Description

|  Enables the source power to be set on individual sweep segments. This
property must be set True before seg.TestPortPower = value is sent. Otherwise,
the test port power command will be ignored.  
---|---  
  
####  VB Syntax

|  segs.SourcePowerOption = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
segs |  A Segments collection (object)  
state |  (boolean) True \- Enables variable TestPortPower to be set segment sweep False \- Disables variable TestPortPower to be set segment sweep  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  segs.SourcePowerOption = True 'Write  
powerOption = SourcePowerOption 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_SourcePowerOption(VARIANT_BOOL *pVal)  
HRESULT put_SourcePowerOption(VARIANT_BOOL newVal)  
  
#### Interface

|  ISegments

