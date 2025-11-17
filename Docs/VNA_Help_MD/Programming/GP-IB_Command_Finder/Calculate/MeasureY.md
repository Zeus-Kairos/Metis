# CALCulate:MEASure:Y Commands

Controls the display of Y-axis for various measurements.

CALCulate:MEASure:Y AXIS | UNIT? [:VALues]  
---  
  
Click a keyword to view the command details.

See Also

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## CALCulate<ch>:MEASure<mnum>:Y:AXIS:UNIT?

Applicable Models: All (Read-only) Returns the current units of the Y-axis (HZ | SECond | MINute | HOUR | DAY | DB | DBM | DBMV | WATTs | FARad | HENRy | OHM | MHO | SIEMen | VOLT | DEGRee | RADians | METer | DPHZ | UNIT | NONe | TNORmalized | NTEMperature | KELVin|CENTigrade | FAHRenheit | FEET | INCH | DBMAAMPere | VOLTAge | DBUV | PERCentage | DMVRoothz | DUVRoothz | DMARoothz | WPHZ | VROothz | AROothz | DBC | DVPerhz | DCPerhz | DBPerhz | HZPerhz | PRHz | VPHz | DBV|DEFault). This command can be used for all Measurement Classes.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:Y:AXIS:UNIT?  
Return Type | Enumeration  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | FREQuency  
  
* * *

## CALCulate<ch>:MEASure<mnum>:Y[:VALues]?

Applicable Models: All (Read-only) Returns the Y-axis values for the selected
measurement in the current units. This command can be used for all Measurement
Classes.  
---  
Parameters |   
<ch> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:Y?  
Return Type | Array of data  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable

