##### Read-only

|

##### [About Equation
Editor](../../../S1_Settings/Power_Level.htm#Atten_Manual)  
  
---|---  
  
## Valid Property

* * *

#### Description

| Returns a boolean value to indicate if the current equation on the
measurement is valid. For equation processing to occur, the equation must be
valid and ON.  
---|---  
  
####  VB Syntax

| IsValid = eq.Valid  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
good | (Boolean) Variable to store the returned value. True (1) - equation is valid False (0) - equation is NOT valid  
eq | [MeasurementEquation](../Objects/MeasurementEquation_Object.md) (object)  
  
#### Return Type

| Boolean  
  
#### Default

| Not Applicable  
  
#### Examples

| IsValid = eq.Valid 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_Valid(Boolean *equation)  
  
#### Interface

| IMeasurementEquation  
  
* * *

