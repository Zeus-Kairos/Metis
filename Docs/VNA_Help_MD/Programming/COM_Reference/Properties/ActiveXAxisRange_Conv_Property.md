##### Write/Read

|

##### [About Mixer
Configuration](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
## ActiveXAxisRange Property

* * *

#### Description

|  Sets the swept frequency range to display on the X-axis for all existing
traces and sets the default for all future traces.  
---|---  
  
####  VB Syntax

|  obj.ActiveXAxisRange = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Converter Object](../Objects/Converter_Object.md) (for IMDX and NFX measurements) or A [Measurement Object](../Objects/Measurement_Object.md) (for GCX, SMC, and VMC measurements)  
value |  (Enum as ConverterStimulusRange) Swept stimulus range to display on the X-axis. Choose from: 0 - naInputRange \- Input frequency range 1 - naLO1Range - LO 1 frequency range 2 - naLO2Range - LO 2 frequency range 3 - naOutputRange \- Output frequency range 4 - naPerMeasurementRange \- reserved for future use. If the specified frequency range is not swept, the default swept range is used.  
  
#### Return Type

|  Enum  
  
#### Default

|  Search is performed in the following order until a swept range is found:

  1. OUTPUT
  2. INPUT (If the OUTPUT is fixed)
  3. Number of Points (If ALL ranges are fixed)

  
  
#### Examples

|  conv.ActiveXAxisRange = naInputRange 'Write variable =
meas.ActiveXAxisRange 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ActiveXAxisRange(tagConverterStimulusRange range *Val) HRESULT
put_ActiveXAxisRange(tagConverterStimulusRange range newVal)  
  
#### Interface

|  IConverter IMeasurement14

