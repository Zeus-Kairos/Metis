# Triggering the Analyzer using SCPI

* * *

To understand how to trigger the analyzer using SCPI, it is very important to
understand the [trigger model](../../S1_Settings/TrigModel.md). Here is a
very simple explanation. These three separate functions control triggering:

  1. [Trigger:Source](../GP-IB_Command_Finder/Trigger_SCPI.md#tss) \- Where the trigger signals originate:

     * Internal Continuous

     * Internal Manual (Single)

     * External - a trigger source that is connected to the rear panel.

  2. [Trigger:Scope](../GP-IB_Command_Finder/Trigger_SCPI.md#tssc) \- what gets triggered:

     * Global - each signal triggers all channels in turn.

     * Channel - each signal triggers ONE channel.

  3. Channel settings ([Sense<ch>:Sweep:Mode](../GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssm)) How many triggers will each channel accept before going into hold.

     * HOLD - channel will not trigger.

     * CONTinuous - channel triggers indefinitely.

     * GROups - channel accepts the number of triggers specified with the last [SENS:SWE:GRO:COUN](../GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssgc) <num>.

     * SINGle - channel accepts ONE trigger, then goes to HOLD.

     * Point trigger [SENS1:SWE:TRIG:POINt](../GP-IB_Command_Finder/Sense/Sweep_SCPI.md#sstp)

When controlling the VNA using SCPI, a SINGLE trigger is used to ensure that a
complete sweep is taken. This example demonstrates how to Single trigger the
VNA using the following two methods:

  * Simplest Triggering

  *     * This method uses the default Trigger Source = Internal to send a stream of trigger signals.

    * The channel is configured to ACCEPT only a single trigger signal, then HOLD ([Sense<ch>:Sweep:Mode SINGle](../GP-IB_Command_Finder/Sense/Sweep_SCPI.md#ssm)). This is the ONLY required command.

    * This method can also be used when an External trigger source sends a continuous stream of trigger signals.

  * Advanced Triggering

  *     * This method SENDS a single trigger from the Source, which can be from either Internal (using INIT:IMM) or External triggering.

    * Each channel is configured to accept an unlimited number of triggers. This method is the only way to perform point triggering.

    * When you require some channels to accept continuous triggers and other channels to accept single triggers, see [INIT:IMM Advanced](../GP-IB_Command_Finder/Initiate.md#Advanced) to learn how.

The SCPI commands in this example are sent over a COM interface using the
SCPIStringParser object. You do NOT need a GPIB connection to run this
example.

This VBScript (*.vbs) program can be run as a macro in the analyzer. To do
this, copy the following code into a text editor file such as Notepad and save
it on the analyzer hard drive as Trigger.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm)

Measurement setup example: This section of code can be used at the start of
both methods. It sets up:

  * S11 traces on two channels

  * 10 data points

  * Sweep time of 2 seconds - this is slow enough to allow us to watch as each trace is triggered.

Dim app Dim scpi ' Create / Get the VNA application. Set app =
CreateObject("AgilentPNA835x.Application") Set scpi = app.ScpiStringParser
'============================================ 'Setup the VNA 'Preset the
analyzer scpi.Execute ("SYST:FPReset") ' Create and turn on window/channel 1
scpi.Execute ("DISPlay:WINDow1:STATE ON") 'Define a measurement name,
parameter scpi.Execute ("CALCulate1:PARameter:DEFine:EXT 'MyMeas1',S11")
'Associate ("FEED") the measurement name ('MyMeas') to WINDow (1) scpi.Execute
("DISPlay:WINDow1:TRACe1:FEED 'MyMeas1'") ' Create and turn on window/channel
2 scpi.Execute ("DISPlay:WINDow2:STATE ON") 'Define a measurement name,
parameter scpi.Execute ("CALCulate2:PARameter:DEFine:EXT 'MyMeas2',S11")
'Associate ("FEED") the measurement name ('MyMeas') to WINDow (2) scpi.Execute
("DISPlay:WINDow2:TRACe2:FEED 'MyMeas2'") 'Set slow sweep so we can see
scpi.Execute ("SENS1:SWE:TIME 2") scpi.Execute ("SENS2:SWE:TIME 2") 'set
number of points to 10 scpi.Execute ("SENS1:SWE:POIN 10") scpi.Execute
("SENS2:SWE:POIN 10") '============================================ ' Put both
channels in Hold scpi.Execute ("SENS1:SWE:MODE HOLD") scpi.Execute
("SENS2:SWE:MODE HOLD") '================================ 'Pick Single Send or
Single Accept resp=Msgbox ("Single Send? - Click No for Single Accept", 4,
"PNA Trigger Demo") If resp=6 Then SingleSend() Else SingleAccept() End If  
---  
  
Simple Triggering The following example sends a continuous stream of trigger
signals and each VNA channel is set to ACCEPT only a signal trigger signal,
then HOLD.

  * This example can be used to configure External triggering where the trigger source sends a continuous stream of trigger signals. Configure the type of trigger signal that the VNA responds to using the [CONTrol:SIGNal](../GP-IB_Command_Finder/Control.md#signal) command. The command in this example sets the VNA to respond to HIGH TTL signals at the rear-panel BNC1 trigger IN connector. This command also automatically sets Trigger Source to External Trigger.

  * The [TRIG SCOPE](../GP-IB_Command_Finder/Trigger_SCPI.md#tssc) (Global or Channel) setting is NOT necessary with a continuous stream of trigger signals. The example program directly controls when each channel is triggered.

  * Point triggering can NOT be used with a continuous stream of trigger signals because in point triggering the channel will accept as many triggers as necessary to complete ONE full sweep. Use the [single SEND](Triggering_the_PNA_using_SCPI.md#SingleSend) example for point triggering.

Sub SingleAccept() 'VNA sends continuous trigger signals scpi.Execute
("TRIG:SOUR IMMediate") 'Uncomment the following to set External triggering
'scpi.Execute ("CONT:SIGN BNC1,TILHIGH") AcceptOne() End Sub Sub AcceptOne()
'The following command makes the channel immediately sweep '*OPC? allows the
measurement to complete before the controller sends another command
scpi.Execute ("SENS1:SWE:MODE SINGle;*OPC?") ' You could do something to ch2
here before sweeping it scpi.Execute ("SENS2:SWE:MODE SINGle;*OPC?")
resp=Msgbox ("Another trigger?", 1, "PNA Trigger Demo") If resp=1 Then
AcceptOne() End If End Sub  
---  
  
Advanced Trigger This example section performs Single Send triggering. Here,
single triggering is accomplished by SENDING one trigger signal from the
Trigger source and each channel is setup to accept unlimited trigger signals.
See the [INIT:IMM](../GP-IB_Command_Finder/Initiate.md#immed) command for
more details.

  * Using this method, it is possible to change [Trigger:Scope](../GP-IB_Command_Finder/Trigger_SCPI.md#tssc) to Global or Channel. Set trigger scope to channel if there is some code to execute between channel measurements. Similarly, this method can be used to set [Point triggering](../GP-IB_Command_Finder/Sense/Sweep_SCPI.md#sstp). Use this method if there is some code to execute between data point measurements.

  * In addition, this method can also be used to perform External triggering if the external trigger source is capable of SENDING single triggers. See the [CONTrol:SIGNal](../GP-IB_Command_Finder/Control.md#signal) command to set the type of signal to which the VNA will respond.

  * If the external source can only send a continuous stream of trigger signals, then the [Single Accept](Triggering_the_PNA_using_SCPI.md#singleAccept) section must be used.

Sub SingleSend() 'Set Source Internal - Manual Triggering scpi.Execute
("TRIG:SOUR MANual") 'If using an External trigger source that is capable of
'sending SINGLE trigger signals, then uncomment the following. 'This command
automatically sets trigger source to External 'scpi.Execute ("CONT:SIGN
BNC1,TILHIGH") 'Setup Trigger Scope 'WHAT gets triggered 'Pick one using
comments 'Set Channel triggering 'scpi.Execute ("TRIG:SCOPe CURRent") 'Set
Global triggering (Default) scpi.Execute ("TRIG:SCOPe ALL") 'Set Channel
Settings 'The channels respond to UNLIMITED trigger signals (Default)
scpi.Execute ("SENS1:SWE:MODE CONTinuous") scpi.Execute ("SENS2:SWE:MODE
CONTinuous") 'To do Point trigger on one or more channels, uncomment the
following. 'Point trigger automatically sets Trig:Scope to Current/Channel
'scpi.Execute ("SENS1:SWE:TRIG:POINt ON") 'scpi.Execute ("SENS2:SWE:TRIG:POINt
ON") IntTrig() End Sub Sub IntTrig() 'If External triggering, replace this Sub
with code 'to single trigger the External Trig Source Dim resp '*OPC? allows
the measurement to complete before the controller sends another command
scpi.Execute ("INITiate:IMMediate;*OPC?") resp=Msgbox ("Another trigger?", 1,
"PNA Trigger Demo") If resp=1 Then IntTrig() End If End Sub  
---  
  

* * *

