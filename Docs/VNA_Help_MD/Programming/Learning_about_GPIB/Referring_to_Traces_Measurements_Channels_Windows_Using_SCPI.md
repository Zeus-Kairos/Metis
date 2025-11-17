# Referring to Traces, Measurements, Channels, and Windows Using SCPI

* * *

Sometimes in a SCPI program you may need to refer to traces that you have not
created. This can be a bit confusing in the VNA. Here are the THREE ways to
refer to a specific measurement trace.

Note: The terms "Trace" and "Measurement" effectively mean the same thing in
this discussion.

  1. The Measurement Name is picked by you when you first create a trace using the [CALCulate<cnum>:PARameter[:DEFine]:EXTended <Mname>,<param>](../GP-IB_Command_Finder/Calculate/Parameter.md#DefineExtend) command. The measurement name is only used by SCPI.

  2. The Trace Number is also picked by you when feeding a newly-created measurement name to a window number using [DISP:WINDow<wmun>:TRACe<tnum>:FEED](../GP-IB_Command_Finder/Display.md#dwtf). The trace number is used ONLY by SCPI and is mainly used to refer to traces in the DISPlay node. This is NOT the number that appears as Tr# on the screen. While you can assign any Trace number you want, when a measurement is created from the GUI, the VNA assigns numbers to the traces sequentially, starting with one in each window. Therefore, when there is more than one window, these numbers are not unique.

  3. The Tr# that appears on the VNA screen is the third and most visible way to refer to a trace. Since we already have a "Trace Number", we call this the Measurement Number in the VNA Help file. This number is issued sequentially by the VNA regardless of channel and window. It is therefore unique among all traces. Use [CALC<ch>:PAR:MNUM](../GP-IB_Command_Finder/Calculate/Parameter.md#MnumSel)? just after the trace is created to read the measurement number.

The concept of the Active measurement versus Selected Measurement is also a
bit confusing. As seen on the screen, the Active measurement has the
highlighted Tr# . While there can only be ONE active measurement, every
channel has a selected measurement. The target measurement must first be
selected before most CALC node settings can be made. There are two ways to
select a measurement for each channel:

  1. Use [CALC<ch>:PAR:SEL <measName>](../GP-IB_Command_Finder/Calculate/Parameter.md#cps) which requires the channel number and measurement name.

  2. Use [CALC<ch>:PAR:MNUM <measNum>](../GP-IB_Command_Finder/Calculate/Parameter.md#MnumSel) which requires the channel and measurement (Tr) number.

Here are other relevant commands for referring to traces, measurements,
channels, and windows:

  * [CALC<cnum>:PAR:CATalog:EXTended?](../GP-IB_Command_Finder/Calculate/Parameter.md#ParCatExtended) \- Catalog the Measurement Names for the specified channel.

  * [CALC<cnum>:PAR:TNUMber?](../GP-IB_Command_Finder/Calculate/Parameter.md#Tnum) \- Returns the Trace Number of the selected trace.

  * [CALC<cnum>:PAR:WNUMber?](../GP-IB_Command_Finder/Calculate/Parameter.md#wnum) \- Returns the window number of the selected trace.

  * [SYSTem:ACTive:CHANnel?](../GP-IB_Command_Finder/System.md#ActiveChannel) \- Returns the number of the active channel. The active channel is the channel number that contains the active measurement.

  * [SYSTem:ACTive:MEAS?](../GP-IB_Command_Finder/System.md#ActMeas) \- Returns the name of the active measurement. As seen on the screen, the Active measurement has the highlighted Tr#.

  * [SYSTem:CHANnels:CATalog?](../GP-IB_Command_Finder/System.md#ChanCat) \- Returns the channel numbers currently in use.

  * [SYSTem:WINDows:CATalog?](../GP-IB_Command_Finder/System.md#winCat) \- Returns the window numbers that are currently being used.

  * [SYSTem:MEAS:CATalog? [chan]](../GP-IB_Command_Finder/System.md#measCat) \- Returns ALL measurement numbers, or optionally measurement numbers from a specified channel.

  * [SYSTem:MEAS<n>:NAME?](../GP-IB_Command_Finder/System.md#MeasName) \- Returns the name of the specified measurement (Tr#) number.

  * [SYSTem:MEAS<n>:TRACe?](../GP-IB_Command_Finder/System.md#MeasTrace) \- Returns the trace number of the specified measurement number.

  * [SYSTem:MEAS<n>:WINDow?](../GP-IB_Command_Finder/System.md#MeasWindow) \- Returns the window number of the specified measurement number.

* * *

