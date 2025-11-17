# FOM Examples

* * *

All three VBScript examples in this topic create a FOM measurement with the
following attributes:

  * Sweep the Source (input) from 1 GHz to 2 GHz

  * Sweep the Receivers (output) from 2 GHz to 3 GHz

  * You provide an LO at 1 GHz

[Learn more about Frequency Offset
Mode](../../FreqOffset/Frequency_Offset_Mode.htm)

These programs can be run as a macro in the VNA. To do this, copy the code
into a text editor file such as Notepad and save on the VNA hard drive as
FOM.vbs. [Learn how to setup and run the macro.](../Using_Macros.md)

The following example will run on any VNA model with FOM (opt S93080A).
However, these commands have no provisions for internal second source. It uses
commands introduced before 'enhanced FOM' was released for the A.07.10
release.

set app = CreateObject("Agilentpna835x.application") set chan =
app.ActiveChannel chan.startFrequency = 1e9 chan.StopFrequency = 2e9 ' set the
receiver frequencies to be 2e9->3e9 chan.FrequencyOffsetFrequency = 1e9
chan.FrequencyOffsetState = 1  
---  
  
The following example can be run ONLY on a VNA with revision A.07.10 or later
and has FOM (opt S93080A). It uses new FOM commands. [See FOMRange
object.](../COM_Reference/Objects/FOMRange_Object.htm)

set app = CreateObject("Agilentpna835x.application") set chan =
app.ActiveChannel chan.startFrequency = 1e9 chan.StopFrequency = 2e9 ' set the
receiver frequencies to be 2e9->3e9 chan.fom("Receivers").Offset = 1e9
chan.fom.State = 1  
---  
  
The following example can be run ONLY on a VNA with a second internal source,
has revision A.07.10 or later, and has FOM (opt S93080A). It uses the internal
2nd source for the fixed LO frequency.

set app = CreateObject("Agilentpna835x.application") set chan =
app.ActiveChannel chan.startFrequency = 1e9 chan.StopFrequency = 2e9 ' set the
receiver frequencies to be 2e9->3e9 chan.fom("Receivers").Offset = 1e9
chan.fom("Source2").Coupled = 0 chan.fom("Source2").StartFrequency = 1e9
chan.fom("Source2").StopFrequency = 1e9 ' turn off port coupling
chan.coupleports = 0 ' set LO to 10 dBm chan.TestPortPower(3) = 10 'Turn ON
port 3, our LO signal on our 2 source PNA chan.SourcePortMode(3) = 1
chan.fom.State = 1  
---  
  
* * *

