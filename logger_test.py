import logger

l = Logger(".", "TestLog", True)
l.Log("Test output.", Flags.CRIT)
l.Crit("Test output.")
l.close()
