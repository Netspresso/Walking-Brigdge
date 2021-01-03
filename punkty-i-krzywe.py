import apex
from apex.construct import Point3D, Point2D
from apex.geometry import createPointXYZ, createCurve3DNurb
import math
from config import Curve as C
from curves import a, b, linspace, Curves_down, Straight_line, Curves_up
# import numpy as np

apex.setScriptUnitSystem(unitSystemName=r'''m-kg-s-N''')
applicationSettingsGeometry = apex.setting.ApplicationSettingsGeometry()
applicationSettingsGeometry.createGeometryInNewPart = apex.setting.CreateGeometryInNewPart.CurrentPart
applicationSettingsGeometry.geometryTessellationIsWatertight = False
applicationSettingsGeometry.geometryEdgeTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
applicationSettingsGeometry.geometryFaceTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
apex.setting.setApplicationSettingsGeometry(
    applicationSettingsGeometry=applicationSettingsGeometry)
model_1 = apex.currentModel()
'''Here I began script'''
''' Classes '''

# Lists of points for all Curves
ptList = []
n_of_curve = 18  # count of curves

# Loop which adds empty lists to ptList (now we have list which contain 18 empty lists)
for i in range(0, n_of_curve):
    ptList.append([])

# Generating points
Curves_up(a(C.range_a, C.step, 0), b(C.range_b, C.step, 0), C.v, 0, ptList[0])
Straight_line(0, 0, ptList[0])
Curves_down(a(C.range_a, C.step, C.plinth), b(C.range_b, C.step, C.plinth),
            C.ibeam_height, ptList[1])
Straight_line(C.plinth, C.ibeam_height, ptList[1])
Curves_up(a(C.range_a, C.step, C.plinth + C.spacing),
          b(C.range_b, C.step, C.plinth + C.spacing), C.v, 0, ptList[2])
Straight_line(C.plinth + C.spacing, 0, ptList[2])
Curves_down(a(C.range_a, C.step, C.plinth + C.spacing),
            b(C.range_b, C.step, C.plinth + C.spacing), C.ibeam_height,
            ptList[3])
Straight_line(C.plinth + C.spacing, C.ibeam_height, ptList[3])
Curves_up(a(C.range_a, C.step, 2.0 * C.spacing + C.plinth),
          b(C.range_b, C.step, 2.0 * C.spacing + C.plinth), C.v, 0, ptList[4])
Straight_line(2.0 * C.spacing + C.plinth, 0, ptList[4])
Curves_down(a(C.range_a, C.step, 2.0 * C.spacing + C.plinth),
            b(C.range_b, C.step, 2.0 * C.spacing + C.plinth), C.ibeam_height,
            ptList[5])
Straight_line(2.0 * C.spacing + C.plinth, C.ibeam_height, ptList[5])
Curves_up(a(C.range_a, C.step, 3.0 * C.spacing + 2.0 * C.plinth),
          b(C.range_b, C.step, 3.0 * C.spacing + 2.0 * C.plinth), C.v, 0,
          ptList[6])
Straight_line(3.0 * C.spacing + 2.0 * C.plinth, 0, ptList[6])
Curves_down(a(C.range_a, C.step, 3.0 * C.spacing + C.plinth),
            b(C.range_b, C.step, 3.0 * C.spacing + C.plinth), C.ibeam_height,
            ptList[7])
Straight_line(3.0 * C.spacing + C.plinth, C.ibeam_height, ptList[7])
Curves_up(a(C.range_a, C.step, C.beam_distance),
          b(C.range_b, C.step, C.beam_distance), C.v, 0, ptList[8])
Straight_line(C.beam_distance, 0, ptList[8])
Curves_down(a(C.range_a, C.step, C.beam_distance + C.plinth),
            b(C.range_b, C.step, C.beam_distance + C.plinth), C.obeam_height,
            ptList[9])
Straight_line(C.beam_distance + C.plinth, C.obeam_height, ptList[9])
Curves_up(a(C.range_a, C.step, C.beam_distance + C.plinth + C.spacing),
          b(C.range_b, C.step, C.beam_distance + C.plinth + C.spacing), C.v, 0,
          ptList[10])
Straight_line(C.beam_distance + C.plinth + C.spacing, 0, ptList[10])
Curves_down(a(C.range_a, C.step, C.beam_distance + C.plinth + C.spacing),
            b(C.range_b, C.step, C.beam_distance + C.plinth + C.spacing),
            C.obeam_height, ptList[11])
Straight_line(C.beam_distance + C.plinth + C.spacing, C.obeam_height,
              ptList[11])
Curves_up(a(C.range_a, C.step, C.beam_distance + C.plinth + 2.0 * C.spacing),
          b(C.range_b, C.step, C.beam_distance + C.plinth + 2.0 * C.spacing),
          C.v, 0, ptList[12])
Straight_line(C.beam_distance + C.plinth + 2.0 * C.spacing, 0, ptList[12])
Curves_down(a(C.range_a, C.step, C.beam_distance + C.plinth + 2.0 * C.spacing),
            b(C.range_b, C.step, C.beam_distance + C.plinth + 2.0 * C.spacing),
            C.obeam_height, ptList[13])
Straight_line(C.beam_distance + C.plinth + 2.0 * C.spacing, C.obeam_height,
              ptList[13])
Curves_up(
    a(C.range_a, C.step, C.beam_distance + 2.0 * C.plinth + 3.0 * C.spacing),
    b(C.range_b, C.step, C.beam_distance + 2.0 * C.plinth + 3.0 * C.spacing),
    C.v, 0, ptList[14])
Straight_line(C.beam_distance + 2.0 * C.plinth + 3.0 * C.spacing, 0,
              ptList[14])
Curves_down(a(C.range_a, C.step, C.beam_distance + C.plinth + 3.0 * C.spacing),
            b(C.range_b, C.step, C.beam_distance + C.plinth + 3.0 * C.spacing),
            C.obeam_height, ptList[15])
Straight_line(C.beam_distance + C.plinth + 3.0 * C.spacing, C.obeam_height,
              ptList[15])
Curves_up(a(C.range_a, C.step, C.beam_distance + C.beam_width + C.br_width),
          b(C.range_b, C.step, C.beam_distance + C.beam_width + C.br_width),
          C.v, C.plate_height, ptList[16])
Straight_line(C.beam_distance + C.beam_width + C.br_width, C.plate_height,
              ptList[16])
Curves_up(a(C.range_a, C.step, -C.br_width), b(C.range_b, C.step, -C.br_width),
          C.v, C.plate_height, ptList[17])
Straight_line(-C.br_width, C.plate_height, ptList[17])

#  Creating curves through the points
for Curve in range(0, len(ptList)):
    controlPoints = ptList[Curve]  # Lista punktów kontrolnych
    n = len(controlPoints)
    deg = 1  # Stopień krzywej, decyduje o tym, ile punktów kontrolnych wpływa na jej kształt.
    m = n + deg + 1
    knotPoints = linspace(0, 1, m)
    createCurve3DNurb(controlPoints, knotPoints, deg).asCurve()