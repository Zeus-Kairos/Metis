# Display Data Setup

The following C# example demonstrates how to read display data, tone-by-tone
data, distortion table data, and how to add/remove display columns in the
distortion table.

[See the Modulation Distortion commands.](../GP-
IB_Command_Finder/SourceModulation.htm)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

using System; using System.Collections.Generic; using System.IO; using
System.Numerics; using Microsoft.VisualStudio.TestTools.UnitTesting; namespace
mod_tests { partial class Vna { [TestMethod] public void Case02() { // Test
Conditions: // \- External source is named as "MXG"; // \- On PNA, file
"D:\Symphony\FR1_100M_64QAM.mdx" is used // \- PNA Port 1 connects to DUT
Input, PNA Port 2 connects to DUT Output; _fmtIO.Cmd("syst:fpr"); // add
traces _fmtIO.Cmd("disp:wind1:stat on"); string[] trNames = new string[] {
"POut2", "PIn1", "MSig2", "MDist2", "MGain21", "MComp21", "PGain21", "S11",
"S21", "LPIn1", "LPOut1", "LPOut2" }; int idx = 1; foreach (var n in trNames)
{ _fmtIO.Cmd(string.Format("calc:cust:def 'ch1_{0}','Modulation
Distortion','{0}'", n)); _fmtIO.Cmd(string.Format("disp:wind1:trac{0}:feed
'ch1_{1}'", idx, n)); ++idx; } // hold sweep _fmtIO.Cmd("sens:swe:mode hold");
// stimulus settings _fmtIO.Cmd("SYST:CONF:EDEV:STAT 'MXG',ON");
_fmtIO.Cmd("sens:DISTortion:MODulate:SOURce 'MXG'");
_fmtIO.Cmd(@"SOURce:MODulation:LOAD 'D:\Symphony\FR1_100M_64QAM.mdx'");
_fmtIO.Cmd("SOURce:MODulation:STATe 1"); // sweep _fmtIO.Cmd("sens:swe:mode
single"); _fmtIO.CmdQry("*OPC?", TimeOuts._2min); // display scale
_fmtIO.Cmd("disp:wind:trac:y:scal:coup:meth wind");
_fmtIO.Cmd("disp:wind1:trac:y:scal:coup on"); _fmtIO.Cmd("disp:wind1:y:auto");
_fmtIO.CmdQry("*OPC?", TimeOuts._1min); string desktopDir =
Environment.GetFolderPath(Environment.SpecialFolder.Desktop); // read display
data { _fmtIO.Cmd("format:border swapped"); _fmtIO.Cmd("format:data real,32");
_fmtIO.Cmd("CALC:MEAS1:DATA:SDAT?"); Complex[] POut2S =
ToComplex(_fmtIO.ReadFloats()); _fmtIO.Cmd("CALC:MEAS1:DATA:FDAT?"); float[]
POut2F = _fmtIO.ReadFloats(); _fmtIO.Cmd("CALC:MEAS1:MATH:MEM"); // POut2,
Data to Memory _fmtIO.Cmd("CALC:MEAS1:DATA:SMEM?"); Complex[] POut2Smem =
ToComplex(_fmtIO.ReadFloats()); _fmtIO.Cmd("CALC:MEAS1:DATA:FMEM?"); float[]
POut2Fmem = _fmtIO.ReadFloats(); SaveColumnsToCSV(Path.Combine(desktopDir,
"mod_data_trace.csv"), new string[] { "POut2 FDAT", "POut2 SDAT", "POut2
FMEM", "POut2 SMEM" }, POut2F, POut2S, POut2Fmem, POut2Smem); } // read tone
by tone data { _fmtIO.Cmd("format:border swapped"); _fmtIO.Cmd("format:data
real,64"); _fmtIO.Cmd("CALC:MEAS:DATA:X:BUFFer? 'POut2'"); double[] freqTones
= _fmtIO.ReadDoubles(); _fmtIO.Cmd("format:data real,32");
_fmtIO.Cmd("CALC:MEAS:DATA:BUFFer? 'POut2'"); Complex[] POut2 =
ToComplex(_fmtIO.ReadFloats()); _fmtIO.Cmd("CALC:MEAS:DATA:BUFFer? 'PIn1'");
Complex[] PIn1 = ToComplex(_fmtIO.ReadFloats());
_fmtIO.Cmd("CALC:MEAS:DATA:BUFFer? 'MSig2'"); Complex[] MSig2 =
ToComplex(_fmtIO.ReadFloats()); _fmtIO.Cmd("CALC:MEAS:DATA:BUFFer? 'MDist2'");
Complex[] MDist2 = ToComplex(_fmtIO.ReadFloats());
_fmtIO.Cmd("CALC:MEAS:DATA:BUFFer? 'MGain21'"); Complex[] MGain21 =
ToComplex(_fmtIO.ReadFloats()); _fmtIO.Cmd("CALC:MEAS:DATA:BUFFer?
'MComp21'"); Complex[] MComp21 = ToComplex(_fmtIO.ReadFloats());
_fmtIO.Cmd("CALC:MEAS:DATA:BUFFer? 'PGain21'"); Complex[] PGain21 =
ToComplex(_fmtIO.ReadFloats()); _fmtIO.Cmd("CALC:MEAS:DATA:BUFFer? 'S11'");
Complex[] S11 = ToComplex(_fmtIO.ReadFloats());
_fmtIO.Cmd("CALC:MEAS:DATA:BUFFer? 'S21'"); Complex[] S21 =
ToComplex(_fmtIO.ReadFloats()); _fmtIO.Cmd("CALC:MEAS:DATA:BUFFer? 'LPIn1'");
Complex[] LPIn1 = ToComplex(_fmtIO.ReadFloats());
_fmtIO.Cmd("CALC:MEAS:DATA:BUFFer? 'LPOut1'"); Complex[] LPOut1 =
ToComplex(_fmtIO.ReadFloats()); _fmtIO.Cmd("CALC:MEAS:DATA:BUFFer? 'LPOut2'");
Complex[] LPOut2 = ToComplex(_fmtIO.ReadFloats());
SaveColumnsToCSV(Path.Combine(desktopDir, "mod_data_tone_by_tone.csv"), new
string[] { "Freq", "POut2", "PIn1", "MSig2", "MDist2", "MGain21", "MComp21",
"PGain21", "S11", "S21", "LPIn1", "LPOut1", "LPOut2" }, freqTones,
ToLogMag(POut2), ToLogMag(PIn1), ToLogMag(MSig2), ToLogMag(MDist2),
ToLogMag(MGain21), ToLogMag(MComp21), ToLogMag(PGain21), ToLogMag(S11),
ToLogMag(S21), ToLogMag(LPIn1), ToLogMag(LPOut1), ToLogMag(LPOut2)); } //
setup distortion table display _fmtIO.Cmd("disp:wind:tabl dist"); string
strColVis = _fmtIO.CmdQry("sens:dist:tabl:disp:cat?"); string[] cols =
strColVis.Split(new char[] { ',' }, StringSplitOptions.RemoveEmptyEntries);
_fmtIO.Cmd(string.Format("sens:dist:tabl:disp:del '{0}'", cols[0]));
_fmtIO.Cmd(string.Format("sens:dist:tabl:disp:feed '{0}'", cols[0])); // get
table data int bandCnt =
int.Parse(_fmtIO.CmdQry("sens:DISTortion:MEASure:BAND:COUNt?")); string rowCat
= _fmtIO.CmdQry("sens:dist:tabl:cat?"); { string colCat =
_fmtIO.CmdQry("sens:dist:tabl:data:cat?"); string[] paramNames = new string[]
{ "EVM DistEq41 dBc", "EVM DistEq41 %" }; object[] col1 = new object[1 +
bandCnt]; col1[0] = paramNames[0]; object[] col2 = new object[1 + bandCnt];
col2[0] = paramNames[0]; for (int bandId = 1; bandId <= bandCnt; ++bandId) {
col1[bandId] =
float.Parse(_fmtIO.CmdQry(string.Format("sens:dist:tabl:data:val? {0},'{1}'",
bandId, paramNames[0]))); col2[bandId] =
float.Parse(_fmtIO.CmdQry(string.Format("sens:dist:tabl:data:val? {0},'{1}'",
bandId, paramNames[1]))); } SaveColumnsToCSV(Path.Combine(desktopDir,
"mod_evm.csv"), null, col1, col2); } // all ACPEVM parameters
_fmtIO.Cmd("sens:DISTortion:MEASure:BAND:INIT"); _fmtIO.Cmd("sens:swe:mode
single"); _fmtIO.CmdQry("*OPC?", TimeOuts._2min); { string colCat =
_fmtIO.CmdQry("sens:dist:tabl:data:cat?"); string[] paramNames =
colCat.Split(new char[] { ',' }, StringSplitOptions.RemoveEmptyEntries);
float[] col1 = new float[paramNames.Length]; for (int i = 0; i <
paramNames.Length; ++i) { col1[i] =
float.Parse(_fmtIO.CmdQry(string.Format("sens:dist:tabl:data:val? {0},'{1}'",
1, paramNames[i]))); } SaveColumnsToCSV(Path.Combine(desktopDir,
"mod_ACPEVM.csv"), null, paramNames, col1); } // all NPR parameters
_fmtIO.Cmd("sens:DISTortion:MEASure:BAND:INIT");
_fmtIO.Cmd("sens:DISTortion:MEASure:BAND:TYPE NPR"); _fmtIO.Cmd("sens:swe:mode
single"); _fmtIO.CmdQry("*OPC?", TimeOuts._2min); { string colCat =
_fmtIO.CmdQry("sens:dist:tabl:data:cat?"); string[] paramNames =
colCat.Split(new char[] { ',' }, StringSplitOptions.RemoveEmptyEntries);
float[] col1 = new float[paramNames.Length]; for (int i = 0; i <
paramNames.Length; ++i) { col1[i] =
float.Parse(_fmtIO.CmdQry(string.Format("sens:dist:tabl:data:val? {0},'{1}'",
1, paramNames[i]))); } SaveColumnsToCSV(Path.Combine(desktopDir,
"mod_NPR.csv"), null, paramNames, col1); } } } }  
---

