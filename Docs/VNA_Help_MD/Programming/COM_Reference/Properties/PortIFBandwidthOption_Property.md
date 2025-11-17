##### Write/Read

|

##### [About Segment Sweep](../../../S1_Settings/Sweep.md#segment)  
  
---|---  
  
# PortIFBandwidthOption Property

* * *

#### Description

| Enables or disables IF Bandwidth per port per segment. Value is set using
the [PortIFBandwidth Property](PortIFBandwidth_Property.md) of a Segment  
---|---  
  
####  VB Syntax

| segs.PortIFBandwidthOption = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
segs | A [Segments](../Objects/Segments_Collection.md) collection (object)  
value | (boolean)  
True \- Enable port IF bandwidth. False \- Disable port IF bandwidth.  
  
#### Return Type

| Boolean  
  
#### Default

| False  
  
#### Examples

| segs.PortIFBandwidthOption = True 'Write  
IFBWstate = segs.PortIFBandwidthOption 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_PortIFBandwidthOption(VARIANT_BOOL* pVal) HRESULT
put_PortIFBandwidthOption(VARIANT_BOOL pVal)  
  
#### Interface

| ISegments6

