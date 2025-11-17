# CALCulate:SA:MARKer commands

Controls the marker settings used in the SA application.

These commands are Superseded by the [CALCulate:MEASure:SA](MeasureSA.md)
commands.

CALCulate:SA:MARKer: BDENsity | ACPR | [:STATe] | BW | DATA? | EQSPan | NOISe | [:STATe] | NPR | [:STATe] | POWer | BW | [:STATe] | TONE | BW | [:STATe] | TSPacing BPOWer | [DATA?](SA.md#bpowData) | [SPAN](SA.md#bpowSpan) | [[:STATe]](SA.md#bpowState) OCCBand | CENTer? | PERCent | POWer? | SPAN? | [:STATe]  
---  
  
Click on a keyword to view the command details.

See Also

  * Marker Readout [number](../Display.md#single) and [size](../Display.md#size) commands.

  * [Learn about Markers](../../../S4_Collect/Markers.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

Critical Note: CALCulate commands act on the selected measurement. You can
select one measurement for each channel using
[Calc:Par:MNUM](Parameter.md#MnumSel) or
[Calc:Par:Select](Parameter.md#cps). [Learn
more](../../Learning_about_GPIB/Referring_to_Traces_Measurements_Channels_Windows_Using_SCPI.htm).  
  
If you use [Calc:Par:Cat?](Parameter.md#cpc) to return the list of current
measurements, the returned string will be similar to CH1_B_1,B.  
  
To select this measurement as a parameter for SA, you need to send
Calc:Par:Sel CH1_B_1.  
  
Moreover, most of the following commands will return +202, Parameter not
valid if they are called with marker number n, and marker number n is not
currently turned ON.

Important: Learn about [programming the reference
marker](../../../S4_Collect/Markers.htm#Number_of_Markers).

Note: For all band power marker family (this includes BNOise, BPOWer, OCCBand
markers) and when measuring wideband repetitive modulated signals, there is
basically 2 approaches to get good measurements:  
  
\- Either run the coherent mode of SA if the modulated test signal repetition
period or tone spacing is known and a frequency reference connection is made
between the signal source and the PNA (usually the 10 MHz ref signal BNC). See
SA Setup Coherence.  
  
\- Or make use of a RBW that is equal or smaller than 1/20 of the modulated
test signal tone spacing (rule of thumb). The test signal tone spacing is 1/
the test signal duration. For example, if the ARB file that generates the test
signal replays each 100 microseconds, it means the tone spacing is 10 kHz. So,
we recommend to set the RBW to 500 Hz or below.

* * *

## CALCulate<ch>:SA:MARKer<n>:BDENsity:ACPR[:STATe] <bool>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
or N524xB models with Option S93070xB  (Read-Write) Sets and reads the ACPR
density marker. See Critical Note  
---  
Parameters |   
<ch> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <ch> is set to 1.  
<n> | Marker number. If unspecified, <n> is set to 1.  
<bool> | Choose from: 0 - OFF \- Turn band density marker OFF. 1 - ON \- Turn band density marker ON.  
Examples | 'Select the measurement CALC2:PAR:SEL "M2SA_CH2_A" 'Create marker3 on that measurement CALC2:MARK3 ON 'Make it a band density noise marker CALC2:SA:MARK3:BDEN:ACPR:STAT 1  
Query Syntax | CALCulate<ch>:SA:MARKer<n>:BDENsity:ACPR[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<ch>:SA:MARKer<n>:BDENsity:BW <num>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-Write) Sets and reads the bandwidth of the band density marker. See
Critical Note  
---  
Parameters |   
<ch> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <ch> is set to 1.  
<n> | Marker number. If unspecified, <n> is set to 1.  
<num> | Choose a bandwidth.  
Examples | CALC:SA:MARK:BDEN:BW 1e6  
Query Syntax | CALCulate<ch>:SA:MARKer<n>:BDENsity:BW?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1 MHz  
  
* * *

## CALCulate<ch>:SA:MARKer<n>:BDENsity:DATA?

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-only) Returns the band density level in dBm/Hz from the band density
marker. See Critical Note  
---  
Parameters |   
<ch> | Channel number of the measurement. There must be a selected measurement on that SA channel. If unspecified, <ch> is set to 1.  
<n> | Band density marker number. If unspecified, <n> is set to 1.  
Examples | CALC:SA:MARK:BDEN:DATA? calculate2:sa:marker2:bdensity:data?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<ch>:SA:MARKer<n>:BDENsity:EQSPan <num>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-Write) Sets and reads the frequency span used by Power Density to
normalize the power. See Critical Note  
---  
Parameters |   
<ch> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <ch> is set to 1.  
<n> | Marker number. If unspecified, <n> is set to 1.  
<num> | Choose a span.  
Examples | CALC:SA:MARK:BDEN:EQSPan 1e6  
Query Syntax | CALCulate<ch>:SA:MARKer<n>:BDENsity:EQSPan?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1 MHz  
  
* * *

## CALCulate<ch>:SA:MARKer<n>:BDENsity:NOISe[:STATe] <bool>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-Write) Sets and reads the state of the band density noise marker.  See
Critical Note  
---  
Parameters |   
<ch> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <ch> is set to 1.  
<n> | Marker number. If unspecified, <n> is set to 1.  
<bool> | Choose from: 0 - OFF \- Turn band density noise marker OFF. 1 - ON \- Turn band density noise marker ON.  
Examples | 'Select the measurement CALC2:PAR:SEL "M2SA_CH2_A" 'Create marker3 on that measurement CALC2:MARK3 ON 'Make it a band density noise marker CALC:SA:MARK:BDEN:NOIS:STAT 1  
Query Syntax | CALCulate<ch>:SA:MARKer<n>:BDENsity:NOISe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<ch>:SA:MARKer<n>:BDENsity:NPR[:STATe] <bool>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
or N524xB models with Option S93070xB  (Read-Write) Sets and reads the NPR
density marker. See Critical Note  
---  
Parameters |   
<ch> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <ch> is set to 1.  
<n> | Marker number. If unspecified, <n> is set to 1.  
<bool> | Choose from: 0 - OFF \- Turn band density marker OFF. 1 - ON \- Turn band density marker ON.  
Examples | 'Select the measurement CALC2:PAR:SEL "M2SA_CH2_A" 'Create marker3 on that measurement CALC2:MARK3 ON 'Make it a band density noise marker CALC2:SA:MARK3:BDEN:NPR:STAT 1  
Query Syntax | CALCulate<ch>:SA:MARKer<n>:BDENsity:NPR[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<ch>:SA:MARKer<n>:BDENsity:POWer:BW <num>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-Write) Sets and reads the bandwidth of the band power density marker.
See Critical Note  
---  
Parameters |   
<ch> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <ch> is set to 1.  
<n> | Marker number. If unspecified, <n> is set to 1.  
<num> | Choose a bandwidth.  
Examples | CALC:SA:MARK:BDEN:POW:BW 1e6  
Query Syntax | CALCulate<ch>:SA:MARKer<n>:BDENsity:POWer:BW?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1 MHz  
  
* * *

## CALCulate<ch>:SA:MARKer<n>:BDENsity:POWer[:STATe] <bool>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-Write) Sets and reads the state of the band power density marker.  See
Critical Note  
---  
Parameters |   
<ch> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <ch> is set to 1.  
<n> | Marker number. If unspecified, <n> is set to 1.  
<bool> | Choose from: 0 - OFF \- Turn band power density marker OFF. 1 - ON \- Turn band power density marker ON.  
Examples | 'Select the measurement CALC2:PAR:SEL "M2SA_CH2_A" 'Create marker3 on that measurement CALC2:MARK3 ON 'Make it a band density noise marker CALC:SA:MARK:BDEN:POW:STAT 1  
Query Syntax | CALCulate<ch>:SA:MARKer<n>:BDENsity:POWer?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<ch>:SA:MARKer<n>:BDENsity:TONE:BW <num>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-Write) Sets and reads the bandwidth of the band tone density marker. See
Critical Note  
---  
Parameters |   
<ch> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <ch> is set to 1.  
<n> | Marker number. If unspecified, <n> is set to 1.  
<num> | Choose a bandwidth.  
Examples | CALC:SA:MARK:BDEN:TONE:BW 1e6  
Query Syntax | CALCulate<ch>:SA:MARKer<n>:BDENsity:TONE:BW?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1 MHz  
  
* * *

## CALCulate<ch>:SA:MARKer<n>:BDENsity:TONE[:STATe] <bool>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-Write) Sets and reads the state of the band tone density marker.  See
Critical Note  
---  
Parameters |   
<ch> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <ch> is set to 1.  
<n> | Marker number. If unspecified, <n> is set to 1.  
<bool> | Choose from: 0 - OFF \- Turn band tone density marker OFF. 1 - ON \- Turn band tone density marker ON.  
Examples | 'Select the measurement CALC2:PAR:SEL "M2SA_CH2_A" 'Create marker3 on that measurement CALC2:MARK3 ON 'Make it a band density noise marker CALC:SA:MARK:BDEN:TONE:STAT 1  
Query Syntax | CALCulate<ch>:SA:MARKer<n>:BDENsity:TONE?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<ch>:SA:MARKer<n>:BDENsity:TONE:TSPacing <num>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-Write) Sets and reads the spacing of the band tone density marker. See
Critical Note  
---  
Parameters |   
<ch> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <ch> is set to 1.  
<n> | Marker number. If unspecified, <n> is set to 1.  
<num> | Choose a spacing value.  
Examples | CALC:SA:MARK:BDEN:TONE:TSP 100e6  
Query Syntax | CALCulate<ch>:SA:MARKer<n>:BDENsity:TONE:TSPacing?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 100 MHz  
  
* * *

## CALCulate<ch>:SA:MARKer<n>:BPOWer:DATA?

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-only) Returns the band power level from the band power marker. See
Critical Note  
---  
Parameters |   
<ch> | Channel number of the measurement. There must be a selected measurement on that SA channel. If unspecified, <ch> is set to 1.  
<n> | Band power marker number. If unspecified, <n> is set to 1.  
Examples | CALC:SA:MARK:BPOW:DATA? calculate2:sa:marker2:bpower:data?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<ch>:SA:MARKer<n>:BPOWer:SPAN <num>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-Write) Sets and reads the frequency span of the band power marker. This
area is marked by two vertical dotted lines on the screen and the marker's
y-axis value is set to the measured power value. Noise and power on the same
marker share the same span. See Critical Note  
---  
Parameters |   
<ch> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <ch> is set to 1.  
<n> | Marker number. If unspecified, <n> is set to 1.  
<num> | Choose a frequency span within the frequency range of the analyzer.  
Examples | CALC:SA:MARK:BPOW:SPAN 1e6  
Query Syntax | CALCulate<ch>:SA:MARKer<n>:BPOWer:SPAN?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1 MHz  
  
* * *

## CALCulate<ch>:SA:MARKer<n>:BPOWer[:STATe] <bool>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-Write) Sets and reads the state of the band power marker. This command
makes a band power marker from a generic marker. The generic marker must first
be created using: [CALC:MARK:STATe](Marker.md#state) See Critical Note  
---  
Parameters |   
<ch> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <ch> is set to 1.  
<n> | Marker number. If unspecified, <n> is set to 1.  
<bool> | Choose from: 0 - OFF \- Turn band power marker OFF. 1 - ON \- Turn band power marker ON.  
Examples | 'Select the measurement CALC2:PAR:SEL "M2SA_CH2_A" 'Create marker3 on that measurement CALC2:MARK3 ON 'Make it a band power marker CALC:SA:MARK:BPOW:STAT 1  
Query Syntax | CALCulate<ch>:SA:MARKer<n>:BPOWer?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
## CALCulate<ch>:SA:MARKer<n>:OCCBand:CENTer?

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-only) Returns the occupied bandwidth center frequency. See Critical Note  
---  
Parameters |   
<ch> | Channel number of the measurement. There must be a selected measurement on that SA channel. If unspecified, <ch> is set to 1.  
<n> | Marker number. If unspecified, <n> is set to 1.  
Examples | CALC:SA:MARK:OCCB:CENT? calculate2:sa:marker2:occband:center?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<ch>:SA:MARKer<n>:OCCBand:PERCent <num>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-Write) Sets and returns the percentage of the band power to search for.
See Critical Note  
---  
Parameters |   
<ch> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <ch> is set to 1.  
<n> | Marker number. If unspecified, <n> is set to 1.  
<num> | Percentage value.  
Examples | CALC:SA:MARK:OCCB:PERC 99 calculate2:sa:marker2:occband:percent 99  
Query Syntax | CALCulate<ch>:SA:MARKer<n>:OCCBand:PERCent?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 99.0  
  
* * *

## CALCulate<ch>:SA:MARKer<n>:OCCBand:POWer?

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-only) Returns the occupied bandwidth power. See Critical Note  
---  
Parameters |   
<ch> | Channel number of the measurement. There must be a selected measurement on that SA channel. If unspecified, <ch> is set to 1.  
<n> | Marker number. If unspecified, <n> is set to 1.  
Examples | CALC:SA:MARK:OCCB:POW? calculate2:sa:marker2:occband:power?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<ch>:SA:MARKer<n>:OCCBand:SPAN?

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-only) Returns the occupied bandwidth span. See Critical Note  
---  
Parameters |   
<ch> | Channel number of the measurement. There must be a selected measurement on that SA channel. If unspecified, <ch> is set to 1.  
<n> | Marker number. If unspecified, <n> is set to 1.  
Examples | CALC:SA:MARK:OCCB:SPAN? calculate2:sa:marker2:occband:span?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<ch>:SA:MARKer<n>:OCCBand[:STATe] <bool>

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-Write) Sets and returns the occupied bandwidth on/off state. See
Critical Note  
---  
Parameters |   
<ch> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <ch> is set to 1.  
<n> | Marker number. If unspecified, <n> is set to 1.  
<bool> | Choose from: 0 - OFF \- Turns occupied bandwidth OFF. 1 - ON \- Turns occupied bandwidth ON.  
Examples | CALC:SA:MARK:OCCB:STAT 1 calculate2:sa:marker2:occband:state 1  
Query Syntax | CALCulate<ch>:SA:MARKer<n>:OCCBand[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 Note: If occupied band state is turned ON, then Band Power or Band Noise is turned OFF.  
  
* * *

