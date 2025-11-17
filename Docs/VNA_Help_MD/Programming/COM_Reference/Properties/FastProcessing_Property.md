##### Write/Read

|

##### [About Equation Editor](../../../S4_Collect/Equation_Editor.md)  
  
---|---  
  
# FastProcessing Property

* * *

#### Description

| Set and return equation editor trace update delay. This property delays
updating the equation editor trace until all trace references have finished
updating to ensure that all data is present. Note: This property does not work
in application channels. In addition, this property does not work with the
standard channel when the channel is in HOLD and then SINGLE sweeps are sent.  
---|---  
  
####  VB Syntax

| equation.FastProcessing = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
equation | A [MeasurementEquation](../Objects/MeasurementEquation_Object.md) (object)  
value | (Boolean) \- Choose from:

  * True \- Delay equation editor trace update.
  * False \- Do not delay equation editor trace update.

  
  
#### Return Type

| Boolean  
  
#### Default

| True  
  
#### Examples

| equation.FastProcessing = 1 'Write  
fast = equation.FastProcessing 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_FastProcessing(VARIANT_BOOL * pref); HRESULT
put_FastProcessing(VARIANT_BOOL pref);  
  
#### Interface

| IMeasurementEquation3

