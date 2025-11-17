# Display Update

#### How to set Display Update  
  
---  
Using Hardkey/SoftTab/Softkey  
  
  1. Press Display > Display Settings > Display Update (Turns ON display update).
  2. press Display > Display Settings > click left side small button of Display Update (Turns OFF display update).

  
[![](../assets/images/SeeProg.gif)](../Programming/CF_Display_Commands.md)  
  
Notes:

  1. Turn ON/OFF the Display update will result on the [Status Bar](../Front_Panel/XScreen.md#Status).

  2. Update State ON/OFF is part of the save/recall state.

  3. Softkey(s) exist for update state ON/OFF and immediate update.

  4. Disabling the display update will yield the most significant performance improvements. The performance improvement (due to disabling updates) for a single channel and window state seems negligible. However, with a large number of channels, windows and traces, it should make more of a difference (but disabling the display update will provide more performance improvement). For example, Performance Oddities, the following is looking at the INDEX line (Handler I/O) for a 1.0 GHz to 1.2 GHz with 201 point sweep (otherwise Preset condition apply). When high, the analyzer is sweeping. There is 20 ms of dead time between many of sweeps.

* * *

