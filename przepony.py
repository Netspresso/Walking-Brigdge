import apex
from apex.construct import Point3D, Point2D
from apex.geometry import createPointXYZ, createCurve3DNurb
import math
from config import Curve as C
from curves import a, b, linspace, odstep_slupa

apex.setScriptUnitSystem(unitSystemName=r'''mm-kg-s-N''')
applicationSettingsGeometry = apex.setting.ApplicationSettingsGeometry()
applicationSettingsGeometry.createGeometryInNewPart = apex.setting.CreateGeometryInNewPart.CurrentPart
applicationSettingsGeometry.geometryTessellationIsWatertight = False
applicationSettingsGeometry.geometryEdgeTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
applicationSettingsGeometry.geometryFaceTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
apex.setting.setApplicationSettingsGeometry(
    applicationSettingsGeometry=applicationSettingsGeometry)
model_1 = apex.currentModel()


class Curves:
    # Class defining curves A

    def __init__(self, a, b, Velocity, Distance, ListPoint):
        t = 0
        count = len(a)
        z = range(0, count)
        for i in z:
            self.x = a[i] * math.cos(t) - (5 * t) / (4 * math.pi) + 15
            self.y = b[i] * math.sin(t)
            self.z = Velocity * t + Distance
            ListPoint.append(
                createPointXYZ(x=self.x, y=self.y, z=self.z).asPoint())
            t += math.pi / 4.0


# functions
def ap(tmax, Step, component):
    """Inner radius(f) (from center to the beam)"""
    radius = []

    t = 0
    while t <= tmax:
        radius.append((-5 / (4 * math.pi)) * t + 10 - component(t))
        t += Step
    return radius


def b_p(tmax, Step, component):
    """Inner radius(f) (from center to the beam)"""
    radius = []

    t = 0
    while t <= tmax:
        radius.append((-5 / (4 * math.pi)) * t + 7.5 - component(t))
        t += Step
    return radius


# Lists of point for all curves
ptList_p = []

n_of_curve = 21

for i in range(0, n_of_curve):
    ptList_p.append([])
# Do przeróbki:

# Do przeróbki:
Curves(ap(C.range_a, C.slow_step, odstep_slupa),
       b_p(C.range_b, C.slow_step, odstep_slupa), C.v, C.pr_height - 0.4,
       ptList_p[0])
# //
Curves(a(C.range_a, C.slow_step, C.plinth),
       b(C.range_b, C.slow_step, C.plinth), C.v, C.ibeam_height, ptList_p[1])
Curves(a(C.range_a, C.slow_step, C.spacing + C.plinth),
       b(C.range_b, C.slow_step, C.spacing + C.plinth), C.v, C.ibeam_height,
       ptList_p[2])
Curves(a(C.range_a, C.slow_step, 2.0 * C.spacing + C.plinth),
       b(C.range_b, C.slow_step, 2.0 * C.spacing + C.plinth), C.v,
       C.ibeam_height, ptList_p[3])
Curves(a(C.range_a, C.slow_step, 3.0 * C.spacing + C.plinth),
       b(C.range_b, C.slow_step, 3.0 * C.spacing + C.plinth), C.v,
       C.ibeam_height, ptList_p[4])
Curves(a(C.range_a, C.slow_step, C.beam_distance + C.plinth),
       b(C.range_b, C.slow_step, C.beam_distance + C.plinth), C.v,
       C.obeam_height, ptList_p[5])
Curves(a(C.range_a, C.slow_step, C.beam_distance + C.plinth + C.spacing),
       b(C.range_b, C.slow_step, C.beam_distance + C.plinth + C.spacing), C.v,
       C.obeam_height, ptList_p[6])
Curves(a(C.range_a, C.slow_step, C.beam_distance + C.plinth + 2.0 * C.spacing),
       b(C.range_b, C.slow_step, C.beam_distance + C.plinth + 2.0 * C.spacing),
       C.v, C.obeam_height, ptList_p[7])
Curves(a(C.range_a, C.slow_step, C.beam_distance + C.plinth + 3.0 * C.spacing),
       b(C.range_b, C.slow_step, C.beam_distance + C.plinth + 3.0 * C.spacing),
       C.v, C.obeam_height, ptList_p[8])
Curves(
    a(C.range_a, C.slow_step,
      C.beam_distance + 2.0 * C.plinth + 3.0 * C.spacing + C.br_width),
    b(C.range_b, C.slow_step,
      C.beam_distance + 2.0 * C.plinth + 3.0 * C.spacing + C.br_width), C.v,
    C.pr_height, ptList_p[9])
Curves(
    a(C.range_a, C.slow_step,
      C.beam_distance + 2.0 * C.plinth + 3.0 * C.spacing + C.br_width),
    b(C.range_b, C.slow_step,
      C.beam_distance + 2.0 * C.plinth + 3.0 * C.spacing + C.br_width), C.v, 0,
    ptList_p[10])
Curves(
    a(C.range_a, C.slow_step,
      C.beam_distance + 2.0 * C.plinth + 3.0 * C.spacing),
    b(C.range_b, C.slow_step,
      C.beam_distance + 2.0 * C.plinth + 3.0 * C.spacing), C.v, 0,
    ptList_p[11])
Curves(a(C.range_a, C.slow_step, C.beam_distance + C.plinth + 2.0 * C.spacing),
       b(C.range_b, C.slow_step, C.beam_distance + C.plinth + 2.0 * C.spacing),
       C.v, 0, ptList_p[12])
Curves(a(C.range_a, C.slow_step, C.beam_distance + C.plinth + C.spacing),
       b(C.range_b, C.slow_step, C.beam_distance + C.plinth + C.spacing), C.v,
       0, ptList_p[13])
Curves(a(C.range_a, C.slow_step, C.beam_distance),
       b(C.range_b, C.slow_step, C.beam_distance), C.v, 0, ptList_p[14])
Curves(a(C.range_a, C.slow_step, 3.0 * C.spacing + 2.0 * C.plinth),
       b(C.range_b, C.slow_step, 3.0 * C.spacing + 2.0 * C.plinth), C.v, 0,
       ptList_p[15])
Curves(a(C.range_a, C.slow_step, 2.0 * C.spacing + C.plinth),
       b(C.range_b, C.slow_step, 2.0 * C.spacing + C.plinth), C.v, 0,
       ptList_p[16])
Curves(a(C.range_a, C.slow_step, C.spacing + C.plinth),
       b(C.range_b, C.slow_step, C.spacing + C.plinth), C.v, 0, ptList_p[17])
Curves(a(C.range_a, C.slow_step, 0), b(C.range_b, C.slow_step, 0), C.v, 0,
       ptList_p[18])
Curves(a(C.range_a, C.slow_step, -C.br_width),
       b(C.range_b, C.slow_step, -C.br_width), C.v, 0, ptList_p[19])
Curves(ap(C.range_a, C.slow_step, odstep_slupa),
       b_p(C.range_b, C.slow_step, odstep_slupa), C.v, 0, ptList_p[20])

size = len(ptList_p[10])
new_ptList = []

for nr_przepony in range(0, size):
    new_ptList.append([])
    for list in ptList_p:
        new_ptList[nr_przepony].append(list[nr_przepony])

for Curve in range(0, len(new_ptList)):
    Lista = new_ptList[Curve]
    n = len(Lista)
    deg = 1
    m = n + deg + 1
    controlPoints = Lista
    knotPoints = linspace(0, 1, m)
    createCurve3DNurb(controlPoints, knotPoints, deg).asCurve()

for i in range(22, 39):
    _target = apex.EntityCollection()
    part_1 = apex.getPart(pathName="Model/Part 1")
    curve_1 = part_1.getCurve(name="Curve {}".format(i))
    _target.extend(curve_1.getEdges())
    result = apex.geometry.fillerSurface(target=_target)