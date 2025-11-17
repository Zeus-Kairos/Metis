# Create fixturing function (impedance conversion and port matching)

* * *

This example programs below create single-ended port impedance conversion
function and add network circuit by loading/recall the file from C drive.

The first program uses [Fsimulator Draft](../GP-
IB_Command_Finder/Calculate/FSimulatorDraft.htm) and [Fsimulator
Active](../GP-IB_Command_Finder/Calculate/FSimulatorActive.htm) SCPI commands
while the second program uses legacy SCPI commands. Learn about [Using Fixture
Simulator](../Using_Fixture_Simulator.htm).

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

Example program with [Fsimulator Draft](../GP-
IB_Command_Finder/Calculate/FSimulatorDraft.htm) and [Fsimulator
Active](../GP-IB_Command_Finder/Calculate/FSimulatorActive.htm) SCPI commands

*CLS *OPC? SYST:PRES calc:fsim:draft:discard calc1:fsim:draft:zcon:send:port1:state 1 calc1:fsim:draft:zcon:send:port1:state? calc1:fsim:draft:zcon:send:port1:SCAL 50 calc1:fsim:draft:zcon:send:port1:SCAL? calc1:fsim:draft:zcon:send:port2:state 1 calc1:fsim:draft:zcon:send:port2:state? calc1:fsim:draft:zcon:send:port2:SCAL 100 calc1:fsim:draft:zcon:send:port2:SCAL? calc1:fsim:draft:zcon:send:port3:state 1 calc1:fsim:draft:zcon:send:port3:state? calc1:fsim:draft:zcon:send:port3:SCAL 100 calc1:fsim:draft:zcon:send:port3:SCAL? calc1:fsim:draft:zcon:send:port4:state 1 calc1:fsim:draft:zcon:send:port4:state? calc1:fsim:draft:zcon:send:port4:SCAL 50 calc1:fsim:draft:zcon:send:port4:SCAL? calc:fsim:draft:circ:reset calc:fsim:draft:circ:next? calc:fsim:draft:circ1:add FILE,2 calc:fsim:draft:circ1:vna:ports 1 CALC:FSIM:DRAFt:CIRCuit1:EMBED:TYPE embed calc:fsim:draft:circ1:file "C:\Keysight\development\bheyburn\scripts\Python_SCPI\s2pFiles\CSET_FIXTURE_plus_5.00.s2p" calc:fsim:draft:circ1:state 1 calc:fsim:draft:circ:next? calc:fsim:draft:circ2:add FILE,2 calc:fsim:draft:circ2:vna:ports 3 CALC:FSIM:DRAFt:CIRCuit2:EMBED:TYPE embed calc:fsim:draft:circ2:file "C:\Keysight\development\bheyburn\scripts\Python_SCPI\s2pFiles\CSET_FIXTURE_minus_3.00.s2p" calc:fsim:draft:circ2:state 1 CALC:FSIM:DRAFt:SECTion:CIRCuit:ENABle on calc:fsim:apply calc1:fsim:stat ON calc1:fsim:stat?  
---  
  
Example program with legacy SCPI commands

*CLS *OPC? SYST:PRES calc1:fsim:send:oord? calc1:fsim:send:zcon:stat on calc1:fsim:send:zcon:stat? calc1:fsim:send:zcon:port1:z0 50 calc1:fsim:send:zcon:port1:z0? calc1:fsim:send:zcon:port2:z0 100 calc1:fsim:send:zcon:port2:z0? calc1:fsim:send:zcon:port3:z0 100 calc1:fsim:send:zcon:port3:z0? calc1:fsim:send:zcon:port4:z0 50 calc1:fsim:send:zcon:port4:z0? calc1:fsim:send:pmc:stat on calc1:fsim:send:pmc:stat? calc1:fsim:send:pmc:port1:type USER calc1:fsim:send:pmc:port1:type? calc1:fsim:send:pmc:port1:user:fil "C:\Keysight\development\bheyburn\scripts\Python_SCPI\s2pFiles\CSET_FIXTURE_plus_5.00.s2p" calc1:fsim:send:pmc:port1:user:fil? calc1:fsim:send:pmc:port3:type USER calc1:fsim:send:pmc:port3:type? calc1:fsim:send:pmc:port3:user:fil "C:\Keysight\development\bheyburn\scripts\Python_SCPI\s2pFiles\CSET_FIXTURE_minus_3.00.s2p" calc1:fsim:send:pmc:port3:user:fil? calc1:fsim:stat ON calc1:fsim:stat?  
---

