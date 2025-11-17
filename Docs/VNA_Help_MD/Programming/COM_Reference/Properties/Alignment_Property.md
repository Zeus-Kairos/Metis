##### Write/Read

|

##### [About Time Domain](../../../Time/TimeDomain.md)  
  
---|---  
  
# Alignment Property

* * *

#### Description

| Sets the way the PNA computes the DC value of the frequency-domain
measurement. The correct DC value is required for inverse-FFT accuracy, and if
not estimated properly, can cause distortions in the time-domain measurement
in the form of an undesired slope in the waveform.  
---|---  
  
####  VB Syntax

| trans.Alignment = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
trans | A [Transform](../Objects/Transform_Object.md) (object)  
value | (Enum As NATransformAlignment) \- Choose from: 0 \- naTransformAlignmentLegacy \- The DC value is extrapolated using three data points. The transform offset is calculated using the delay of the first frequency point. This is the same algorithm used in the HP 8510 network analyzer. 1 \- naTransformAlignmentNormalize \- The DC value is extrapolated using three data points. The transform offset is set to zero at t=0 minus six rise-times. This mode requires that a good S-parameter calibration has been performed, which can be verified by observing a flat time-domain response at t=0 when measuring a load located at the physical point corresponding to t=0. Setting the time domain trace to zero at a time before t=0 stabilizes the trace for determining impedances after time t=0, resulting in improved behavior compared to Legacy mode. This method is similar to that used with PLTS, and is very useful in determining the time-domain-transform response of transmission lines and printed-circuit-board characteristics.  
  
#### Return Type

| Enum  
  
#### Default

| 0 - naTransformAlignmentNormalize  
  
#### Examples

| trans.Alignment = naTransformAlignmentNormalize 'Write  
value = trans.Alignment 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_Alignment(enum tagNATransformAlignment *pVal); HRESULT
put_Alignment(enum tagNATransformAlignment newVal);  
  
#### Interface

| ITransform3

