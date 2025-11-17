# Using Trace Control

  * Changing Trace Allocation

  * Coupling Marker/Time

  * [Target Annotation/Readout](Using_Trace_Control.md#TargetAnnotationReadout)

  * Copying Trace Setting

[Other topics about Making Measurement](Making_Measurements.md)

## Changing Trace Allocation

Changing the trace allocation affects the data display on the graph plot.
Table below shows the details of each selection:

Allocation | Details  
---|---  
Mixed | Display mixed of commonly measured time domain and S-parameter data  
All T | Display all Time Domain data for selected device topology  
All S | Display all S-Parameter data for selected device topology  
  
  1. Click the TDR/TDT tab.

  2. Click on the desired trace allocation in the Trace Control tab under Allocation.

## Coupling Marker, Time, Scale and Window Type / Rise Time

  1. Click the TDR/TDT tab.

  2. Click on the desired check box in Trace Control tab under Coupling.

  * Selecting Marker under Coupling enables all the marker on other traces to be moved in same alignment.

  * Selecting Time under Coupling enables all other traces using the same X axis (Time).

  * Selecting Rise Time under Coupling enables all other traces using the same rise time .

  * Selecting Scale under Coupling enables all other traces using the same scale .

  * Selecting Window / Rise Time under Coupling enables all other traces using the same window type / rise time .

## Target Annotation/Readout

  * Selecting Trace Annotation under Active Trace Only enables the trace annotation only on an active trace.

  * Selecting Marker Readout under Active Trace Only enables the marker readout only on an active trace.

## Copying Trace Setting

  1. Click on the Trace Settings Copy button. The Trace Settings Copy dialog box appears.

  2. Select the source trace in the From list. Select the desired destination trace in the To list.

  3. Click on the >> Copy >> button.

### Copied Parameter

The following parameters for the following functions are copied by the Trace
Settings Copy.

Functions | SCPI Commands  
---|---  
Parameter, Time Domain/S-Parameter, Single-Ended/Differential | CALCulate:TDR:MEASure:PARameter  
Format | CALCulate:TDR:MEASure:FORMat  
Marker | CALCulate:TDR:MEASure:ACTive:MARKer  
Peeling | CALCulate:TDR:MEASure:PEELing:STATe  
Delta Time Dialog | CALCulate:TDR:MEASure:DTIMe:POSition  
CALCulate:TDR:MEASure:DTIMe:STATe  
Delta Time Target [Target is trace for stop] | CALCulate:TDR:MEASure:DTIMe:TARGet  
Gating Start | CALCulate:MEASure:FILTer:GATE:TIME:STARt  
Gating State | CALCulate:MEASure:FILTer:GATE:TIME:STATe  
Gating Stop | CALCulate:MEASure:FILTer:GATE:TIME:STOP  
Gating Type | CALCulate:MEASure:FILTer:GATE:TIME:TYPE  
Marker Search [ON/OFF], marker [0-9, ref] | CALCulate:MEASure:MARKer:FUNCtion:TRACking  
Marker Search [MIN/MAX], marker [0-9, ref] | CALCulate:MEASure:MARKer:FUNCtion:SELect  
Reference Marker [ON/OFF] | CALCulate:MEASure:MARKer:REFerence:STATe  
Marker | CALCulate:MEASure:MARKer:STATe  
Marker [x-axis value] | CALCulate:MEASure:MARKer:X  
Smoothing | CALCulate:MEASure:SMOothing:STATe  
Impulse Width Value for Lowpass Impulse | CALCulate:MEASure:TRANsform:TIME:IMPulse:WIDTh  
Rise Time (for all traces) | CALCulate:MEASure:TRANsform:TIME:STEP:RTIMe  
CALCulate:MEASure:TRANsform:TIME:STEP:RTIMe:THReshold  
Stimulus | CALCulate:MEASure:TRANsform:TIME:TYPE  
Search Rise Time | CALCulate:TDR:MEASure:TTIMe:STATe  
CALCulate:TDR:MEASure:TTIMe:THReshold  
Horizontal Scale | DISPlay:TDR:MEASure:X:SCALe:PDIVision  
Horizontal Position | DISPlay:TDR:MEASure:X:SCALe:RLEVel  
Vertical Scale | DISPlay:TDR:MEASure:Y:SCALe:PDIVision  
Vertical Position | DISPlay:TDR:MEASure:Y:SCALe:RLEVel

