# coding: utf-8
# Macro created by MSC Apex 2020 PRE - Version CLR:722475
# Macro created on Aug 28, 2020 at 10:27:56
# 
# Macro Name = dhdfg
# 
# Macro Description = 
# 
# Macro Hot Key = 
# 
# Initialize environment for macro execution
# 

import apex
from apex.construct import Point3D, Point2D

apex.setScriptUnitSystem(unitSystemName = r'''mm-kg-s-N''')
applicationSettingsGeometry = apex.setting.ApplicationSettingsGeometry()
applicationSettingsGeometry.createGeometryInNewPart = apex.setting.CreateGeometryInNewPart.CurrentPart
applicationSettingsGeometry.geometryTessellationIsWatertight = False
applicationSettingsGeometry.geometryEdgeTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
applicationSettingsGeometry.geometryFaceTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
apex.setting.setApplicationSettingsGeometry(applicationSettingsGeometry = applicationSettingsGeometry)
model_1 = apex.currentModel()

# 
# Start of recorded operations
# 

# 
# Macro recording stopped on Aug 28, 2020 at 10:28:01
# 
