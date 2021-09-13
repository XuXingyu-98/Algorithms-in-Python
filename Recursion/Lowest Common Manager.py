def getLowestCommonManager(topManager, reportOne, reportTwo):
    return getOrgInfo(topManager, reportOne, reportTwo).lowestCommonManager

def getOrgInfo(manager, reportOne, reportTwo):
    numReports = 0
    for directReport in manager.directReports:
        orgInfo = getOrgInfo(directReport, reportOne, reportTwo)
        if orgInfo.lowestCommonManager is not None:
            return orgInfo
        numReports += orgInfo.lowestCommonManager
    if manager == reportOne or manager == reportTwo:
        numReports += 1
    lowestCommonManager = manager if numReports == 2 else None
    return OrgInfo(lowestCommonManager, numReports)


class OrgInfo:
    def __init__(self, lowestCommonManager, numReports):
        self.lowestCommonManager = lowestCommonManager
        self.numReports = numReports



class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
