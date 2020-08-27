import apex
from apex.construct import Point3D, Point2D
from apex.geometry import createPointXYZ, createCurve3DNurb
import math

apex.setScriptUnitSystem(unitSystemName=r'''mm-kg-s-N''')
applicationSettingsGeometry = apex.setting.ApplicationSettingsGeometry()
applicationSettingsGeometry.createGeometryInNewPart = apex.setting.CreateGeometryInNewPart.CurrentPart
applicationSettingsGeometry.geometryTessellationIsWatertight = False
applicationSettingsGeometry.geometryEdgeTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
applicationSettingsGeometry.geometryFaceTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
apex.setting.setApplicationSettingsGeometry(
    applicationSettingsGeometry=applicationSettingsGeometry)
model_1 = apex.currentModel()


class Elipsa:
    '''Class defining elipses'''
    def __init__(self, a, b, Height, distance, ListPoint):
        t = 0
        while t <= 2 * math.pi:
            self.x = a * math.cos(t) + distance
            self.y = b * math.sin(t)
            self.z = Height
            ListPoint.append(
                createPointXYZ(x=self.x, y=self.y, z=self.z).asPoint())
            t += 0.2


def linspace(low, up, leng):
    """function creating a linear space from [low] to [up] using [leng] number of elements"""
    list = []
    step = (up - low) / float(leng)
    for i in range(leng):
        list.append(low)
        low = low + step
    return list


ptList = []
n_of_curve = 2

for i in range(0, n_of_curve):
    ptList.append([])

Elipsa(1.5, 0.75, 0, 10.5, ptList[0])
Elipsa(1.75 / 2, 0.75, 10, 9.875, ptList[1])

for elipsa in range(0, len(ptList)):
    Lista = ptList[elipsa]
    n = len(Lista)
    deg = 1
    m = n + deg + 1
    controlPoints = Lista
    knotPoints = linspace(0, 1, m)
    createCurve3DNurb(controlPoints, knotPoints, deg).asCurve()

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_1 = part_1.getCurve(name="Curve 20")
_target.extend(curve_1.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_2 = part_1.getCurve(name="Curve 19")
_target.extend(curve_2.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name='',
    target=_list,
    loftClampingMethod=apex.geometry.LoftClampingMethod.No,
    clampStartProfile=True,
    clampEndProfile=True,
    stitch=True)
