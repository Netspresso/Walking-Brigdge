# coding: utf-8
# Macro created by MSC Apex 2020 PRE - Version CLR:722475
# Macro created on Aug 28, 2020 at 10:22:56
#
# Macro Name = powierzchnie przypon
#
# Macro Description =
#
# Macro Hot Key =
#
# Initialize environment for macro execution
#

import apex
from apex.construct import Point3D, Point2D

apex.setScriptUnitSystem(unitSystemName=r'''mm-kg-s-N''')
applicationSettingsGeometry = apex.setting.ApplicationSettingsGeometry()
applicationSettingsGeometry.createGeometryInNewPart = apex.setting.CreateGeometryInNewPart.CurrentPart
applicationSettingsGeometry.geometryTessellationIsWatertight = False
applicationSettingsGeometry.geometryEdgeTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
applicationSettingsGeometry.geometryFaceTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
apex.setting.setApplicationSettingsGeometry(
    applicationSettingsGeometry=applicationSettingsGeometry)
model_1 = apex.currentModel()

#
# Start of recorded operations
#
for i in range(21, 38):
    _target = apex.EntityCollection()
    part_1 = apex.getPart(pathName="Model/Part 1")
    curve_1 = part_1.getCurve(name="Curve {}".format(i))
    _target.extend(curve_1.getEdges())
    result = apex.geometry.fillerSurface(target=_target)

#
# Macro recording stopped on Aug 28, 2020 at 10:23:58
#
