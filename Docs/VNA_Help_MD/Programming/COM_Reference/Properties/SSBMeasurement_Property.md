##### Write/Read

|

##### [About Balanced
Measurements](../../../S1_Settings/Balanced_Measurements.htm)  
  
---|---  
  
## SSBMeasurement Property

* * *

#### Description

|  Sets and returns the measurement for the Single-Ended - Single-Ended -
Balanced topology.  
---|---  
  
####  VB Syntax

|  balMeas.SSBMeasurement = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
balMeas |  A [BalancedMeasurement](../Objects/BalancedMeasurement_Object.md) (object)  
value |  (String) \- Single-ended - Single-ended - Balanced Measurement parameter. Not case sensitive. Choose from: |  Sss11 |  Sss12 |  Ssd13 |  Ssc13  
---|---|---|---  
Sss21 |  Sss22 |  Ssd23 |  Ssc23  
Sds31 |  Sds32 |  Sdd33 |  Sdc33  
Scs31 |  Scs32 |  Scd33 |  Scc33  
Imb1 |  Imb2 |  CMRR1 (Sds31/Scs31) |  CMRR2 (Sds32/Scs32)  
  
#### Return Type

|  String  
  
#### Default

|  Sss11  
  
#### Examples

|  balMeas.SSBMeasurement = "Sss11" 'Write variable = balMeas.SSBMeasurement
'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SSBMeasurement(BSTR *pVal) HRESULT put_SSBMeasurement(BSTR p
newVal)  
  
#### Interface

|  IBalancedMeasurement

