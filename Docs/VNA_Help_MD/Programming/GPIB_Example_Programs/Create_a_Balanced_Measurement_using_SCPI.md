# Create a Balanced Measurement using SCPI

* * *

This example program does the following:

  * creates several Balanced measurements in separate windows

  * generates markers

  * calculates statistics

  * sets limit lines and queries results

  * queries a measurement to determine if we have a balanced parameter and what type it is.

Note: By their nature, balanced measurements are extremely sensitive to phase
differences between the two RF paths that make up the balanced port,
especially at higher frequencies. A good calibration (not performed in this
example) is critical to achieving good balanced measurement results.

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You do NOT need a GPIB connection to run this example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as Balanced.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

Dim app Dim scpi ' Create / Get the VNA application. Set app = CreateObject("AgilentPNA835x.Application") Set scpi = app.ScpiStringParser ' A comment scpi.Parse("SYST:FPRESET") ' This example uses DUT topology Bal-Bal - ' a DUT with a balanced input and balanced output. ' ' Port mapping for our DUT: ' logical port 1 = physical ports 1 and 4 ' logical port 2 = physical ports 2 and 3 ' The default is: ' logical port 1 = physical ports 1 and 2 ' logical port 2 = physical ports 3 and 4 ' ' logical 1 logical 2 ' ___________ ' 1 ------| |------ 2 + ' | DUT | ' 4 ------|___________|------ 3 - ' Turn on Four windows scpi.Parse("DISP:WIND1:STATe ON") scpi.Parse("DISP:WIND2:STATe ON") scpi.Parse("DISP:WIND3:STATe ON") scpi.Parse("DISP:WIND4:STATe ON") ' Create a trace called "sdd21", and for that trace turn on the balanced ' transformation and set the balanced transformation to BBAL SDD21. scpi.Parse("CALC:PAR:DEF:EXT ""sdd21"",S11") scpi.Parse("CALC:PAR:SEL ""sdd21""") scpi.Parse("CALC:FSIM:BAL:PAR:STATe ON") scpi.Parse("CALC:FSIM:BAL:PAR:BBAL:DEF SDD21") ' Feed the sdd21 trace to window 1, trace 1 scpi.Parse("DISP:WIND1:TRAC1:FEED ""sdd21""") ' Similarly create 3 more balanced transmission/conversion parameters ' Create Scd21 scpi.Parse("CALC:PAR:DEF:EXT ""scd21"",S11") scpi.Parse("CALC:PAR:SEL ""scd21""") scpi.Parse("CALC:FSIM:BAL:PAR:STATe ON") scpi.Parse("CALC:FSIM:BAL:PAR:BBAL:DEF SCD21") scpi.Parse("DISP:WIND1:TRAC2:FEED ""scd21""") ' Create Sdc21 scpi.Parse("CALC:PAR:DEF:EXT ""sdc21"",S11") scpi.Parse("CALC:PAR:SEL ""sdc21""") scpi.Parse("CALC:FSIM:BAL:PAR:STATe ON") scpi.Parse("CALC:FSIM:BAL:PAR:BBAL:DEF SDC21") scpi.Parse("DISP:WIND1:TRAC3:FEED ""sdc21""") ' Create Scc21 scpi.Parse("CALC:PAR:DEF:EXT ""scc21"",S11") scpi.Parse("CALC:PAR:SEL ""scc21""") scpi.Parse("CALC:FSIM:BAL:PAR:STATe ON") scpi.Parse("CALC:FSIM:BAL:PAR:BBAL:DEF SCC21") scpi.Parse("DISP:WIND1:TRAC4:FEED ""scc21""") ' Now create logical port 1 reflection parameters, and place them in window 2 scpi.Parse("CALC:PAR:DEF:EXT ""sdd11"",S11") scpi.Parse("CALC:PAR:SEL ""sdd11""") scpi.Parse("CALC:FSIM:BAL:PAR:STATe ON") scpi.Parse("CALC:FSIM:BAL:PAR:BBAL:DEF SDD11") ' Feed the sdd11 trace to window 2, trace 1 scpi.Parse("DISP:WIND2:TRAC1:FEED ""sdd11""") ' Similarly create 3 more balanced reflection/conversion parameters scpi.Parse("CALC:PAR:DEF:EXT ""scd11"",S11") scpi.Parse("CALC:PAR:SEL ""scd11""") scpi.Parse("CALC:FSIM:BAL:PAR:STATe ON") scpi.Parse("CALC:FSIM:BAL:PAR:BBAL:DEF SCD11") scpi.Parse("DISP:WIND2:TRAC2:FEED ""scd11""") scpi.Parse("CALC:PAR:DEF:EXT ""sdc11"",S11") scpi.Parse("CALC:PAR:SEL ""sdc11""") scpi.Parse("CALC:FSIM:BAL:PAR:STATe ON") scpi.Parse("CALC:FSIM:BAL:PAR:BBAL:DEF SDC11") scpi.Parse("DISP:WIND2:TRAC3:FEED ""sdc11""") scpi.Parse("CALC:PAR:DEF:EXT ""scc11"",S11") scpi.Parse("CALC:PAR:SEL ""scc11""") scpi.Parse("CALC:FSIM:BAL:PAR:STATe ON") scpi.Parse("CALC:FSIM:BAL:PAR:BBAL:DEF SCC11") scpi.Parse("DISP:WIND2:TRAC4:FEED ""scc11""") ' Now create reverse transmission parameters, and place them in window 3 scpi.Parse("CALC:PAR:DEF:EXT ""sdd12"",S11") scpi.Parse("CALC:PAR:SEL ""sdd12""") scpi.Parse("CALC:FSIM:BAL:PAR:STATe ON") scpi.Parse("CALC:FSIM:BAL:PAR:BBAL:DEF SDD12") ' Feed the sdd11 trace to window 3, trace 1 scpi.Parse("DISP:WIND3:TRAC1:FEED ""sdd12""") ' Similarly create 3 more balanced reverse transmission/conversion parameters scpi.Parse("CALC:PAR:DEF:EXT ""scd12"",S11") scpi.Parse("CALC:PAR:SEL ""scd12""") scpi.Parse("CALC:FSIM:BAL:PAR:STATe ON") scpi.Parse("CALC:FSIM:BAL:PAR:BBAL:DEF SCD12") scpi.Parse("DISP:WIND3:TRAC2:FEED ""scd12""") scpi.Parse("CALC:PAR:DEF:EXT ""sdc12"",S11") scpi.Parse("CALC:PAR:SEL ""sdc12""") scpi.Parse("CALC:FSIM:BAL:PAR:STATe ON") scpi.Parse("CALC:FSIM:BAL:PAR:BBAL:DEF SDC12") scpi.Parse("DISP:WIND3:TRAC3:FEED ""sdc12""") scpi.Parse("CALC:PAR:DEF:EXT ""scc12"",S11") scpi.Parse("CALC:PAR:SEL ""scc12""") scpi.Parse("CALC:FSIM:BAL:PAR:STATe ON") scpi.Parse("CALC:FSIM:BAL:PAR:BBAL:DEF SCC12") scpi.Parse("DISP:WIND3:TRAC4:FEED ""scc12""") ' Now create reverse reflection parameters, and place them in window 4 scpi.Parse("CALC:PAR:DEF:EXT ""sdd22"",S11") scpi.Parse("CALC:PAR:SEL ""sdd22""") scpi.Parse("CALC:FSIM:BAL:PAR:STATe ON") scpi.Parse("CALC:FSIM:BAL:PAR:BBAL:DEF SDD22") ' Feed the sdd11 trace to window 3, trace 1 scpi.Parse("DISP:WIND4:TRAC1:FEED ""sdd22""") ' Similarly create 3 more balanced reverse reflection parameters scpi.Parse("CALC:PAR:DEF:EXT ""scd22"",S11") scpi.Parse("CALC:PAR:SEL ""scd22""") scpi.Parse("CALC:FSIM:BAL:PAR:STATe ON") scpi.Parse("CALC:FSIM:BAL:PAR:BBAL:DEF SCD22") scpi.Parse("DISP:WIND4:TRAC2:FEED ""scd22""") scpi.Parse("CALC:PAR:DEF:EXT ""sdc22"",S11") scpi.Parse("CALC:PAR:SEL ""sdc22""") scpi.Parse("CALC:FSIM:BAL:PAR:STATe ON") scpi.Parse("CALC:FSIM:BAL:PAR:BBAL:DEF SDC22") scpi.Parse("DISP:WIND4:TRAC3:FEED ""sdc22""") scpi.Parse("CALC:PAR:DEF:EXT ""scc22"",S11") scpi.Parse("CALC:PAR:SEL ""scc22""") scpi.Parse("CALC:FSIM:BAL:PAR:STATe ON") scpi.Parse("CALC:FSIM:BAL:PAR:BBAL:DEF SCC22") scpi.Parse("DISP:WIND4:TRAC4:FEED ""scc22""") scpi.Parse("CALC:FSIM:BAL:DEVice BBALanced") scpi.Parse("CALC:FSIM:BAL:TOPology:BBAL:PPORts 1,4,2,3") ' Set up stimulus scpi.Parse("SENS:SWE:POINts 801") scpi.Parse("SENS:FREQ:STARt 10e6") scpi.Parse("SENS:FREQ:STOP 1e9") ' Here we demonstrate how to determine if we have ' a balanced parameter and what type it is. ' Read back one parameter to verify its type scpi.Parse("CALC:PAR:SEL ""sdd21""") ' Is this a balanced parameter? isbal = scpi.Parse("CALC:FSIM:BAL:PAR?") ' Which topology/device is set? device = scpi.Parse("CALC:FSIM:BAL:DEV?") device = Left( device, Len(device)-1 ) ' strip off newline ' Which parameter are we measuring within that topology? balparam = scpi.Parse("CALC:FSIM:BAL:PAR:" & device & ":DEF?") balparam = Left( balparam, Len(balparam)-1 ) ' strip off newline If isbal Then WScript.Echo "Balanced Parameter: " & balparam & " in topology: " & device & "." Else WScript.Echo "Parameter not balanced." End If  
---  
  
* * *

