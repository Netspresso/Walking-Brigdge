import apex
from apex.construct import Point3D, Point2D

apex.setScriptUnitSystem(unitSystemName=r'''m-kg-s-N''')
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

material_1 = apex.catalog.createMaterial(name="Material 1",
                                         description="",
                                         color=[64, 254, 250])

material_1.update(name="Stal", )

material_1.update(elasticModulus=2100000000., )

material_1.update(poissonRatio=0.3, )

material_1.update(density=8750., )

#
# Macro recording stopped on Oct 21, 2020 at 18:29:16
#
