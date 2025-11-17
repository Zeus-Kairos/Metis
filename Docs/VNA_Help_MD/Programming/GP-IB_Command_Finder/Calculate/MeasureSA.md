# CALCulate:MEASure:SA Commands

Controls the marker settings used in the SA application.

CALCulate:MEASure:SA:MARKer: BAND | FUNCtion | IBW BDENsity | ACPR | [:STATe] | BW | DATA? | EQSPan | NOISe | [:STATe] | NPR | [:STATe] | POWer | BW | [:STATe] | TONE | BW | [:STATe] | TSPacing BPOWer | DATA? | SPAN | [:STATe] OCCBand | CENTer? | PERCent | POWer? | SPAN? | [:STATe] SEARch | ACPR | NPR  
---  
  
Click on a keyword to view the command details.

See Also

  * Marker Readout [number](../Display.md#single) and [size](../Display.md#size) commands.

  * [Learn about Markers](../../../S4_Collect/Markers.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

Important: Learn about [programming the reference
marker](../../../S4_Collect/Markers.htm#Number_of_Markers).

* * *

## CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BAND:FUNCtion <enum>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
or N524xB models with Option S93070xB (Read-Write) Set and read the SA marker
function type.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<n> | Marker number. If unspecified, <n> is set to 1.  
<enum> | Choose from: MNOI - Marker noise. BPOW - Band power. BDEN - Band density. OFF [Learn about these settings.](../../../S4_Collect/Markers.md#Spectrum_Analyzer_Marker_Search)  
Examples | CALC:MEAS2:SA:MARK:BAND:FUNC MNOI  
Query Syntax | CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BAND:FUNCtion?  
Return Type | Enumeration  
Default | OFF  
  
* * *

## CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BAND:IBW <num>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
or N524xB models with Option S93070xB (Read-Write) Sets and reads the
integration bandwidth marker. The IBW is used to determine total signal power
within a specified frequency span. For example, to calculate the total power
of a signal composed of 100 tones spaced 1 MHz apart over a 100 MHz span, the
signal power would be integrated over an IBW of 100 MHz.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<n> | Marker number. If unspecified, <n> is set to 1.  
<num> | Choose an integration bandwidth.  
Examples | CALC:MEAS2:SA:MARK:BAND:IBW 100e6  
Query Syntax | CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BAND:IBW?  
Return Type | Numeric  
Default | Not Applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BDENsity:ACPR[:STATe] <bool>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
or N524xB models with Option S93070xB  (Read-Write) Sets and reads the ACPR
density marker.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<n> | Marker number. If unspecified, <n> is set to 1.  
<bool> | Choose from: 0 - OFF \- Turn band density marker OFF. 1 - ON \- Turn band density marker ON.  
Examples | 'Create marker3 on that measurement CALC2:MARK3 ON 'Make it a band density noise marker CALC2:MEAS:SA:MARK3:BDEN:ACPR:STAT 1  
Query Syntax | CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BDENsity:ACPR[:STATe]?  
Return Type | Boolean  
Default | 0  
  
* * *

## CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BDENsity:BW <num>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-Write) Sets and reads the bandwidth of the band density marker.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<n> | Marker number. If unspecified, <n> is set to 1.  
<num> | Choose a bandwidth.  
Examples | CALC:MEAS2:SA:MARK:BDEN:BW 1e6  
Query Syntax | CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BDENsity:BW?  
Return Type | Numeric  
Default | 1 MHz  
  
* * *

## CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BDENsity:DATA?

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-only) Returns the band density level in dBm/Hz from the band density
marker.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<n> | Band density marker number. If unspecified, <n> is set to 1.  
Examples | CALC:MEAS2:SA:MARK:BDEN:DATA? calculate2:measure2:sa:marker2:bdensity:data?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BDENsity:EQSPan <num>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-Write) Sets and reads the frequency span used by Power Density to
normalize the power.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<n> | Marker number. If unspecified, <n> is set to 1.  
<num> | Choose a span.  
Examples | CALC:MEAS:SA:MARK:BDEN:EQSPan 1e6  
Query Syntax | CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BDENsity:EQSPan?  
Return Type | Numeric  
Default | 1 MHz  
  
* * *

## CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BDENsity:NOISe[:STATe] <bool>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-Write) Sets and reads the state of the band density noise marker.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<n> | Marker number. If unspecified, <n> is set to 1.  
<bool> | Choose from: 0 - OFF \- Turn band density noise marker OFF. 1 - ON \- Turn band density noise marker ON.  
Examples | 'Create marker3 on that measurement CALC2:MARK3 ON 'Make it a band density noise marker CALC:MEAS:SA:MARK:BDEN:NOIS:STAT 1  
Query Syntax | CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BDENsity:NOISe?  
Return Type | Boolean  
Default | 0  
  
* * *

## CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BDENsity:NPR[:STATe] <bool>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
or N524xB models with Option S93070xB  (Read-Write) Sets and reads the NPR
density marker.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<n> | Marker number. If unspecified, <n> is set to 1.  
<bool> | Choose from: 0 - OFF \- Turn band density marker OFF. 1 - ON \- Turn band density marker ON.  
Examples | 'Create marker3 on that measurement CALC2:MARK3 ON 'Make it a band density noise marker CALC2:MEAS:SA:MARK3:BDEN:NPR:STAT 1  
Query Syntax | CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BDENsity:NPR[:STATe]?  
Return Type | Boolean  
Default | 0  
  
* * *

## CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BDENsity:POWer[:STATe] <bool>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-Write) Sets and reads the state of the band power density marker.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<n> | Marker number. If unspecified, <n> is set to 1.  
<bool> | Choose from: 0 - OFF \- Turn band power density marker OFF. 1 - ON \- Turn band power density marker ON.  
Examples | 'Create marker3 on that measurement CALC2:MARK3 ON 'Make it a band density noise marker CALC:MEAS:SA:MARK:BDEN:POW:STAT 1  
Query Syntax | CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BDENsity:POWer?  
Return Type | Boolean  
Default | 0  
  
* * *

## CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BDENsity:POWer:BW <num>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-Write) Sets and reads the bandwidth of the band power density marker.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<n> | Marker number. If unspecified, <n> is set to 1.  
<num> | Choose a bandwidth.  
Examples | CALC:MEAS:SA:MARK:BDEN:POW:BW 1e6  
Query Syntax | CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BDENsity:POWer:BW?  
Return Type | Numeric  
Default | 1 MHz  
  
* * *

* * *

## CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BDENsity:TONE:BW <num>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-Write) Sets and reads the bandwidth of the band tone density marker.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<n> | Marker number. If unspecified, <n> is set to 1.  
<num> | Choose a bandwidth.  
Examples | CALC:MEAS:SA:MARK:BDEN:TONE:BW 1e6  
Query Syntax | CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BDENsity:TONE:BW?  
Return Type | Numeric  
Default | 1 MHz  
  
* * *

## CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BDENsity:TONE[:STATe] <bool>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-Write) Sets and reads the state of the band tone density marker.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<n> | Marker number. If unspecified, <n> is set to 1.  
<bool> | Choose from: 0 - OFF \- Turn band tone density marker OFF. 1 - ON \- Turn band tone density marker ON.  
Examples | 'Create marker3 on that measurement CALC2:MARK3 ON 'Make it a band density noise marker CALC:MEAS:SA:MARK:BDEN:TONE:STAT 1  
Query Syntax | CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BDENsity:TONE?  
Return Type | Boolean  
Default | 0  
  
* * *

## CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BDENsity:TONE:TSPacing <num>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-Write) Sets and reads the spacing of the band tone density marker.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<n> | Marker number. If unspecified, <n> is set to 1.  
<num> | Choose a spacing value.  
Examples | CALC:MEAS:SA:MARK:BDEN:TONE:TSP 100e6  
Query Syntax | CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BDENsity:TONE:TSPacing?  
Return Type | Numeric  
Default | 100 MHz  
  
* * *

## CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BPOWer:DATA?

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-only) Returns the band power level from the band power marker.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<n> | Band power marker number.  
Examples | CALC:MEAS2:SA:MARK:BPOW:DATA? calculate2:measure2:sa:marker2:bpower:data?  
Default | Not applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BPOWer:SPAN <num>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-Write) Sets and reads the frequency span of the band power marker. This
area is marked by two vertical dotted lines on the screen and the marker's
y-axis value is set to the measured power value. Noise and power on the same
marker share the same span.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<n> | Marker number.  
<num> | Choose a frequency span within the frequency range of the analyzer.  
Examples | CALC:MEAS2:SA:MARK:BPOW:SPAN 1e6  
Query Syntax | CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BPOWer:SPAN?  
Return Type | Numeric  
Default | 1 MHz  
  
* * *

## CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BPOWer[:STATe] <bool>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-Write) Sets and reads the state of the band power marker. This command
makes a band power marker from a generic marker. The generic marker must first
be created using:
[CALC:MEAS:MARK:STATe](MeasureMARKer.md#CALCulate:MEASure:MARKer:STATe)  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<n> | Marker number.  
<bool> | Choose from: 0 - OFF \- Turn band power marker OFF. 1 - ON \- Turn band power marker ON.  
Examples | 'Create marker3 on the specified measurement CALC2:MEAS2:MARK3 ON 'Make it a band power marker CALC:MEAS2:SA:MARK:BPOW:STAT 1  
Query Syntax | CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:BPOWer?  
Return Type | Boolean  
Default | 0  
  
## CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:OCCBand:CENTer?

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-only) Returns the occupied bandwidth center frequency.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<n> | Marker number.  
Examples | CALC:MEAS:SA:MARK:OCCB:CENT? calculate2:measure:sa:marker2:occband:center?  
Default | Not applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:OCCBand:PERCent <num>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-Write) Sets and returns the percentage of the band power to search for.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<n> | Marker number.  
<num> | Percentage value.  
Examples | CALC:MEAS:SA:MARK:OCCB:PERC 99 calculate2:measure:sa:marker2:occband:percent 99  
Query Syntax | CALCulate<ch>:SA:MARKer<n>:OCCBand:PERCent?  
Return Type | Numeric  
Default | 99.0  
  
* * *

## CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:OCCBand:POWer?

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-only) Returns the occupied bandwidth power.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<n> | Marker number.  
Examples | CALC:MEAS:SA:MARK:OCCB:POW? calculate2:measure:sa:marker2:occband:power?  
Default | Not applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:OCCBand:SPAN?

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-only) Returns the occupied bandwidth span.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<n> | Marker number.  
Examples | CALC:MEAS:SA:MARK:OCCB:SPAN? calculate2:measure:sa:marker2:occband:span?  
Default | Not applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:OCCBand[:STATe] <bool>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-Write) Sets and returns the occupied bandwidth on/off state.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<n> | Marker number.  
<bool> | Choose from: 0 - OFF \- Turns occupied bandwidth OFF. 1 - ON \- Turns occupied bandwidth ON.  
Examples | CALC:MEAS:SA:MARK:OCCB:STAT 1 calculate2:measure:sa:marker2:occband:state 1  
Query Syntax | CALCulate<ch>:SA:MARKer<n>:OCCBand[:STATe]?  
Return Type | Boolean  
Default | 0 Note: If occupied band state is turned ON, then Band Power or Band Noise is turned OFF.  
  
* * *

## CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:SEARch:ACPR

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Write-only) Executes the search ACPR density marker.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<n> | Marker number. If unspecified, <n> is set to 1.  
Examples | CALC:MEAS:SA:MARK:SEAR:ACPR calculate2:measure:sa:marker2:search:acpr  
Query Syntax | Not Applicable  
Default | Not Applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:SA:MARKer<n>:SEARch:NPR

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Write-only) Executes the search NPR density marker.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<n> | Marker number. If unspecified, <n> is set to 1.  
Examples | CALC:MEAS:SA:MARK:SEAR:NPR calculate2:measure:sa:marker2:search:npr  
Query Syntax | Not Applicable  
Default | Not Applicable  
  
* * *

