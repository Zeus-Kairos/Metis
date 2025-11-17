##### Write/Read

|

##### [About Segment Sweep](../../../S1_Settings/Sweep.md#segment)  
  
---|---  
  
# SweepMode Property

* * *

#### Description

| Set and read the sweep mode per segment. Enable the sweep mode property
using the [SweepModeOption Property](SweepModeOption_Property.md) on Segments
collection.  
---|---  
  
####  VB Syntax

| seg.SweepMode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
seg | A [Segment](../Objects/Segment_Object.md) (object)  
value | (NASweepGenerationModes)  Choose from: 0 \- naSteppedSweep Sets sweep mode to stepped sweep. 1 \- naAnalogSweep Sets sweep mode to analog sweep.  
  
#### Return Type

| Enum  
  
#### Default

| naAnalogSweep  
  
#### Examples

| seg.SweepMode = naAnalogSweep 'Write  
value = seg.SweepMode 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT get_SweepMode(tagNASweepGenerationModes* mode) HRESULT
put_SweepMode(tagNASweepGenerationModes mode)  
  
#### Interface

| ISegment3

