#pragma once
#define interface struct

interface Switches {
	virtual void StartEngine() = 0;
	virtual void ShutDownEngine() = 0;
	virtual void TurnRadioOn() = 0;
	virtual void TurnRadioOff() = 0;
	virtual void TurnCameraOn() = 0;
	virtual void TurnCameraOff() = 0;
};