##### Write/Read

|

##### About [Mixer
Configuration](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
## OutputSideband Property

* * *

#### Description

|  Specify whether to select the sum (High) or difference (Low) products.

  * When one LO is used: Input + or - LO1 = Output frequency
  * When two LOs are used: IF1 + or - LO2 = Output frequency

Use [IFSideband_Property](IFSideband_Property.md) when two LOs are used to
determine the IF1 frequency. If you are changing several mixer configuration
settings, you can make all the changes first and then issue the
[Calculate](../Methods/Calculate_Method.md) and
[Apply](../Methods/Apply_Method.md) commands as you would do from the user
interface. Note: There is also an [OutputSideband_Property](OutputSideband-
Converter_Property.htm) on the Converter Object.  
---|---  
  
####  VB Syntax

|  mixer.OutputSideband = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mixer |  A [Mixer](../Objects/IMixer_Interface.md) (object)  
value |  (FCASideBand) - Choose from: 0 - LOW Minus (-) on the Mixer setup dialog 1 - HIGH Plus (+) on the Mixer setup dialog  
  
#### Return Type

|  Enum as FCASideBand  
  
#### Default

|  LOW  
  
#### Examples

|  Print mixer.OutputSideband 'prints the value of the OutputSideband  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_OutputSideband(FCASideBand *pVal) HRESULT
put_OutputSideband(FCASideBand newVal)  
  
#### Interface

|  IMixer  
  
* * *

