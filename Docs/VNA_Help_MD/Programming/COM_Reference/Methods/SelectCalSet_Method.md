##### Write-only

|

#####  
  
---|---  
  
## SelectCalSet Method

* * *

#### Description

|  Selects and applies a Cal Set to the specified channel. Note: Error
Correction is not automatically applied as a result of this command being
issued. If there is more than one Cal Type in the Cal Set, you must explicitly
choose the Cal Type you want to apply. (See
[meas.Caltype](../Properties/Calibration_Type_Property.md))I  
---|---  
  
####  VB Syntax

|  channel.SelectCalSet calSet, restore  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
channel |  (object) - A [Channel](../Objects/Channel_Object.md) object  
calSet |  (string) \- Cal Set to make active. Specify the Cal Set by GUID or Name. Use [EnumerateCalSets](EnumerateCalSets_Method.md) to list the available Cal Sets.  
restore |  (boolean) - True (1) \- The stimulus stored with the cal set will be applied to the channel. False (0) \- If a conflict is detected between the existing channel settings and the Cal Set stimulus settings, then the following will occur: If interpolation is ON, then interpolation will be attempted. This may fail if the channel frequency is outside the range of the Cal Set. If interpolation is OFF, the selection will be abandoned and an error is returned: E_NA_CAL_STIMULUS_VALUES_EXCEEDED  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Example

|  channel.SelectCalSet GUID, 1 chan.SelectCalSet "MyCalSet", 0  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT SelectCalSet (BSTR strCset, bool bRestore);  
  
#### Interface

|  IChannel  
  
* * *

