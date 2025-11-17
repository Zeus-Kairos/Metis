##### Write/Read

|

##### About [Mixer
Configuration](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
## IsInputGreaterThanLO Property

* * *

#### Description

|  Specifies whether to use the Input frequency that is greater than the LO or
less than the LO. To learn more, see the [mixer setup dialog box
help.](../../../Applications/MixerConverter_Setup.htm#ILTI) If you are
changing several mixer configuration settings, you can make all the changes
first and then issue the [Calculate](../Methods/Calculate_Method.md) and
[Apply](../Methods/Apply_Method.md) commands as you would do from the user
interface.  
---|---  
  
####  VB Syntax

|  obj.IsInputGreaterThanLO (LO) = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Mixer Interface](../Objects/IMixer_Interface.md) pointer to the [Measurement](../Objects/Measurement_Object.md) (object) Or A [Converter Object](../Objects/Converter_Object.md)  
LO |  (Integer) - LO stage number Choose from 1 (default) or 2  
bool |  (Boolean) - True \- Use the Input that is Greater than the specified LO. False \- Use the Input that is Less than the specified LO.  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  mixer.IsInputGreaterThanLO(1) = True  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_IsInputGreaterThanLO(VARIANT_BOOL * val); HRESULT
put_IsInputGreaterThanLO(VARIANT_BOOL val);  
  
#### Interface

|  IMixer2 IConverter  
  
* * *

