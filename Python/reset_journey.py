from gaia.cu9.ari.gaiaorbit.script import EventScriptingInterface

gs = EventScriptingInterface.instance()
gs.waitForInput()

gs.setHeadlineMessage("Press any key to reset the journey.")

def reset_journey(lat, long, target, desc): 
	gs.pointAtSkyCoordinate(lat, long)
	gs.setHeadlineMessage(target)
	gs.setSubheadMessage(desc)
	gs.sleep(1)
	
reset_journey(92.879, -26.703, "End Of Universe", "Let's go back to the starting point")

gs.sleep(1)

gs.clearAllMessages()