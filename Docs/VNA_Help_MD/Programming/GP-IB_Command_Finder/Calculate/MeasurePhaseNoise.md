# CALCulate:MEASure:PN Commands

Defines the settings for phase noise measurements. Option S93031xB is required
and applies ONLY to instruments with serial prefix 6021 and above.

CALCulate:MEASure:PN AVARiance: | DEViation | JITTer | VARiance CARRier | FREQuency | LEVel DATA | PDATa | PMEMory | SPData | SPMemory INTegral | RANGe | DATA | STARt | STOP | TYPE | WEIGhting SNOise | DECades | [:STATe] | X | Y | [:STATe] | USER | [:STATe] | X | Y SPURious | ANALysis | [:STATe] | DATA | OMISsion | [:STATe] | OSSPur | DATA | DELete | [:STATe] | SENSibility | SORT | THReshold | LEVel | MINimum | TABle | DATA | DELete  
---  
  
Click a keyword to view the command details.

See Also

  * [Calibrating with SCPI](../../Learning_about_GPIB/Calibrating_the_Analyzer_Using_SCPI.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## CALCulate<ch>:MEASure<mnum>:PN:AVARiance:DEViation? <avg_time>,<fcutoff>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-only)
Returns the calculated Allan deviation using the measured average time and the
measured cut-off frequency for the selected measurement.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<avg_time> | Measured average time (sec).  
<fcutoff> | Measured cut-off frequency (Hz).  
Examples | CALC:MEAS2:PN:AVAR:DEV? 0.001,10 kHz calculate2:measure2:pn:avariance:deviation? 0.001,10 kHz  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:AVARiance:JITTer? <avg_time>,<fcutoff>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-only)
Returns the calculated Jitter using the measured average time and the measured
cut-off frequency for the selected measurement.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<avg_time> | Measured average time (sec).  
<fcutoff> | Measured cut-off frequency (Hz).  
Examples | CALC:MEAS2:PN:AVAR:JITT? 0.001,10 kHz calculate2:measure2:pn:avariance:jitter? 0.001,10 kHz  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:AVARiance:VARiance? <avg_time>,<fcutoff>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-only)
Returns the calculated Allan variance using the measured average time and the
measured cut-off frequency for the selected measurement.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<avg_time> | Measured average time (sec).  
<fcutoff> | Measured cut-off frequency (Hz).  
Examples | CALC:MEAS2:PN:AVAR:VAR? 0.001,10 kHz calculate2:measure2:pn:avariance:variance? 0.001,10 kHz  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:CARRier:FREQuency?

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-only)
Returns the measured carrier frequency.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:PN:CARR:FREQ? calculate2:measure2:pn:carrier:frequency?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:CARRier:LEVel?

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-only)
Returns the measured carrier power level.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:PN:CARR:LEV? calculate2:measure2:pn:carrier:level?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:DATA:PDATa

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Sets and returns the dBc data array for the selected measurement.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:PN:DATA:PDAT -81.285,-97.663,-100.02,-100.15,-103.37,-117.93 calculate2:measure2:pn:data:pdata -81.285,-97.663,-100.02,-100.15,-103.37,-117.93  
Query Syntax | CALCulate<ch>:MEASure<mnum>:PN:DATA:PDATa?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:DATA:PMEMory

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Sets and returns the dBc memory data for the selected measurement.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:PN:DATA:PDAT -81.285,-97.663,-100.02,-100.15,-103.37,-117.93 calculate2:measure2:pn:data:pdata -81.285,-97.663,-100.02,-100.15,-103.37,-117.93  
Query Syntax | CALCulate<ch>:MEASure<mnum>:PN:DATA:PDATa?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:DATA:SPData?

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-only)
Returns the spurious data (0 or 1) for the selected measurement.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:PN:DATA:SPData? calculate2:measure2:pn:data:spdata?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:DATA:SPMemory?

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-only)
Returns the spurious memory data (0 or 1) for the selected measurement.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:PN:DATA:SPMemory? calculate2:measure2:pn:data:spmemory?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:INTegral:RANGe[1-4]:DATA? <enum>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-only)
Returns the specified data for the selected range number. RANGe[1-4] allows
selection of the desired integration range. The following commands are used to
configure these integration ranges:
CALCulate<ch>:MEASure<mnum>:PN:INTegral:RANGe[1-4]:TYPE
CALCulate<ch>:MEASure<mnum>:PN:INTegral:RANGe[1-4]:STARt
CALCulate<ch>:MEASure<mnum>:PN:INTegral:RANGe[1-4]:STOP
CALCulate<ch>:MEASure<mnum>:PN:INTegral:RANGe[1-4]:WEIGhting  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<enum> | (Enumeration) Choose from: IPN \- Integrated Noise RFM \- Residual FM RAM \- Residual AM RPM \- Residual PM RMSJ \- RMS Jitter RMSR \- RMS Radian RMSD \- RMS Degree  
Examples | CALC:MEAS2:PN:INT:RANG1:DATA? IPN calculate2:measure2:pn:range1:data? RFM  
Return Type | Numeric  
Default | IPN  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:INTegral:RANGe[1-4]:STARt <value>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Sets and returns the start frequency of the selected integration range.
RANGe[1-4] allows selection of the desired integration range. The
CALCulate:MEASure:PN:INTegral:RANGe:TYPE command must be set to CUSTom.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<value> | Start frequency of integration range. If the range is unspecified, the start frequency is assigned to RANGe1.  
Examples | CALC:MEAS2:PN:INT:RANG1 10 MHz calculate2:measure2:pn:integral:range1:start 10 MHz  
Query Syntax | CALCulate<ch>:MEASure<mnum>:PN:INTegral:RANGe[1-4]:STARt?  
Return Type | Numeric  
Default | Minimum frequency of the analyzer  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:INTegral:RANGe[1-4]:STOP <value>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Sets and returns the stop frequency of the selected integration range.
RANGe[1-4] allows selection of the desired integration range. The
CALCulate:MEASure:PN:INTegral:RANGe:TYPE command must be set to CUSTom.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<value> | Stop frequency of integration range. If the range is unspecified, the stop frequency is assigned to RANGe1.  
Examples | CALC:MEAS2:PN:INT:RANG1 10 GHz calculate2:measure2:pn:integral:range1:start 10 GHz  
Query Syntax | CALCulate<ch>:MEASure<mnum>:PN:INTegral:RANGe[1-4]:STOP?  
Return Type | Numeric  
Default | Maximum frequency of the analyzer  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:INTegral:RANGe[1-4]:TYPE <enum>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Sets and returns the integration range type of the selected integration
range. RANGe[1-4] allows selection of the desired integration range.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<enum> | (Enumeration) Choose from: OFF \- Turn integration range off. The range will not be measured. FULL \- Set integration range to full span. CUSTom \- Set user-defined start and stop frequency range.  
Examples | CALC:MEAS2:PN:INT:RANG1:TYPE FULL calculate2:measure2:pn:range1:type full  
Query Syntax | CALCulate<ch>:MEASure<mnum>:PN:INTegral:RANGe[1-4]:TYPE?  
Return Type | Enumeration  
Default | OFF  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:INTegral:RANGe[1-4]:WEIGhting <string>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Sets and returns the weighting filter of the selected integration
range. RANGe[1-4] allows selection of the desired weighting filter. This
command selects a weighting filter whose values are applied to the calculation
of residual effects. The file should be saved in the following directory:
C:\Program Data\Keysight\Network Analyzer\WeightingFilter.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<string> | Weighting filter file name which contains the weighting data.  
Examples | CALC:MEAS2:PN:INT:RANG1:WEIG "Filter_A" calculate2:measure2:pn:range1:weighting "Filter_A"  
Query Syntax | CALCulate<ch>:MEASure<mnum>:PN:INTegral:RANGe[1-4]:WEIGhting?  
Return Type | String  
Default | Not applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:SNOise:DECades[:STATe] <bool>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Enables and disables the spot noise calculation on every decade offset
frequency.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<bool> | Choose from: 0 - OFF \- Disable spot noise calculation on every decade offset frequency. 1 - ON \- Enable spot noise calculation on every decade offset frequency.  
Examples | CALC:MEAS2:PN:SNOise:DECades ON calculate2:measure2:pn:snoise:decades:state ON  
Query Syntax | CALCulate<ch>:MEASure<mnum>:PN:SNOise:DECades[:STATe]?  
Return Type | Boolean  
Default | ON  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:SNOise:DECades:X?

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-only)
Returns the spot noise x-axis array of all decade offset frequencies.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:PN:SNO:DEC:X? calculate2:measure2:pn:snoise:decades:x?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:SNOise:DECades:Y?

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-only)
Returns the spot noise y-axis array of all decade offset frequencies.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:PN:SNO:DEC:Y? calculate2:measure2:pn:snoise:decades:y?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:SNOise[:STATe] <bool>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Enables and disables spot noise calculation for the selected
measurement number.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<bool> | Choose from: 0 - OFF \- Disable spot noise. 1 - ON \- Enable spot noise.  
Examples | CALC:MEAS2:PN:SNOise ON calculate2:measure2:pn:snoise:state ON  
Query Syntax | CALCulate<ch>:MEASure<mnum>:PN:SNOise[:STATe]?  
Return Type | Boolean  
Default | OFF  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:SNOise:USER[1-6][:STATe] <bool>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Enables and disables spot noise calculation for the specified user-
defined offset frequency.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<bool> | Choose from: 0 - OFF \- Disable spot noise calculation for the specified user-defined offset frequency. 1 - ON \- Enable spot noise calculation for the specified user-defined offset frequency.  
Examples | CALC:MEAS2:PN:SNOise:USER2 ON calculate2:measure2:pn:snoise:user2:state ON  
Query Syntax | CALCulate<ch>:MEASure<mnum>:PN:SNOiseUSER[1-6][:STATe]?  
Return Type | Boolean  
Default | ON  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:SNOise:USER[1-6]:X

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Sets and returns the offset frequency on which the spot noise is
calculated. Up to six offset frequencies can be defined.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:PN:SNO:USER2:X 1.234 kHz calculate2:measure2:pn:snoise:user2:x 1.234 kHz  
Query Syntax | CALCulate<ch>:MEASure<mnum>:PN:SNOiseUSER[1-6]:X?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:SNOise:USER[1-6]:Y?

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-only)
Returns the spot noise y-axis value of the specified offset frequency. The
offset frequency is defined using the CALCulate:MEASure:PN:SNOise:USER[1-6]:X
command.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:PN:SNO:USER2:Y? calculate2:measure2:pn:snoise:user2:y?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:SPURious:ANALysis[:STATe] <bool>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Enables and disables spurious analysis.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<bool> | Choose from: 0 - OFF \- Disable spurious analysis. 1 - ON \- Enable spurious analysis.  
Examples | CALC:MEAS2:PN:SPUR:ANAL ON calculate2:measure2:pn:spurious:analysis:state ON  
Query Syntax | CALCulate<ch>:MEASure<mnum>:PN:SPURious:ANALysis[:STATe]?  
Return Type | Boolean  
Default | OFF  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:SPURious:DATA?

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-only)
Returns a list of detected spurs. Data per spur includes frequency, power, and
jitter.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:PN:SPUR:DATA? calculate2:measure2:pn:spurious:data?  
Return Type | Array  
Default | Not applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:SPURious:OMISsion[:STATe] <bool>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Enables and disables spur omission.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<bool> | Choose from: 0 - OFF \- Disable spurious omission. 1 - ON \- Enable spurious omission.  
Examples | CALC:MEAS2:PN:SPUR:OMIS ON calculate2:measure2:pn:spurious:omission:state ON  
Query Syntax | CALCulate<ch>:MEASure<mnum>:PN:SPURious:OMISsion[:STATe]?  
Return Type | Boolean  
Default | OFF  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:SPURious:OSSPur:DATA <data>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Sets and returns the User Spur Table data which defines spurs to omit.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<data> | (Array) List of spurious frequencies of spurs to omit.  
Examples | CALC:MEAS2:PN:SPUR:OSSP:DATA 1.0e3,10.0e3 calculate2:measure2:pn:spurious:osspur:data 1.0e3,10.0e3  
Query Syntax | CALCulate<ch>:MEASure<mnum>:PN:SPURious:OSSPur:DATA?  
Return Type | Array  
Default | Not applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:SPURious:OSSPur:DELete

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Write-
only) Deletes the User Spur Table data which defines spurs to omit.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:PN:SPUR:OSSP:DEL  calculate2:measure2:pn:spurious:osspur:delete   
Default | Not applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:SPURious:OSSPur[:STATe] <bool>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Enables and disables user specified spur omission.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<bool> | Choose from: 0 - OFF \- Disable user specified spurious omission. 1 - ON \- Enable user specified spurious omission.  
Examples | CALC:MEAS2:PN:SPUR:OSSP ON calculate2:measure2:pn:spurious:osspur:state ON  
Query Syntax | CALCulate<ch>:MEASure<mnum>:PN:SPURious:OSSPur[:STATe]?  
Return Type | Boolean  
Default | OFF  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:SPURious:SENSibility <num>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Sets and returns the spurious sensibility number.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<num> | Spurious sensibility value. The default is 3 (3 x standard deviation).  
Examples | CALC:MEAS2:PN:SPUR:SENS 3 calculate2:measure2:pn:spurious:sensibility 3  
Query Syntax | CALCulate<ch>:MEASure<mnum>:PN:SPURious:SENSibility?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:SPURious:SORT <enum>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Sets and returns the spurious table sorting order.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<enum> | (Enumeration) Choose from: POWer \- Sort spurious table by power. OFFSet \- Sort spurious table by offset.  
Examples | CALC:MEAS2:PN:SPUR:SORT POW calculate2:measure2:pn:spurious:sort offset  
Query Syntax | CALCulate<ch>:MEASure<mnum>:PN:SPURious:SORT?  
Return Type | Enumeration  
Default | POWer  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:SPURious:THReshold:LEVel:MINimum <num>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Sets and returns the minimum spurious threshold level.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<num> | Minimum spurious threshold level. The range is -500 dBC to 500 dBc.  
Examples | CALC:MEAS2:PN:SPUR:THR:LEV:MIN -500 dBc calculate2:measure2:pn:spurious:threshold:level:minimum -500 dBc  
Query Syntax | CALCulate<ch>:MEASure<mnum>:PN:SPURious:THReshold:LEVel:MINimum?  
Return Type | Numeric  
Default | -500  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:SPURious:THReshold:TABle:DATA <data>

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Read-
Write) Sets and returns the spurious threshold table data.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<data> | (Array) Spurious threshold table data: start freq, lower threshold (dB), upper threshold (dB).  
Examples | CALC:MEAS2:PN:SPUR:THR:TAB:DATA 1,0,10 calculate2:measure2:pn:spurious:threshold:table:data 1,0,10  
Query Syntax | CALCulate<ch>:MEASure<mnum>:PN:SPURious:THReshold:TABle:DATA?  
Return Type | Array  
Default | Not applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:PN:SPURious:THReshold:TABle:DELete

Applicable Models: N522xB, N524xB with Phase Noise Option S93031xB (Write-
only) Deletes the spurious threshold table.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:PN:SPUR:THR:TAB:DEL calculate2:measure2:pn:spurious:threshold:table:delete  
Default | Not applicable  
  
* * *

