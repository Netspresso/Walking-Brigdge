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

# Pierwsza płaszczyzna
_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_1 = part_1.getCurve( name = "Curve 38")
_target.extend( curve_1.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_2 = part_1.getCurve( name = "Curve 21" )
_target.extend( curve_2.getEdges() )
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name = '',
    target = _list,
    loftClampingMethod = apex.geometry.LoftClampingMethod.No,
    clampStartProfile = True,
    clampEndProfile = True,
    stitch = False
)
# druga płaszczyzna
_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_2 = part_1.getCurve( name = "Curve 21" )
_target.extend( curve_2.getEdges() )
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_3 = part_1.getCurve( name = "Curve 23" )
_target.extend( curve_3.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name = '',
    target = _list,
    loftClampingMethod = apex.geometry.LoftClampingMethod.No,
    clampStartProfile = True,
    clampEndProfile = True,
    stitch = False
)

# trzecia płaszczyzna
_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_4 = part_1.getCurve( name = "Curve 25" )
_target.extend( curve_4.getEdges() )
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_3 = part_1.getCurve( name = "Curve 23" )
_target.extend( curve_3.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name = '',
    target = _list,
    loftClampingMethod = apex.geometry.LoftClampingMethod.No,
    clampStartProfile = True,
    clampEndProfile = True,
    stitch = False
)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_5 = part_1.getCurve( name = "Curve 27" )
_target.extend( curve_5.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_4 = part_1.getCurve( name = "Curve 25" )
_target.extend( curve_4.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name = '',
    target = _list,
    loftClampingMethod = apex.geometry.LoftClampingMethod.No,
    clampStartProfile = True,
    clampEndProfile = True,
    stitch = False
)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_6 = part_1.getCurve( name = "Curve 29" )
_target.extend( curve_6.getEdges() )
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_5 = part_1.getCurve( name = "Curve 27" )
_target.extend( curve_5.getEdges() )
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name = '',
    target = _list,
    loftClampingMethod = apex.geometry.LoftClampingMethod.No,
    clampStartProfile = True,
    clampEndProfile = True,
    stitch = False
)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_7 = part_1.getCurve( name = "Curve 31" )
_target.extend( curve_7.getEdges() )
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_6 = part_1.getCurve( name = "Curve 29" )
_target.extend( curve_6.getEdges() )
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name = '',
    target = _list,
    loftClampingMethod = apex.geometry.LoftClampingMethod.No,
    clampStartProfile = True,
    clampEndProfile = True,
    stitch = False
)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_8 = part_1.getCurve( name = "Curve 33" )
_target.extend( curve_8.getEdges() )
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_7 = part_1.getCurve( name = "Curve 31" )
_target.extend( curve_7.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name = '',
    target = _list,
    loftClampingMethod = apex.geometry.LoftClampingMethod.No,
    clampStartProfile = True,
    clampEndProfile = True,
    stitch = False
)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_9 = part_1.getCurve( name = "Curve 35" )
_target.extend( curve_9.getEdges() )
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_8 = part_1.getCurve( name = "Curve 33" )
_target.extend( curve_8.getEdges() )
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name = '',
    target = _list,
    loftClampingMethod = apex.geometry.LoftClampingMethod.No,
    clampStartProfile = True,
    clampEndProfile = True,
    stitch = False
)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_9 = part_1.getCurve( name = "Curve 35" )
_target.extend( curve_9.getEdges() )
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_10 = part_1.getCurve( name = "Curve 37" )
_target.extend( curve_10.getEdges() )
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name = '',
    target = _list,
    loftClampingMethod = apex.geometry.LoftClampingMethod.No,
    clampStartProfile = True,
    clampEndProfile = True,
    stitch = False
)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_2 = part_1.getCurve( name = "Curve 21" )
_target.extend( curve_2.getEdges() )
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_11 = part_1.getCurve( name = "Curve 22" )
_target.extend( curve_11.getEdges() )
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name = '',
    target = _list,
    loftClampingMethod = apex.geometry.LoftClampingMethod.No,
    clampStartProfile = True,
    clampEndProfile = True,
    stitch = False
)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_3 = part_1.getCurve( name = "Curve 23" )
_target.extend( curve_3.getEdges() )
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_12 = part_1.getCurve( name = "Curve 24" )
_target.extend( curve_12.getEdges() )
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name = '',
    target = _list,
    loftClampingMethod = apex.geometry.LoftClampingMethod.No,
    clampStartProfile = True,
    clampEndProfile = True,
    stitch = False
)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_4 = part_1.getCurve( name = "Curve 25" )
_target.extend( curve_4.getEdges() )
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_13 = part_1.getCurve( name = "Curve 26" )
_target.extend( curve_13.getEdges() )
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name = '',
    target = _list,
    loftClampingMethod = apex.geometry.LoftClampingMethod.No,
    clampStartProfile = True,
    clampEndProfile = True,
    stitch = False
)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_5 = part_1.getCurve( name = "Curve 27" )
_target.extend( curve_5.getEdges() )
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_14 = part_1.getCurve( name = "Curve 28" )
_target.extend( curve_14.getEdges() )
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name = '',
    target = _list,
    loftClampingMethod = apex.geometry.LoftClampingMethod.No,
    clampStartProfile = True,
    clampEndProfile = True,
    stitch = False
)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_6 = part_1.getCurve( name = "Curve 29" )
_target.extend( curve_6.getEdges() )
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_15 = part_1.getCurve( name = "Curve 30" )
_target.extend( curve_15.getEdges() )
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name = '',
    target = _list,
    loftClampingMethod = apex.geometry.LoftClampingMethod.No,
    clampStartProfile = True,
    clampEndProfile = True,
    stitch = False
)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_7 = part_1.getCurve( name = "Curve 31" )
_target.extend( curve_7.getEdges() )
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_16 = part_1.getCurve( name = "Curve 32" )
_target.extend( curve_16.getEdges() )
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name = '',
    target = _list,
    loftClampingMethod = apex.geometry.LoftClampingMethod.No,
    clampStartProfile = True,
    clampEndProfile = True,
    stitch = False
)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_8 = part_1.getCurve( name = "Curve 33" )
_target.extend( curve_8.getEdges() )
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_17 = part_1.getCurve( name = "Curve 34" )
_target.extend( curve_17.getEdges() )
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name = '',
    target = _list,
    loftClampingMethod = apex.geometry.LoftClampingMethod.No,
    clampStartProfile = True,
    clampEndProfile = True,
    stitch = False
)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_9 = part_1.getCurve( name = "Curve 35" )
_target.extend( curve_9.getEdges() )
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_18 = part_1.getCurve( name = "Curve 36" )
_target.extend( curve_18.getEdges() )
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name = '',
    target = _list,
    loftClampingMethod = apex.geometry.LoftClampingMethod.No,
    clampStartProfile = True,
    clampEndProfile = True,
    stitch = False
)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_11 = part_1.getCurve( name = "Curve 22" )
_target.extend( curve_11.getEdges() )
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_12 = part_1.getCurve( name = "Curve 24" )
_target.extend( curve_12.getEdges() )
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name = '',
    target = _list,
    loftClampingMethod = apex.geometry.LoftClampingMethod.No,
    clampStartProfile = True,
    clampEndProfile = True,
    stitch = False
)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_12 = part_1.getCurve( name = "Curve 24" )
_target.extend( curve_12.getEdges() )
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_13 = part_1.getCurve( name = "Curve 26" )
_target.extend( curve_13.getEdges() )
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name = '',
    target = _list,
    loftClampingMethod = apex.geometry.LoftClampingMethod.No,
    clampStartProfile = True,
    clampEndProfile = True,
    stitch = False
)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_13 = part_1.getCurve( name = "Curve 26" )
_target.extend( curve_13.getEdges() )
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_14 = part_1.getCurve( name = "Curve 28" )
_target.extend( curve_14.getEdges() )
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name = '',
    target = _list,
    loftClampingMethod = apex.geometry.LoftClampingMethod.No,
    clampStartProfile = True,
    clampEndProfile = True,
    stitch = False
)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_15 = part_1.getCurve( name = "Curve 30" )
_target.extend( curve_15.getEdges() )
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_16 = part_1.getCurve( name = "Curve 32" )
_target.extend( curve_16.getEdges() )
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name = '',
    target = _list,
    loftClampingMethod = apex.geometry.LoftClampingMethod.No,
    clampStartProfile = True,
    clampEndProfile = True,
    stitch = False
)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_16 = part_1.getCurve( name = "Curve 32" )
_target.extend( curve_16.getEdges() )
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_17 = part_1.getCurve( name = "Curve 34" )
_target.extend( curve_17.getEdges() )
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name = '',
    target = _list,
    loftClampingMethod = apex.geometry.LoftClampingMethod.No,
    clampStartProfile = True,
    clampEndProfile = True,
    stitch = False
)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_17 = part_1.getCurve( name = "Curve 34" )
_target.extend( curve_17.getEdges() )
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = "Model/Part 1" )
curve_18 = part_1.getCurve( name = "Curve 36" )
_target.extend( curve_18.getEdges() )
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name = '',
    target = _list,
    loftClampingMethod = apex.geometry.LoftClampingMethod.No,
    clampStartProfile = True,
    clampEndProfile = True,
    stitch = False
)
