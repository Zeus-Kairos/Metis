##### Write/Read

|

##### [About Balanced
Measurements](../../../S1_Settings/Balanced_Measurements.htm)  
  
---|---  
  
## BBalMeasurement Property

* * *

#### Description

|  Sets and returns the measurement for the Balanced - Balanced topology.  
---|---  
  
####  VB Syntax

|  balMeas.BBalMeasurement = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
balMeas |  A [BalancedMeasurement](../Objects/BalancedMeasurement_Object.md) (object)  
value |  (String) \- Balanced - Balanced Measurement parameter. Not case sensitive. Choose from: |  Sdd11 |  Sdd12 |  Sdc11 |  Sdc12  
---|---|---|---  
Sdd21 |  Sdd22 |  Sdc21 |  Sdc22  
Scd11 |  Scd12 |  Scc11 |  Scc12  
Scd21 |  Scd22 |  Scc21 |  Scc22  
Imb1 |  Imb2 |  CMRR -(Sdd21/Scc21)  
  
#### Return Type

|  String  
  
#### Default

|  Sdd11  
  
#### Examples

|  balMeas.BBalMeasurement = "Sdd11" 'Write variable = balMeas.BBalMeasurement
'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_BBalMeasurement(BSTR *pVal) HRESULT put_BBalMeasurement(BSTR
newVal)  
  
#### Interface

|  IBalancedMeasurement  
  
* * *

