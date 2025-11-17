# CALCulate:MEASure:GCData Commands

Reads Gain Compression data from the current Gain Compression acquisition.

CALCulate:MEASure:GCData DATA IMAG ITERations REAL  
---  
  
Click a keyword to view the command details.

### Other Gain Compression commands

The calibration commands listed in this topic are supplemental to the Guided
Cal commands.

  * [CALC:MEAS:DEFine](Measure.md#CALCulate:MEASure:DEFine) \- creates a gain compression measurement.

  * [SENS:GCSetup](../Sense/Gain_Compression.md) \- Most Gain Compression settings.

  * [CALC:MEAS:GCMeas:ANAL](MeasureGCMeas.md) \- Gain Compression Analysis settings

  * Gain compression data can also be saved to a *.csv file. [Learn how.](../../../Applications/Gain_Compression_Application.md#Saving2D)

See Also

  * [Learn about Gain Compression Application](../../../Applications/Gain_Compression_Application.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## CALCulate<ch>:MEASure<mnum>:GCData:DATA? <param>

Applicable Models: All with Option S93070xB or S9x070B (Read-Only) Returns
measurement data at all frequency and power data points for GCA SMART sweeps
and 2D sweeps.

  * When using SMART sweep, ALL data is returned including ALL background iteration sweeps. Use CALC:MEAS:GCD:ITER to determine the number of iteration sweeps. The number of data points that are returned is always going to be number of frequency points times the number of iteration sweeps.
  * When using 2D sweeps, ALL data is returned. The number of data points returned / freq may vary. [Learn more.](../../../Applications/Gain_Compression_Application.md#Saving)

Use [CALC:MEAS:DATA?](MeasureDATA.md) to return just the displayed data
results (not the background sweeps). A compression parameter must be present.
[Learn
more](../../../Applications/Gain_Compression_Application.htm#CompressionParams).
The format of the data is the same as the format of the measurement that you
select using
[CALC:MEAS:PAR](MeasurePARameter.md#CALCulate:MEASure:PARameter). If the
measurement is scalar, than one number is returned per sweep per data point.
If complex (such as Smith Chart format) than both real and imaginary numbers
are returned. If correction is on, corrected data are returned. Otherwise, raw
data are returned.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<param> | (String) Parameter to read. NOT Case-sensitive. The specified parameter need NOT be displayed or selected. However, a compression parameter must be present. [Learn more](../../../Applications/Gain_Compression_Application.md#CompressionParams). Choose from:

  * "pin" \- (CompIn21) Input power at the compression point.
  * "pout" \- (CompOut21) Output power at the compression point.
  * "gain" \- (CompGain21) Device gain (S21) at the compression point.
  * "inputmatch" \- (CompS11) Input match at the compression point.
  * "DeltaGain" \- (DeltaGain21) Measured Gain (watts) / Ref Gain (watts). [Learn more.](../../../Applications/Gain_Compression_Application.md#DeltaGain21)
  * "AI1" and "AI2" \- ADC measurements at the specified compression level. [Learn more.](../../../Applications/Gain_Compression_Application.md#ADC)

[Learn more about GCA
parameters.](../../../Applications/Gain_Compression_Application.htm#Parameters)  
Examples | data = CALC:MEAS2:GCD:DATA? "pin" data = calculate:measure2:gcdata:data? "pout"  
Return Type | Array of data  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:GCData:IMAG? <char>, <dpoint>, <param>

Applicable Models: All with Option S93070xB or S9x070B (Read-Only) For a
specified data point, returns the imaginary part of the specified Gain
Compression data. If correction is on, corrected data are returned. Otherwise,
raw data are returned. Can be used with Smart and 2D sweeps.

  * For SMART sweep, the number of data points that are returned is always going to be the number of iteration sweeps. Use CALC:MEAS:GCD:ITER to determine the number of iteration sweeps.
  * For 2D sweeps, the number of data points returned / freq may vary. [Learn more.](../../../Applications/Gain_Compression_Application.md#Saving)

  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<char> | Choose from:

  * FREQuency \- for the specified frequency data point, returns all of the measured data for each power stimulus.
  * POWer \- for the specified power data point, returns all of the measured data for each frequency stimulus.

  
<dPoint> | Data point (FREQ or POWer) for which data is returned.  
<param> | (String) Parameter to read. NOT Case-sensitive. The specified parameter need NOT be displayed. However, a compression parameter must be present. [Learn more](../../../Applications/Gain_Compression_Application.md#CompressionParams).

  * "pin" \- (CompIn21) Input power at the compression point.
  * "pout" \- (CompOut21) Output power at the compression point.
  * "gain" \- (CompGain21) Device gain (S21) at the compression point.
  * "inputmatch" \- (CompS11) Input match at the compression point.
  * "DeltaGain" \- (DeltaGain21) Measured Gain (watts) / Ref Gain (watts). [Learn more.](../../../Applications/Gain_Compression_Application.md#DeltaGain21)
  * "AI1" and "AI2" \- ADC measurements at the specified compression level. [Learn more.](../../../Applications/Gain_Compression_Application.md#ADC)

  
Examples | For the fifth frequency data point, returns 'Power Output' imaginary (phase) data from all power stimulus values. For SmartSweep, if there are 30 power sweep points, 30 values are returned. For 2D sweeps, 30 or 31 power sweep points may be returned. [Learn more.](../../../Applications/Gain_Compression_Application.md#Saving) data = CALC:MEAS2:GCD:IMAG? FREQ,5,"pout"  
Return Type | Array of data  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:GCData:ITERations?

Applicable Models: All with Option S93070xB or S9x070B (Read-only) In a SMART
sweep, returns the max number of iterations that it took for ALL frequencies
to converge. Use this number to determine the size of the block data that is
returned from Gain Compression SMART sweep data queries. For a 2D sweep,
returns the number of power points.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | data = CALC:MEAS2:GCD:ITER?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<ch>:MEASure<mnum>:GCData:REAL? <char>, <dpoint>, <param>

Applicable Models: All with Option S93070xB or S9x070B (Read-Only) For a
specified data point, returns the real part of the Gain Compression data. If
correction is on, corrected data are returned. Otherwise, raw data are
returned. Can be used with Smart and 2D sweeps.

  * For SMART sweep, the number of data points that are returned is always going to be the number of iteration sweeps. Use CALC:MEAS:GCD:ITER to determine the number of iteration sweeps.
  * For 2D sweeps, the number of data points returned / freq may vary. [Learn more.](../../../Applications/Gain_Compression_Application.md#Saving)

  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<char> | Choose from:

  * FREQuency \- for the specified frequency data point, returns all of the measured data for each power stimulus.
  * POWer \- for the specified power data point, returns all of the measured data for each frequency stimulus.

  
<dPoint> | Data point (FREQ or POWer) for which data is returned.  
<param> | (String) Parameter to read. NOT Case-sensitive. The specified parameter need NOT be displayed. However, a compression parameter must be present. [Learn more](../../../Applications/Gain_Compression_Application.md#CompressionParams).

  * "pin" \- (CompIn21) Input power at the compression point.
  * "pout" \- (CompOut21) Output power at the compression point.
  * "gain" \- (CompGain21) Device gain (S21) at the compression point.
  * "inputmatch" \- (CompS11) Input match at the compression point.
  * "DeltaGain" \- (DeltaGain21) Measured Gain (watts) / Ref Gain (watts). [Learn more.](../../../Applications/Gain_Compression_Application.md#DeltaGain21)
  * "AI1" and "AI2" \- ADC measurements at the specified compression level. [Learn more.](../../../Applications/Gain_Compression_Application.md#ADC)

  
Examples | For the fifth frequency data point, returns 'Power Output' real data from all power stimulus values. For SmartSweep, if there are 30 power sweep points, 30 values are returned. For 2D sweeps, 30 or 31 power sweep points may be returned. [Learn more.](../../../Applications/Gain_Compression_Application.md#Saving) data = CALC:MEAS2:GCD:REAL? FREQ,5,"pout"  
Return Type | Array of data  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

