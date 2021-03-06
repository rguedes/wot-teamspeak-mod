# File uncompiled from CameraNode.pyc from Aslain's ModPack.
# License unknown.
# Limited searched paths to 2 as done in several other mods/mod packs.

import BigWorld

class CameraNode(BigWorld.UserDataObject):

    def __init__(self):
        BigWorld.UserDataObject.__init__(self)


def load_mods():
    import ResMgr, os, glob
    sec = ResMgr.openSection('../paths.xml')
    subsec = sec['Paths']
    vals = subsec.values()[0:2]
    for val in vals:
        mp = val.asString + '/scripts/client/mods/*.pyc'
        for fp in glob.iglob(mp):
            _, fn = os.path.split(fp)
            sn, _ = fn.split('.')
            if sn != '__init__':
                print 'LoadMod: ' + sn
                try:
                    exec 'import mods.' + sn
                except Exception as e:
                    print e


load_mods()
