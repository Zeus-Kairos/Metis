##### Write/Read

|  
---|---  
  
## ElecDelayMedium Property

* * *

#### Description

|  Sets or returns the electrical delay medium.  
---|---  
  
####  VB Syntax

|  meas.ElecDelayMedium = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A Measurement  (object)  
value |  ( enum NACalStandardMedium ) choose from 0 - naCoax 1 - naWaveGuide  
  
#### Return Type

|  NACalStandardMedium  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Print meas.ElecDelayMedium 'prints the value of the electrical delay medium  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_ElecDelayMedium(tagNACalStandardMedium *pVal); HRESULT
put_ElecDelayMedium(tagNACalStandardMedium newVal);  
  
#### Interface

|  IMeasurement2

