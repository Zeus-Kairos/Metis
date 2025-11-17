# DISPlay:TDR Commands

These commands control the TDR display setup.

DISPlay:TDR EYE | Y | SCALe | AUTO | STATe | PDIVision | RLEVel | RPOSition IMAGe MEASure | DMEMory | TYPE | X | SCALe | AUTO | PDIVision | RLEVel MINimize:STATe SCALe | AUTO VIEW X | SCALe | RPOSition  
---  
  
Click on a red keyword to view the command details.

See Also

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## DISPlay:TDR:EYE:Y:SCALe:AUTO:STATe <bool>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) Turns the
continuous auto-scale mode for the eye y-axis ON or OFF.  
---  
Parameters |   
<bool> | ON or 1 \- Turns continuous auto-scale ON.  
OFF or 0 \- Turns continuous auto-scale OFF.  
Examples | DISP:TDR:EYE:Y:SCAL:AUTO:STAT ON  
display:tdr:eye:y:scale:auto:state off  
Query Syntax | DISPlay:TDR:EYE:SCALe:AUTO:STATe?  
Return Type | Boolean  
Default | ON  
  
* * *

## DISPlay:TDR:EYE:Y:SCALe:PDIVision <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the value of the y-axis scale per division for eye diagram.  
---  
Parameters |   
<value> | Value of eye diagram y-axis scale per division. The range is 1E-18 to 5.  
Examples | DISP:TDR:EYE:Y:SCAL:PDIV 300E-03  
display:tdr:eye:y:scale:pdivision 300e-03  
Query Syntax | DISPlay:TDR:EYE:Y:SCALe:PDIVision?  
Return Type | Double  
Default |  0.2  
  
* * *

## DISPlay:TDR:EYE:Y:SCALe:RLEVel <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the value of the eye diagram y-axis reference line.  
---  
Parameters |   
<value> | Value of eye diagram y-axis reference line. The range is -5 to +5.  
Examples | DISP:TDR:EYE:Y:SCAL:RLEV 0.01  
display:tdr:eye:y:scale:rlevel 0.01  
Query Syntax | DISPlay:TDR:EYE:Y:SCALe:RLEVel?  
Return Type | Double  
Default | 0  
  
* * *

## DISPlay:TDR:EYE:Y:SCALe:RPOSition <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the value of the eye diagram y-axis reference position.  
---  
Parameters |   
<value> | Value of eye diagram y-axis reference position. The range is 0 to 10.  
Examples | DISP:TDR:EYE:Y:SCAL:RPOS 10  
display:tdr:eye:y:scale:rposition 10  
Query Syntax | DISPlay:TDR:EYE:Y:SCALe:RPOSition?  
Return Type | Integer  
Default | 4  
  
* * *

## DISPlay:TDR:IMAGe <enum>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
changes the background color of the screen.  
---  
Parameters |   
<enum> | Screen background color. Choose from: NORMal \- Black background color. INVert \- White background color.  
Examples | DISP:TDR:IMAG NORM  
display:tdr:image normal  
Query Syntax | DISPlay:TDR:IMAGe?  
Return Type | String  
Default | NORMal  
  
* * *

## DISPlay:TDR:MEASure[1-16]:DMEMory:TYPE <enum>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the display to off, data type, memory type, or data and memory type.  
---  
Parameters |   
<enum> | Data/memory display. Choose from: OFF \- Nothing is displayed on the graph plot. DATA \- Data only is displayed on the graph plot. MEMory \- Memory only is displayed on the graph plot. DMEMory \- Data and Memory are displayed on the graph plot.  
Examples | DISP:TDR:MEAS1:DMEM:TYPE OFF  
display:tdr:measure1:dmemory:type off  
Query Syntax | DISPlay:TDR:MEASure[1-16]:DMEMory:TYPE?  
Return Type | String  
Default | DATA  
  
* * *

## DISPlay:TDR:MEASure[1-16]:X:SCALe:AUTO

Applicable Models: All with TDR Options (S9x011A/B) (Write-only) This command
executes x-axis auto scaling.  
---  
Examples | DISP:TDR:MEAS1:X:SCAL:AUTO display:tdr:measure1:x:scale:auto  
  
* * *

## DISPlay:TDR:MEASure[1-16]:X:SCALe:PDIVision <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the value of the x-axis scale per division.  
---  
Parameters |   
<value> | Value of x-axis scale per division.  
Examples | DISP:TDR:MEAS1:X:SCAL:PDIV 1E-9  
display:tdr:measure1:scale:pdivision 1e-9  
Query Syntax | DISPlay:TDR:MEASure[1-16]:X:SCALe:PDIVision?  
Return Type | Double  
Default | 2n  
  
* * *

## DISPlay:TDR:MEASure[1-16]:X:SCALe:RLEVel <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the value of the x-axis reference line.  
---  
Parameters |   
<value> | Value of x-axis reference line.  
Examples | DISP:TDR:MEAS1:X:SCAL:RLEV 20E-9  
display:tdr:measure1:x:scale:rlevel 20e-9  
Query Syntax | DISPlay:TDR:MEASure[1-16]:X:SCALe:RLEVel?  
Return Type | Double  
Default | 10n  
  
* * *

## DISPlay:TDR:MINimize:STATe <bool>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) Sets or gets
the minimize state.  
---  
Parameters |   
<bool> | ON or 1 \- Turns minimize state ON.  
OFF or 0 \- Turns minimize state OFF.  
Examples | DISP:TDR:MIN:STAT ON  
display:tdr:minimize:state off  
Query Syntax | DISPlay:TDR:MINimize:STATe?  
Return Type | Boolean  
Default | OFF  
  
* * *

## DISPlay:TDR:SCALe:AUTO

Applicable Models: All with TDR Options (S9x011A/B) (Write-only) This command
executes y-axis auto scaling.  
---  
Examples | DISP:TDR:SCAL:AUTO display:tdr:scale:auto  
  
* * *

## DISPlay:TDR:VIEW <enum>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
selects the view point for waveform analysis either before or after the DUT.  
---  
Parameters |   
<enum> | X-axis reference position. Choose from: STIMulus \- Stimulus view, observation point before DUT. RESPonse \- Response view, observation point after DUT.  
Examples | DISP:TDR:VIEW STIM  
display:tdr:view stimulus  
Query Syntax | DISPlay:TDR:VIEW?  
Return Type | String  
Default | RESPonse  
  
* * *

## DISPlay:TDR:X:SCALe:RPOSition <enum>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the x-axis reference position for the time domain measurement.  
---  
Parameters |   
<enum> | X-axis reference position. Choose from: LEFT \- Reference position is the left edge. CENTer \- Reference position is center.  
Examples | DISP:TDR:SCAL:RPOS LEFT  
display:tdr:scale:rposition left  
Query Syntax | DISPlay:TDR:SCALe:RPOSition?  
Return Type | String  
Default | LEFT  
  
* * *

##

