##### Write-Read

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## XAxisDomain Property

* * *

#### Description

|  Sets and returns the X-Axis domain of the selected DIQ measurement.  
---|---  
  
#### VB Syntax

|  Meas.XAxisDomain = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
Meas |  A [Measurement](../Objects/Measurement_Object.md) (object)  
value |  String \- Domain that is displayed on the X-axis. |  Choose one of these: |  Then set X-Axis Source ([XAxis Property](XAxis_Property.md)) using one of these as the argument.  
---|---  
"Frequency" |  "F1", "F2", etc.  
"Power" |  Source port: "Port 1", "Port 2", etc.  
"Phase" |  Source port: "Port 1", "Port 2", etc.  
"DC" |  DC Source:"AO1", "AO2"  
"Points" |  "Points"  
  
#### Example

|  1\. Meas.XAxisDomain = "Frequency" 2\. Meas.XAxis = "F2" domain =
Meas.XAxisDomain 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_XAxisDomain(BSTR domain); HRESULT get_XAxisDomain(BSTR
*domain);  
  
#### Interface

|  IMeasurement17  
  
* * *

