##### Write/Read

|

##### [About Segment Sweep](../../../S1_Settings/Sweep.md#segment)  
  
---|---  
  
# Delay (Segment Sweep) Property

* * *

#### Description

| Sets or returns the segment delay property of the sweep segment. Enable
delay using the [DelayOption Property](DelayOption_Property.md) of Segments
collection.  
---|---  
  
####  VB Syntax

| seg.Delay = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
seg | A [Segment](../Objects/Segment_Object.md) (object)  
value | (Double) Delay value in seconds.  
  
#### Return Type

| Double  
  
#### Default

| 0  
  
#### Examples

| seg.Delay = 0.001 'Write  
value = seg.Delay 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_Delay(double* delay); HRESULT put_Delay(double delay);  
  
#### Interface

| ISegment3

