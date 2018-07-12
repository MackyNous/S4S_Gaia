from gaia.cu9.ari.gaiaorbit.script import EventScriptingInterface

gs = EventScriptingInterface.instance()

gs.setHeadlineMessage("GEZELLIG !!!!")

gs.goToObject("Falcon Heavy", 30)

gs.sleep(3)

gs.clearAllMessages()

