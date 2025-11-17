# CALCulate:Measure:UNCertainty Commands

Controls the trace settings for Dynamic Uncertainty for S-Parameters.

CALCulate:MEASure:UNCertainty DISPlay | CFACtor | TYPE MODE | CABle:REPeat | ETERm | NOISe SAVE  
---  
  
### See Also

  * See other [Dynamic Uncertainty commands](../SystUncertainty.md)

  * [Learn more about Dynamic Uncertainty](../../../S3_Cals/Dynamic_Uncertainty.md)

## CALCulate<cnum>:MEASure<mnum>:UNCertainty:DISPlay:CFACtor <value>

Applicable Models: N522xB, N523xB, N524xB (Write-Read) Sets and returns the
coverage factor (sigma) value to apply to the displayed uncertainty for the
selected measurement trace. Coverage Factor corresponds to the level of
confidence used in computing the specified measurement uncertainties.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<value> | Integer. Choose from: | Coverage Factor | Approximate confidence level  
---|---  
1 | 67%  
2 | 95%  
3 | 99%  
4 | >99%  
Examples | CALC1:MEAS:UNC:DISP:CFAC 2  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:UNCertainty:DISPlay:CFACtor?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 2  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:UNCertainty:DISPlay:TYPE <char>

Applicable Models: N522xB, N523xB, N524xB (Write-Read) Sets and returns the
display type for uncertainties for the selected measurement trace.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<char> | Display type. Choose from: NONE \- Display the trace without uncertainties. MAXimum  Display the trace as the uncertainty maximum (measured or memory data + upper limit uncertainty values). Not supported with Smith Chart or Polar display format. MINimum \- Display the trace as the uncertainty minimum (measured or memory data - lower limit uncertainty values). Not supported with Smith Chart or Polar display format. BAR  Display the uncertainties as error bars around the trace. Not supported with Smith Chart or Polar display format. SHADe  Display the uncertainties as a shaded region around the trace. Not supported with Smith Chart or Polar display format. ELLipse  Display the uncertainties in ellipse form. Supported only in Smith Chart or Polar display format.  
Examples | CALC1:MEAS:UNC:DISP:TYPE BAR  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:UNCertainty:DISPlay:TYPE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | NONE  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:UNCertainty:MODE:CABLe:REPeat <bool>

Applicable Models: N522xB, N523xB, N524xB (Write-Read) Sets and returns
whether the cable/connection repeatability contribution is currently included
in the uncertainty values for the selected measurement trace.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<bool> | Choose from: OFF (or 0) - Cable repeatability is NOT included. ON (or 1) - Cable repeatability IS included.  
Examples | CALC1:MEAS:UNC:MODE:CABL:REP ON  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:UNCertainty:MODE:CABLe:REPeat?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:UNCertainty:MODE:ETERm <bool>

Applicable Models: N522xB, N523xB, N524xB (Write-Read) Sets and returns
whether the uncertainties associated with the correction error terms are being
included in the uncertainty values for the selected measurement trace.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<bool> | Choose from: OFF (or 0) - Error term uncertainty contribution is NOT included. ON (or 1) - Error term uncertainty contribution IS included.  
Examples | CALC1:MEAS:UNC:MODE:ETER ON  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:UNCertainty:MODE:ETERm?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:UNCertainty:MODE:NOISe <bool>

Applicable Models: N522xB, N523xB, N524xB (Write-Read) Sets and returns
whether the noise contribution is currently included in the uncertainty values
for the selected measurement trace.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<bool> | Choose from: OFF (or 0) - Noise contribution is NOT included. ON (or 1) - Noise contribution IS included.  
Examples | CALC1:MEAS:UNC:MODE:NOIS ON  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:UNCertainty:MODE:NOISe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:UNCertainty:SAVE <"x,y,z">,<filename>

Applicable Models: N522xB, N523xB, N524xB (Write-only) Saves all three
uncertainty data formats from the active measurement for the specified ports.

  * This command is valid ONLY with Dynamic Uncertainty Calibration applied to the active measurement.
  * Data that is not available is zero-filled.
  * For sweeps with a large number of data points, always follow this command with *OPC? [Learn more.](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<"x,y,z"> | String Comma or space delimited port numbers for which data is requested, enclosed in quotes.  
<filename> | String Path, filename, and suffix of location to store the uncertainty data, enclosed in quotes. The suffix is not checked for accuracy.

  * (*.u*p) S-parameter Uncertainty File - If saving 2 ports, specify "filename.u2p"; If saving 4 ports, specify "filename.u4p.", and so forth.
  * (*.dsd) S-parameter Data Standard Definition file - Data for Only one or two ports is allowed.
  * (*.sdatcv) METAS S-parameter Covariance File.

  
Examples | All three examples save the active uncertainty measurement on channel 1 'Saves ports 2 and 3 to .u2p file CALC1:MEAS:UNC:SAVE "2,3","C:\myData.u2p" 'Saves ports 1 and 2 to .dsd file CALC1:MEAS:UNC:SAVE "1,2","C:\myData.dsd" 'Saves ports 1 through 4 to .sdatcv file CALC1:MEAS:UNC:SAVE "1,2,3,4","C:\myData.sdatcv"  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

