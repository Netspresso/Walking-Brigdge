'''
class curvesE:
    #Class defining curves E

    def __init__(self, a, b, Distance, ListPoint):

        t = 0
        count = len(a)
        z = range(0, count)
        for i in z:
            curvesE.x = -a[i] * math.cos(t) + (5 * t) / (4 * math.pi) - 15
            curvesE.y = -b[i] * math.sin(t)
            if t <= math.pi / 8.0:
                curvesE.z = 9.6 / math.pi * t - 1.0 + Distance
            else:
                curvesE.z = 2.0 / math.pi * t - 0.05 + Distance
            ListPoint.append(
                createPointXYZ(x=curvesE.x, y=curvesE.y,
                               z=curvesE.z).asPoint())
            t += 1
'''
'''
class curvesD:
    def __init__(self, component, Distance, ListPoint):
        x = -9.375
        while x <= 8.0:
            curvesD.x = x
            curvesD.y = -1.875 - component
            curvesD.z = 9 + Distance
            ListPoint.append(
                createPointXYZ(x=curvesD.x, y=curvesD.y,
                               z=curvesD.z).asPoint())
'''
'''
class curvesC:
    def __init__(self, a, b, Velocity, Distance, ListPoint):
        t = 0
        count = len(a)
        z = range(0, count)
        for i in z:
            curvesC.x = -a[i] * math.cos(t) + (5 * t) / (4 * math.pi) - 15
            curvesC.y = -b[i] * math.sin(t)
            curvesC.z = Velocity * t + Distance
            ListPoint.append(
                createPointXYZ(x=curvesC.x, y=curvesC.y,
                               z=curvesC.z).asPoint())
            t += 1
            '''
'''
CurvesC(a(C.range_a, C.step, 0), b(C.range_b, C.step, 0), v, 0, ptList[18])
CurvesE(a(C.range_a, C.step, C.plinth), b(C.range_b, C.step, C.plinth), C.ibeam_height,
        ptList[19])
CurvesC(a(C.range_a, C.step, C.plinth + C.spacing), b(C.range_b, C.step, C.plinth + C.spacing),
        v, 0, ptList[20])
CurvesE(a(C.range_a, C.step, C.plinth + C.spacing), b(C.range_b, C.step, C.plinth + C.spacing),
        C.ibeam_height, ptList[21])
CurvesC(a(C.range_a, C.step, 2.0 * C.spacing + C.plinth),
        b(C.range_b, C.step, 2.0 * C.spacing + C.plinth), v, 0, ptList[22])
CurvesE(a(C.range_a, C.step, 2.0 * C.spacing + C.plinth),
        b(C.range_b, C.step, 2.0 * C.spacing + C.plinth), C.ibeam_height, ptList[23])
CurvesC(a(C.range_a, C.step, 3.0 * C.spacing + 2.0 * C.plinth),
        b(C.range_b, C.step, 3.0 * C.spacing + 2.0 * C.plinth), v, 0, ptList[24])
CurvesE(a(C.range_a, C.step, 3.0 * C.spacing + C.plinth),
        b(C.range_b, C.step, 3.0 * C.spacing + C.plinth), C.ibeam_height, ptList[25])
CurvesC(a(C.range_a, C.step, C.beam_distance), b(C.range_b, C.step, C.beam_distance), v, 0,
        ptList[26])
CurvesE(a(C.range_a, C.step, C.beam_distance + C.plinth),
        b(C.range_b, C.step, C.beam_distance + C.plinth), C.obeam_height, ptList[27])
CurvesC(a(C.range_a, C.step, C.beam_distance + C.plinth + C.spacing),
        b(C.range_b, C.step, C.beam_distance + C.plinth + C.spacing), v, 0, ptList[28])
CurvesE(a(C.range_a, C.step, C.beam_distance + C.plinth + C.spacing),
        b(C.range_b, C.step, C.beam_distance + C.plinth + C.spacing), C.obeam_height,
        ptList[29])
CurvesC(a(C.range_a, C.step, C.beam_distance + C.plinth + 2.0 * C.spacing),
        b(C.range_b, C.step, C.beam_distance + C.plinth + 2.0 * C.spacing), v, 0,
        ptList[30])
CurvesE(a(C.range_a, C.step, C.beam_distance + C.plinth + 2.0 * C.spacing),
        b(C.range_b, C.step, C.beam_distance + C.plinth + 2.0 * C.spacing), C.obeam_height,
        ptList[31])
CurvesC(a(C.range_a, C.step, C.beam_distance + 2.0 * C.plinth + 3.0 * C.spacing),
        b(C.range_b, C.step, C.beam_distance + 2.0 * C.plinth + 3.0 * C.spacing), v, 0,
        ptList[32])
CurvesE(a(C.range_a, C.step, C.beam_distance + C.plinth + 3.0 * C.spacing),
        b(C.range_b, C.step, C.beam_distance + C.plinth + 3.0 * C.spacing), C.obeam_height,
        ptList[33])
CurvesC(a(C.range_a, C.step, C.beam_distance + C.beam_width + C.br_width),
        b(C.range_b, C.step, C.beam_distance + C.beam_width + C.br_width), v,
        C.plate_height, ptList[34])
CurvesC(a(C.range_a, C.step, -C.br_width), b(C.range_b, C.step, -C.br_width), v,
        C.plate_height, ptList[35])

'''
''' Wywyołanie krzywych odbitej części '''
'''
CurvesD(0, 0, ptList[18])
CurvesD(C.plinth, C.ibeam_height, ptList[19])
CurvesD(C.plinth + C.spacing, 0, ptList[20])
CurvesD(C.plinth + C.spacing, C.ibeam_height, ptList[21])
CurvesD(2.0 * C.spacing + C.plinth, 0, ptList[22])
CurvesD(2.0 * C.spacing + C.plinth, C.ibeam_height, ptList[23])
CurvesD(3.0 * C.spacing + 2.0 * C.plinth, 0, ptList[24])
CurvesD(3.0 * C.spacing + C.plinth, C.ibeam_height, ptList[25])
CurvesD(C.beam_distance, 0, ptList[26])
CurvesD(C.beam_distance + C.plinth, C.obeam_height, ptList[27])
CurvesD(C.beam_distance + C.plinth + C.spacing, 0, ptList[28])
CurvesD(C.beam_distance + C.plinth + C.spacing, C.obeam_height, ptList[29])
CurvesD(C.beam_distance + C.plinth + 2.0 * C.spacing, 0, ptList[30])
CurvesD(C.beam_distance + C.plinth + 2.0 * C.spacing, C.obeam_height, ptList[31])
CurvesD(C.beam_distance + 2.0 * C.plinth + 3.0 * C.spacing, 0, ptList[32])
CurvesD(C.beam_distance + C.plinth + 3.0 * C.spacing, C.obeam_height, ptList[33])
CurvesD(C.beam_distance + C.beam_width + C.br_width, C.plate_height, ptList[34])
CurvesD(-C.br_width, C.plate_height, ptList[35])
'''