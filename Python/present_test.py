from gaia.cu9.ari.gaiaorbit.script import EventScriptingInterface

gs = EventScriptingInterface.instance()
gs.waitForInput();

def present_planet(name,description,angle): 
	gs.goToObject(name, angle,20)
	gs.setHeadlineMessage(name)
	gs.setSubheadMessage(description)
	gs.sleep(3)
	gs.clearAllMessages()



gs.goToObject("Sol", 30,30)
gs.setHeadlineMessage("Welcome to the Gaia planetarium")
gs.sleep(3)
present_planet("Earth","""Earth, our world !""",-15)
present_planet("Saturn","""The second biggest planet our solar system.""",15)
present_planet("Uranus","""Uranus is a giant planet.""",15)
present_planet("Venus","""Venus is one of the four terrestrial planets of the Solar System.""",15)

gs.setHeadlineMessage("Gezellig !")
