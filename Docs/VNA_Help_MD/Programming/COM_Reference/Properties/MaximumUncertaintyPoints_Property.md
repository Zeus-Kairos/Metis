##### Read/Write

|

##### [About Dynamic Uncertainty](../../../S3_Cals/Dynamic_Uncertainty.md)  
  
---|---  
  
# MaximumUncertaintyPoints Property

* * *

#### Description

|  Sets and returns the maximum number of points for which uncertainties are
to be computed for subsequent calibrations that are performed using Dynamic
Uncertainty.  
---|---  
  
#### VB Syntax

|  uncertMan.MaximumUncertaintyPoints = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
uncertMan |  An [UncertaintyManager](../Objects/UncertaintyManager_Object.md) Object  
value |  (Boolean) Max number of points.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  500  
  
#### Examples

|  uncertMan.MaximumUncertaintyPoints = 201 [See example
program](../../COM_Example_Programs/Dynamic_Uncertainty.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MaximumUncertaintyPoints([out,retval] long* pNumPoints);
HRESULT put_MaximumUncertaintyPoints([in] long numPoints);  
  
#### Interface

|  IUncertaintyManager  
  
* * *

