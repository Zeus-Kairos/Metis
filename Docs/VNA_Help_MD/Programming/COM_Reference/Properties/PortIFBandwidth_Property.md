##### Write/Read

|

##### [About Segment Sweep](../../../S1_Settings/Sweep.md#segment)  
  
---|---  
  
# PortIFBandwidth Property

* * *

#### Description

| Sets or returns the IF Bandwidth per port property of the Segment. Enable
the IF bandwidth per port property using the [PortIFBandwidthOption
Property](PortIFBandwidthOption_Property.htm) of the Segments collection.  
---|---  
  
####  VB Syntax

| seg.PortIFBandwidth(port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
seg | A [Segment](../Objects/Segment_Object.md) (object)  
port | (Long) Port number.  
value | (Double) IF bandwidth.  
  
#### Return Type

| Double  
  
#### Default

| 1000  
  
#### Examples

| seg.PortIFBandwidth(1) = 1000 'Write  
value = seg.PortIFBandwidth(1) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_PortIFBandwidth(long port, double* pVal); HRESULT
put_PortIFBandwidth(long port, double pVal);  
  
#### Interface

| ISegment3

