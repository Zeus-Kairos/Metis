# Create fixturing function ( port impedance conversion and port extension)

* * *

This example programs below create port extension and port impedance
conversion function.

The first program uses [Fsimulator Draft](../GP-
IB_Command_Finder/Calculate/FSimulatorDraft.htm) and [Fsimulator
Active](../GP-IB_Command_Finder/Calculate/FSimulatorActive.htm) SCPI commands
while the second program uses legacy SCPI commands. Learn about [Using Fixture
Simulator](../Using_Fixture_Simulator.htm).

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

Example program with [Fsimulator Draft](../GP-
IB_Command_Finder/Calculate/FSimulatorDraft.htm) and [Fsimulator
Active](../GP-IB_Command_Finder/Calculate/FSimulatorActive.htm) SCPI commands

SYST:PRES *OPC? #calc1:fsim:send:oord 3,2,1,0  #The command above indicates
that we need to create the blocks in this order: #Arb Impendance, Port
Matching, 2-Port Deembed, Port Extensions #Special note: It turns out that the
arb impedance doesn't matter where it's at in the chain, the new fixture
generator #takes care of it appropriately, so it doesn't matter (and no need
to have a command to move it) (it is in a different processing chain) #for as
an example, we'll show you how to move it: calc1:fsim:stat ON calc1:fsim:stat?
calc:fsim:draft:discard CALC:FSIM:DRAFt:SECTion:ZCONversion:ENABle on
calc1:fsim:draft:zcon:send:port1:state on
calc1:fsim:draft:zcon:send:port1:state? calc1:fsim:draft:zcon:send:port1:scal
75 calc1:fsim:draft:zcon:send:port1:scal?
CALC:FSIM:DRAFt:EXTension:PORT1:DELay 1E-10
CALC:FSIM:DRAFt:EXTension:PORT1:DELay? CALC:FSIM:DRAFt:EXTension:PORT1:STATe
on CALC:FSIM:DRAFt:EXTension:PORT1:STATe? CALC:FSIM:DRAFt:EXTension:PORT1:END
CALC:FSIM:DRAFt:SECTion:EXTension:ENABle ON calc:fsim:apply  
---  
  
Example program with legacy SCPI commands

SYST:PRES *OPC? calc1:fsim:send:oord? calc1:fsim:send:oord 3,2,1,0
calc1:fsim:stat ON calc1:fsim:stat? sens1:corr:ext:port1:time 1E-10
sens1:corr:ext:port1:time? sens1:corr:ext ON sens1:corr:ext?
calc1:fsim:send:zcon:stat on calc1:fsim:send:zcon:stat?
calc1:fsim:send:zcon:port1:z0 75  
---

