##### Write-Read

|  
---|---  
  
## WGCutoffFreq Property

* * *

#### Description

|  Sets or returns the value of the waveguide cut off frequency.  
---|---  
  
####  VB Syntax

|  meas.WGCutoffFreq = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A Measurement  (object)  
value |  (double) \- Frequency in Hertz.  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Print meas.WGCutoffFreq 'prints the value of the waveguide cut off
frequency  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_WGCutoffFreq(double *pVal); HRESULT put_WGCutoffFreq(double
newVal);  
  
#### Interface

|  IMeasurement2

