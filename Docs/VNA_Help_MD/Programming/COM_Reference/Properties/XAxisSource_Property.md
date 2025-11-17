##### Read-only

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## XAxisSource Property

* * *

#### Description

|  Returns the X-Axis source of the selected measurement.

### See Also:

[ActiveXAxis Property](ActiveXAxis_Property.md) [XAxisDomain
Property](XAxisDomain_Property.htm)  
---|---  
  
#### VB Syntax

|  src = DIQMeas.XAxisSource  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
src |  (String) \- Variable to store the returned source for the domain that is displayed on the X-axis. See [ActiveXAxis Property](ActiveXAxis_Property.md) for possible returned values.  
DIQMeas |  A [DIQMeas](../Objects/DIQMeasurement_Object.md) (object)  
  
#### Example

|  src = diqMeas.XAxisSource 'Read 'Returns "Port 1"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_XAxisSource(BSTR* source);  
  
#### Interface

|  IDIQMeas  
  
* * *

