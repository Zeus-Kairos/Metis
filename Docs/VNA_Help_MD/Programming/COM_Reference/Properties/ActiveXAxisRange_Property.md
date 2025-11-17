##### Write/Read

|

##### [About X-axis display](../../../FreqOffset/FCA_Use.md#Xaxis)  
  
---|---  
  
## ActiveXAxisRange Property

* * *

#### Description

|  For [FCA](../../../FreqOffset/FCA_Use.md) and
[GCX](../../../Applications/Gain_Compression_for_Converters.md) measurements,
sets the swept parameter to display on the X-axis This command does not change
the default setting for new traces. Use
[Converter.ActiveXAxisRange](ActiveXAxisRange_Conv_Property.md) to change all
existing traces and make the setting the default setting for new traces. This
command is NOT used for NFX, IMDX, and IMSX measurements. Use
[Converter.ActiveXAxisRange](ActiveXAxisRange_Conv_Property.md).  
---|---  
  
####  VB Syntax

|  mixer.ActiveXAxisRange = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mixer |  A Mixer  (object)  
value |  (Enum as MixerStimulusRange) \- Parameter to display on the X-axis. Choose from: 0 - mixINPUT \- Input frequency span 1 - mixLO_1 \- First LO frequency span 2 - mixLO_2 \- Second LO frequency span 3 - mixOUTPUT \- Output frequency span  
  
#### Return Type

|  Enum  
  
#### Default

|  OUTPUT  
  
#### Examples

|  mixer.ActiveXAxisRange = 1 'Write variable = mixer.ActiveXAxisRange 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ActiveXAxisRange(tagMixerStimulusRange *Val) HRESULT
put_ActiveXAxisRange(tagMixerStimulusRange newVal)  
  
#### Interface

|  IMixer3

