##### Write/Read

|

##### [About Equation
Editor](../../../S1_Settings/Power_Level.htm#Atten_Manual)  
  
---|---  
  
## Text Property

* * *

#### Description

| Specifies an equation or expression to be used on the measurement.  
---|---  
  
####  VB Syntax

| eq.Text = eqText  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
eq | [MeasurementEquation](../Objects/MeasurementEquation_Object.md) (object)  
eqText | (String) \- Any valid equation or expression.  
  
#### Return Type

| String  
  
#### Default

| Not Applicable  
  
#### Examples

| eq.Text = "foo=S11/S21"  
equation = eq.Text 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_Text(BSTR *equation)  
HRESULT put_Text(BSTR equation)  
  
#### Interface

| IMeasurementEquation

