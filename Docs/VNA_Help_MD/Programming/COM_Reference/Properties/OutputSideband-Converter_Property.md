##### Write/Read

|

##### About [Mixer
Configuration](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
## OutputSideband Property

* * *

#### Description

|  Specify whether to select the sum (High) or difference (Low) products.

  * When one LO is used: Input (+ or -) LO1 = Output frequency.
  * When two LO's are used: IF (+ or -) LO2 = Output frequency. See Also: [IFSideband Property](IFSideband-Converter_Property.md)

If you are changing several mixer configuration settings, you can make all the
changes first and then issue the [Calculate](../Methods/Calculate_Method.md)
and [Apply](../Methods/Apply_Method.md) commands as you would do from the
user interface.  
---|---  
  
####  VB Syntax

|  obj.OutputSideband = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Converter Object](../Objects/Converter_Object.md)  
value |  (enum as ConverterSideBand) \- Choose from: 0 - or naLowSide Minus (-) on the Mixer setup dialog 1 - or naHighSide Plus (+) on the Mixer setup dialog  
  
#### Return Type

|  Enum as ConverterSideBand  
  
#### Default

|  naLowSide  
  
#### Examples

|  Print converter.OutputSideband 'prints the value of the OutputSideband  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_OutputSideband(ConverterSideBand *pVal) HRESULT
put_OutputSideband(ConverterSideBand newVal)  
  
#### Interface

|  IConverter  
  
* * *

