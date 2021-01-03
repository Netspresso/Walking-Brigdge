import apex
from apex.construct import Point3D, Point2D

# Environmental setup
apex.setScriptUnitSystem(unitSystemName=r'''m-kg-s-N''')
applicationSettingsGeometry = apex.setting.ApplicationSettingsGeometry()
applicationSettingsGeometry.createGeometryInNewPart = apex.setting.CreateGeometryInNewPart.CurrentPart
applicationSettingsGeometry.geometryTessellationIsWatertight = False
applicationSettingsGeometry.geometryEdgeTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
applicationSettingsGeometry.geometryFaceTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
apex.setting.setApplicationSettingsGeometry(
    applicationSettingsGeometry=applicationSettingsGeometry)
model_1 = apex.currentModel()

# Steel material creation
material_1 = apex.catalog.createMaterial(
    name="Steel",
    description="Steel with typical properties",
    color=[255, 77, 64])

material_1.update(elasticModulus=210000000000., )  # Mouł Younga

material_1.update(poissonRatio=0.3, )  # Wspołczynnik Poisson'a

material_1.update(density=8750., )  # Gęstość objętościowa

#
# Macro recording stopped on Oct 21, 2020 at 16:41:22
#
