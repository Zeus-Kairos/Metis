# X Values Command

* * *

## SENSe<cnum>:X[:VALues]? - Superseded

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA Replaced with
[CALC:X?](../Calculate/X_Values.md) (Read-only) Returns the stimulus values
for the specified channel. If the channel is sweeping the source backwards,
the values will be in descending order. Note: To avoid frequency rounding
errors, specify [FORM:DATA](../Format_SCPI.md#fd) <Real,64> or <ASCii, 0>  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
Examples | SENS:X?  
sense2:x:values?  
Return Type | Depends on [FORM:DATA](../Format_SCPI.md#fd) command  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

