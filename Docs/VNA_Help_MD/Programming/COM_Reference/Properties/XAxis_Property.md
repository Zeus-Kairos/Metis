##### Write-Read

|

##### [About Internal DC Sources](../../../S1_Settings/ADC_Measurements.md)  
  
---|---  
  
## XAxis Property

* * *

#### Description

|  Sets the X-axis of the selected measurement to a DC Source. This command
does not change the default setting for new traces.  
---|---  
  
#### VB Syntax

|  Meas.XAxisSource= value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
Meas |  A [Measurement](../Objects/Measurement_Object.md) (object)  
value |  (String) \- Not case-sensitive. For all channels EXCEPT DIQ, choose from the following: "Default" \- The default X-axis setting for the selected measurement. For Application measurements, the X-Axis domain is set with specific commands. "AO1" \- Internal DC source #1 "AO2" \- Internal DC source #2 Note: For DIQ channels, see [XAxisDomain Property](XAxisDomain_Property.md)  
  
#### Example

|  Meas.XAxis = "Default" 'Write value = Meas.XAxis 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_XAxis(BSTR source); HRESULT get_XAxis(BSTR* source);  
  
#### Interface

|  IMeasurement17  
  
* * *

