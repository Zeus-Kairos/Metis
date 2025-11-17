##### Write/Read

|

##### [About Balanced
Measurements](../../../S1_Settings/Balanced_Measurements.htm)  
  
---|---  
  
## SBalMeasurement Property

* * *

#### Description

|  Sets and returns the measurement for the Single-Ended - Balanced topology.  
---|---  
  
####  VB Syntax

|  balMeas.SBalMeasurement = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
balMeas |  A [BalancedMeasurement](../Objects/BalancedMeasurement_Object.md) (object)  
value |  (String) \- Single-ended - Balanced Measurement parameter. Not case-sensitive. Choose from: |  Sss11 |  Ssd12 |  Ssc12  
---|---|---  
Sds21 |  Sdd22 |  Sdc22  
Scs21 |  Scd22 |  Scc22  
Imb |  CMRR1 (Sds21/Scs21) |  CMRR2 (Ssd12/Ssc12)  
  
#### Return Type

|  Sss11  
  
#### Default

|  Not Applicable  
  
#### Examples

|  balMeas.SBalMeasurement = "Ssd12" 'Write variable = balMeas.SBalMeasurement
'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_SBalMeasurement(BSTR *pVal) HRESULT put_SBalMeasurement(BSTR
newVal)  
  
#### Interface

|  IBalancedMeasurement

