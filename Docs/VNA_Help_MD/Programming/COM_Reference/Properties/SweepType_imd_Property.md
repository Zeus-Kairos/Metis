##### Write/Read

|

##### [About Swept IMD Sweep
types](../../../Applications/Swept_IMD.htm#FreqTabDiag)  
  
---|---  
  
## SweepType Property (IMD Opt S93087A/B)

* * *

#### Description

| Sets and returns the type of sweep for a Swept IMD measurement. See a [list
of commands](../Objects/SweptIMD_Object.htm#sweepTypes) that are relevant for
each sweep type.  
---|---  
  
####  VB Syntax

| imd.SweepType = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
imd | A [SweptIMD](../Objects/SweptIMD_Object.md) Object  
value | (Enum as naSweepTypes) - Choose from:

  * 0 - naIMDToneCWSweep The main tone frequencies (F1 and F2) and power levels (P1 and P2) are held constant. Measurements are taken for the specified number of points.
  * 1 - naIMDTonePowerSweep The main tone frequencies are specified as either F1 and F2, or as FC and DeltaF. These frequencies are held constant while the power of each tone is varied from the Start Power to Stop Power
  * 2 - naIMDToneCenterFreqSweep Maintaining a constant tone spacing (DeltaF) and tone powers (P1 and P2), the center frequency (FC) is swept from Start to Stop, or can also be specified as Center and Span.
  * 3 - naIMDDeltaFrequencySweep The center frequency (FC) is held constant. The tone spacing is increased from Start DeltaF to Stop DeltaF.
  * 4 - naIMDToneSegmentSweep Same as FCenter sweep, except that the center frequencies for the sweep are constructed using the standard [segment sweep commands.](../Objects/Segments_Collection.md) (NOT valid for IMDx)
  * 5 - naLOPowerSweep All frequencies are fixed while the LO power is swept. (IMDx ONLY)

  
  
#### Return Type

| Enum  
  
#### Default

| 2 - naIMDToneCenterFreqSweep  
  
#### Examples

| imd.SweepType = naIMDToneCWSweep 'Write  
swptyp = imd.SweepType 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_SweepType(tagNASweepTypes* pVal) HRESULT
put_SweepType(tagNASweepTypes newVal)  
  
#### Interface

| ISweptIMD  
  
* * *

