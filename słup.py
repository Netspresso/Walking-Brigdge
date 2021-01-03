import apex
from apex.construct import Point3D, Point2D
from apex.geometry import createPointXYZ, createCurve3DNurb
import math
from curves import Elipsa, Elipsa_2, linspace, odstep_slupa, ap

apex.setScriptUnitSystem(unitSystemName=r'''m-kg-s-N''')
applicationSettingsGeometry = apex.setting.ApplicationSettingsGeometry()
applicationSettingsGeometry.createGeometryInNewPart = apex.setting.CreateGeometryInNewPart.CurrentPart
applicationSettingsGeometry.geometryTessellationIsWatertight = False
applicationSettingsGeometry.geometryEdgeTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
applicationSettingsGeometry.geometryFaceTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
apex.setting.setApplicationSettingsGeometry(
    applicationSettingsGeometry=applicationSettingsGeometry)
model_1 = apex.currentModel()

ptList = []
n_of_curve = 2
slow_step = math.pi / 24.0
v = 2.0 / math.pi

for i in range(0, n_of_curve):
    ptList.append([])

Elipsa(ap(2 * math.pi, slow_step, odstep_slupa), -1, ptList[0])
Elipsa_2(ap(2 * math.pi, slow_step, odstep_slupa), v * 4 * math.pi + 1,
         ptList[1])

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
part_1 = apex.getPart(pathName="gen/Part 1")
curve_1 = part_1.getCurve(name="Curve 20")
_target.extend(curve_1.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="gen/Part 1")
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
