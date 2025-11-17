# Undo/Redo Settings

* * *

If you make an incorrect setting, you can quickly recover by selecting Undo.
If you then incorrectly Undo a setting, you can Redo the undone setting.

  * Undo and Redo applies ONLY to [selected settings](Undo.md).

  * The Undo stack remembers 16 levels of Undo-able settings.

### How to Undo or Redo a setting

Tips:

  * Click or touch the Undo and Redo Icons:

|  ![](../assets/images/UndoRedoIcons.gif)  
---  
Undo |  Redo  
  
  * With a mouse, right-click on the Softkeys or on the Entry toolbar.

  * With a keyboard:

  *     * Undo....Ctrl+Z

    * Redo....Ctrl+Y

  
Using Hardkey/SoftTab/Softkey |  Using a mouse  
  
  1. Press Undo > Main.
  2. Click Undo or Redo.

|

  1. Click Undo and Redo Icons on Active Entry or Softkey Toolbar.

  
SCPI and COM programming and Undo/Redo:

  * There are NO Programming commands to invoke Undo/Redo
  * Programing commands are NOT Undo-able.
  * The Undo stack is cleared when programming commands are sent to the VNA.

  
  
### Return To Task

To return to the previous task, press Undo > Main > Return To Task.

### Clear Undo History

To clear the Undo stack, press Undo > Main > Clear Undo History.

### Undo and Security

  * Undo/Redo is disabled with High and Extra security levels. [Learn more](../System/Frequency_Blanking.md).

  * State files that are saved for Undo/Redo purposes (for example: Preset) are deleted when any of the following occur:

  *     * The Security level is changed

    * The Network Analyzer App is started or closed.

### Selected Undo-able settings

You can Undo or Redo the following settings:

Note: There are several settings that are NOT Undo-able. Because of this, when
you attempt to Undo a long sequence of operations, it is unlikely that the
original state can be recreated exactly.

  * [Preset](Preset_the_Analyzer.md)

  * [File Recall](../S5_Output/SaveRecall.md)

  * Frequency Settings

  *     * For Standard Class, Gain Compression, and NF: Start, Stop, Center, Span, CW

    * For SMC, VMC: Mixer Setup dialog Apply

    * For Swept IMD: Freq softkeys, setup dialog Apply 

    * IM Spectrum: Freq softkeys, setup dialog Apply

    * Noise Figure: Freq softkeys, setup dialog Apply

    * GCX, IMDX, NFX: setup dialog Apply

  * [Turn off Marker](../S4_Collect/Markers.md) and [Marker All OFF](../S4_Collect/Markers.md#MarkerDiag)

  * [Number of Points](DPoints.md)

  * [Power Level](Power_Level.md) \- most applications and S-parameters

  * [Add or Change Measurement Class](Measurement_Classes.md)

  * [Turn OFF Channel](../S0_Start/Traces_Channels_and_Windows.md#ManagingChan)

  * [Close Window](../S0_Start/Traces_Channels_and_Windows.md)

  * [New Channel , new Window, and new Trace](../S0_Start/Traces_Channels_and_Windows.md).

  * Delete Trace

  * Window Tile

  * Change Layout (1x, 2x, 3x, 4x)

  * Move Trace, Drag Trace

  * Zoom XY, Zoom Out Full

  * Autoscale All, Autoscale

  * Scale, Reference Level, Reference Position

  * Scale Coupling dialog

  * Electrical Delay

  * Phase Offset

  * Measurement Setups dialog

  * Format

  * Sweep Type

  * Data->Memory

  * Single Marker Searches (Max, Min, Target, Peak )

  * Multi-marker Searches (Bandwidth, Power Saturation, Normal Operating Pt)

  * Change a Markers stimulus value: softkeys, dialog or drag

  * Change cell in Segment Table

  * Mechanical Settings dialog

* * *

* * *

