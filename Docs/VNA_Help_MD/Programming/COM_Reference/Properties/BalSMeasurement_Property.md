##### Write/Read

|

##### [About Balanced
Measurements](../../../S1_Settings/Balanced_Measurements.htm)  
  
---|---  
  
## BalSMeasurement Property

* * *

#### Description

| Sets and returns the measurement for the Balanced - Single-ended topology.  
---|---  
  
####  VB Syntax

| balMeas.BalSMeasurement = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
balMeas | A [BalancedMeasurement](../Objects/BalancedMeasurement_Object.md) (object)  
value | (String) \- Balanced - Single-ended measurement parameter. Not case sensitive. Choose from: | Sdd11 | Sdc11 | Sds12  
---|---|---  
Scd11 | Scc11 | Scs12  
Ssd21 | Ssc21 | Sss22  
Imb | CMRR1  
(Ssd21/Ssc21) | CMRR2  
(Sds12/Scs12)  
  
#### Return Type

| String  
  
#### Default

| Sdd11  
  
#### Examples

| balMeas.BalSMeasurement = "Sdd11" 'Write variable = balMeas.BalSMeasurement
'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_BalSMeasurement(BSTR *pVal) HRESULT put_BalSMeasurement(BSTR
newVal)  
  
#### Interface

| IBalancedMeasurement3  
  
* * *

