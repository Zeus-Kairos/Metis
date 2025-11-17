##### Write/Read

|

##### [About Balanced
Measurements](../../../S1_Settings/Balanced_Measurements.htm)  
  
---|---  
  
# BSSMeasurement Property

* * *

#### Description

| Sets and returns the measurement for the Balanced - Single-Ended - Single-
Ended topology.  
---|---  
  
####  VB Syntax

| balMeas.BSSMeasurement = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
balMeas | A [BalancedMeasurement](../Objects/BalancedMeasurement_Object.md) (object)  
value | (String) \- Balanced - Single-Ended - Single-Ended Measurement parameter. Not case sensitive. Choose from: | Sdd11 | Sdc11 | Sds12 | Sds13  
---|---|---|---  
Scd11 | Scc11 | Scs12 | Scs13  
Ssd21 | Ssc21 | Sss22 | Sss23  
Ssd31 | Ssc31 | Sss32 | Sss33  
Imbal1 | Imbal2 | Sds12/Scs12 | Sds13/Scs13  
  
#### Return Type

| String  
  
#### Default

| Sdd11  
  
#### Examples

| balMeas.BSSMeasurement = "Sdd11" 'Write variable = balMeas.BSSMeasurement
'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_BSSMeasurement(BSTR *pVal) HRESULT put_BSSMeasurement(BSTR
newVal)  
  
#### Interface

| IBalancedMeasurement4  
  
* * *

