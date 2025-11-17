##### Write/Read

|

##### About [Mixer
Configuration](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
## IFSideband Property

* * *

#### Description

|  When two LOs are used, sets or returns whether to select the sum or
difference for the IF1 product. (Input + or - LO1 = IF1)

  * This setting corresponds to the ![](../../../assets/images/mixerMinus.gif) buttons on LO1.
  * Also set [OutputSideband](OutputSideband_Property.md) to LOW or HIGH to determine the output frequency of the mixer.
  * This setting is ignored when ONE LO is used.
  * If you are changing several mixer configuration settings, you can make all the changes first and then issue the [Calculate](../Methods/Calculate_Method.md) and [Apply](../Methods/Apply_Method.md) commands as you would do from the user interface.

Note: There is also an [IFSideband_Property](IFSideband-
Converter_Property.htm) on the Converter Object.  
---|---  
  
####  VB Syntax

|  mixer.IFSideband =value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mixer |  A Mixer  (object)  
value |  (enum as FCASideBand) \- Choose from: 0 or LOW Minus (-) on the Mixer setup dialog 1 or HIGH Plus (+) on the Mixer setup dialog  
  
#### Return Type

|  Enum as FCASideBand  
  
#### Default

|  0 - LOW  
  
#### Examples

|  Print mixer.IFSideband 'prints the value of the IFSideband  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_IFSideband(FCASideBand *pVal) HRESULT
put_IFSideband(FCASideBand newVal)  
  
#### Interface

|  IMixer  
  
* * *

