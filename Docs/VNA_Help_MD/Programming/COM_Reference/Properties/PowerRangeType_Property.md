##### Write / Read

|

##### [About Receiver Leveling](../../../S1_Settings/Receiver_Leveling.md)  
  
---|---  
  
# PowerRangeType Property

* * *

#### Description

|  Sets and reads the type of power range data (specified or typical) to be
returned.  
---|---  
  
####  VB Syntax

|  powerRange.PowerRangeType = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
powerRange |  A [PowerRange](../Objects/Power_Range_Object.md) (object)  
value |  (Enum NAType) Choose from: 0 or naSpecifiedPower 1 or naTypicalPower  
  
#### Return Type

|  Enum  
  
#### Default

|  Not Applicable  
  
#### Examples

|  powerRange.PowerRangeType = naSpecifiedPower 'Write  
value = powerRange.PowerRangeType 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PowerRangeType(enum NAType *val); HRESULT
put_PowerRangeType(enum NAType val);  
  
#### Interface

|  IPowreRange  
  
* * *

