##### Write/Read

|

##### [About Dynamic Uncertainty](../../../S3_Cals/Dynamic_Uncertainty.md)  
  
---|---  
  
## DisplayType Property

* * *

#### Description

|  Sets and returns the display type for uncertainties for the selected
measurement trace.  
---|---  
  
#### VB Syntax

|  uncert.DisplayType = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
uncert |  An [Uncertainty](../Objects/Uncertainty_Object.md) (object)  
value |  (Enum as NAUncertaintyDisplayType) Display type. Choose from:

  * 0 or naUncertaintyDisplayNone \- Display the trace without uncertainties.
  * 1 or naUncertaintyDisplayMaximum - Display the trace as the uncertainty maximum (measured or memory data + upper limit uncertainty values). Not supported with Smith Chart or Polar display format.
  * 2 or naUncertaintyDisplayMinimum \- Display the trace as the uncertainty minimum (measured or memory data - lower limit uncertainty values). Not supported with Smith Chart or Polar display format.
  * 3 or naUncertaintyDisplayBar \- Display the uncertainties as error bars around the trace. Not supported with Smith Chart or Polar display format.
  * 4 or naUncertaintyDisplayShade \- Display the uncertainties as a shaded region around the trace. Not supported with Smith Chart or Polar display format.
  * 5 or naUncertaintyDisplayEllipse \- Display the uncertainties in ellipse form. Supported only in Smith Chart or Polar display format.

  
  
#### Return Type

|  Enum as NAUncertaintyDisplayType  
  
#### Default

|  naUncertaintyDisplayNone  
  
#### Examples

|  uncert.DisplayType = naUncertaintyDisplayMaximum  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_DisplayType(enum NAUncertaintyDisplayType *pDispType); HRESULT
put_DisplayType(enum NAUncertaintyDisplayType dispType);  
  
#### Interface

|  IUncertainty  
  
* * *

