from pyplasm import *


#primo blocco 
verts0PVert = [[3,3],[3.2,3],[3,12],[3.2,12]]
cells0PVert = [[1,2,3,4]]
pols0PVert = None
wall0P = MKPOL([verts0PVert, cells0PVert, pols0PVert])
wall0SolidVert = PROD([wall0P,Q(27)])
wall1SolidVert = T([1])([8.8])(wall0SolidVert)


orzs0POrz = [[3,3],[3,3.2],[12,3],[12,3.2]]
cells0POrz = [[1,2,3,4]]
pols0POrz = None
wall0POrz = MKPOL([orzs0POrz, cells0POrz, pols0POrz])
wall0SolidOrz = PROD([wall0POrz,Q(27)])
wall1SolidOrz = T([2])([8.8])(wall0SolidOrz)

verts1piano = [[3,3],[12,3],[3,12],[12,12]]
cells1piano = [[1,2,3,4]]
pols1piano = None
wall01piano= MKPOL([verts1piano, cells1piano, pols1piano])
wall0Solid1piano = PROD([wall01piano,Q(0.2)])
wall1Solid1piano = T([3])([27])(wall0Solid1piano)

verts111piano = [[3,3],[12,3],[3,12],[12,12]]
cells111piano = [[1,2,3,4]]
pols111piano = None
wall0111piano= MKPOL([verts111piano, cells111piano, pols111piano])
wall0Solid111piano = PROD([wall0111piano,Q(0.2)])



#finestre primo blocco

verts0Windows = [[3.3,3],[3.7,3],[3.3,3.2],[3.7,3.2]]
cells0Windows = [[1,2,3,4]]
pols0Windows = None
windows = MKPOL([verts0Windows, cells0Windows, pols0Windows])
windowsProd = PROD([windows,Q(0.6)])
windowsTrasl = T([3])([0.3])(windowsProd)
windowsColonne = STRUCT([windowsTrasl, T(1)(1)]*9)
windowsRighe = STRUCT([windowsColonne, T(3)(1)]*25)
windowsTrasl1 = T([2])([8.8])(windowsTrasl)
windowsColonne1 = STRUCT([windowsTrasl1, T(1)(1)]*9)
windowsRighe1 = STRUCT([windowsColonne1, T(3)(1)]*25)
###########
verts0Windows1 = [[3,3.3],[3,3.7],[3.2,3.3],[3.2,3.7]]
cells0Windows1 = [[1,2,3,4]]
pols0Windows1 = None
windows1 = MKPOL([verts0Windows1, cells0Windows1, pols0Windows1])
windowsProd1 = PROD([windows1,Q(0.6)])
windowsTrasl2 = T([3])([0.3])(windowsProd1)
windowsColonne2 = STRUCT([windowsTrasl2, T(2)(1)]*9)
windowsRighe2 = STRUCT([windowsColonne2, T(3)(1)]*25)
windowsTrasl3 = T([1])([8.8])(windowsTrasl2)
windowsColonne3 = STRUCT([windowsTrasl3, T(2)(1)]*9)
windowsRighe3 = STRUCT([windowsColonne3, T(3)(1)]*25)

#secondo blocco 
verts0PVert1 = [[3,3],[3.2,3],[3,9],[3.2,9]]
cells0PVert1 = [[1,2,3,4]]
pols0PVert1 = None
wall0P1 = MKPOL([verts0PVert1, cells0PVert1, pols0PVert1])
wall0SolidVert1 = PROD([wall0P1,Q(27)])
wall1SolidVert1OK = T([3])([27])(wall0SolidVert1)
wall1SolidVert1 = T([1,2])([8.8,3])(wall1SolidVert1OK)

orzs0POrz1 = [[3,3],[3,3.2],[9,3],[9,3.2]]
cells0POrz1 = [[1,2,3,4]]
pols0POrz1 = None
wall0POrz1 = MKPOL([orzs0POrz1, cells0POrz1, pols0POrz1])
wall0SolidOrz1 = PROD([wall0POrz1,Q(27)])
wall1SolidOrz1OK = T([3])([27])(wall0SolidOrz1)
wall1SolidOrz1 = T([1,2])([3,8.8])(wall1SolidOrz1OK)

verts0PVert12 = [[6,9],[6.2,9],[6,12],[6.2,12]]
cells0PVert12 = [[1,2,3,4]]
pols0PVert12 = None
wall0P12 = MKPOL([verts0PVert12, cells0PVert12, pols0PVert12])
wall0SolidVert2 = PROD([wall0P12,Q(27)])
wall1SolidVert2OK = T([3])([27])(wall0SolidVert2)
wall1SolidVert2 = T([1,2])([2.8,-6])(wall1SolidVert2OK)

orzs0POrz12 = [[3,9],[3,8.8],[6,9],[6,8.8]]
cells0POrz12 = [[1,2,3,4]]
pols0POrz12 = None
wall0POrz12 = MKPOL([orzs0POrz12, cells0POrz12, pols0POrz12])
wall0SolidOrz12 = PROD([wall0POrz12,Q(27)])
wall1SolidOrz2OK = T([3])([27])(wall0SolidOrz12)
wall1SolidOrz2 = T([1,2])([6,-2.8])(wall1SolidOrz2OK)

verts2piano = [[3,3],[9,3],[3,9],[9,9]]
cells2piano = [[1,2,3,4]]
pols2piano = None
wall02piano= MKPOL([verts2piano, cells2piano, pols2piano])
wall0Solid2piano = PROD([wall02piano,Q(0.2)])
wall1Solid2piano = T([3])([54])(wall0Solid2piano)

verts22piano = [[6,6],[12,6],[12,12],[6,12]]
cells22piano = [[1,2,3,4]]
pols22piano = None
wall022piano= MKPOL([verts22piano, cells22piano, pols22piano])
wall0Solid22piano = PROD([wall022piano,Q(0.2)])
wall1Solid22piano = T([3])([54])(wall0Solid22piano)

#finestre secondo blocco

verts0Windows4 = [[3.3,3],[3.7,3],[3.3,3.2],[3.7,3.2]]
cells0Windows4 = [[1,2,3,4]]
pols0Windows4 = None
windows4 = MKPOL([verts0Windows4, cells0Windows4, pols0Windows4])
windowsProd4 = PROD([windows4,Q(0.6)])
windowsTrasl4 = T([3])([27.3])(windowsProd4)
windowsColonne4 = STRUCT([windowsTrasl4, T(1)(1)]*6)
windowsRighe4 = STRUCT([windowsColonne4, T(3)(1)]*25)
windowsTrasl5 = T([1,2])([3,8.8])(windowsTrasl4)
windowsColonne5 = STRUCT([windowsTrasl5, T(1)(1)]*6)
windowsRighe5 = STRUCT([windowsColonne5, T(3)(1)]*25)
windowsTrasl51 = T([2])([5.8])(windowsTrasl4)
windowsColonne51 = STRUCT([windowsTrasl51, T(1)(1)]*3)
windowsRighe51 = STRUCT([windowsColonne51, T(3)(1)]*25)
windowsTrasl52 = T([1,2])([6,3])(windowsTrasl4)
windowsColonne52 = STRUCT([windowsTrasl52, T(1)(1)]*3)
windowsRighe52 = STRUCT([windowsColonne52, T(3)(1)]*25)
windowsA = STRUCT([windowsColonne4,windowsColonne5,windowsRighe5,windowsRighe4,windowsColonne51,windowsRighe51,windowsColonne52,windowsRighe52])
###########
verts0Windows6 = [[3,3.3],[3,3.7],[3.2,3.3],[3.2,3.7]]
cells0Windows6 = [[1,2,3,4]]
pols0Windows6 = None
windows6 = MKPOL([verts0Windows6, cells0Windows6, pols0Windows6])
windowsProd6 = PROD([windows6,Q(0.6)])
windowsTrasl6 = T([3])([27.3])(windowsProd6)
windowsColonne6 = STRUCT([windowsTrasl6, T(2)(1)]*6)
windowsRighe6 = STRUCT([windowsColonne6, T(3)(1)]*25)
windowsTrasl7 = T([1,2])([8.8,3])(windowsTrasl6)
windowsColonne7 = STRUCT([windowsTrasl7, T(2)(1)]*6)
windowsRighe7 = STRUCT([windowsColonne7, T(3)(1)]*25)
windowsTrasl71 = T([1])([5.8])(windowsTrasl6)
windowsColonne71 = STRUCT([windowsTrasl71, T(2)(1)]*3)
windowsRighe71 = STRUCT([windowsColonne71, T(3)(1)]*25)
windowsTrasl72 = T([1,2])([3,6])(windowsTrasl6)
windowsColonne72 = STRUCT([windowsTrasl72, T(2)(1)]*3)
windowsRighe72 = STRUCT([windowsColonne72, T(3)(1)]*25)
windowsB = STRUCT([windowsColonne6,windowsRighe6,windowsRighe7,windowsRighe7,windowsColonne71,windowsRighe71,windowsRighe72,windowsColonne72])

#terzo blocco 
verts0PVert2 = [[3,6],[3.2,6],[3,9],[3.2,9]]
cells0PVert2 = [[1,2,3,4]]
pols0PVert2 = None
wall0P2 = MKPOL([verts0PVert2, cells0PVert2, pols0PVert2])
wall0SolidVert22 = PROD([wall0P2,Q(15)])
wall1SolidVert3OK = T([3])([54])(wall0SolidVert22)
wall1SolidVert22 = T([1])([8.8])(wall1SolidVert3OK)
wall1SolidVert3 = T([1,2])([3,3])(wall1SolidVert3OK)
wall1SolidVert4 = T([1,2])([3,-3])(wall1SolidVert3OK)
wall1SolidVert5 = T([1,2])([5.8,3])(wall1SolidVert3OK)
wall1SolidVert6 = T([1,2])([5.8,-3])(wall1SolidVert3OK)

verts0PVert21 = [[6,3],[6,3.2],[9,3],[9,3.2]]
cells0PVert21 = [[1,2,3,4]]
pols0PVert21 = None
wall0P21 = MKPOL([verts0PVert21, cells0PVert21, pols0PVert21])
wall0SolidVert222 = PROD([wall0P21,Q(15)])
wall1SolidVert4OK = T([3])([54])(wall0SolidVert222)
wall1SolidVert222 = T([2])([8.8])(wall1SolidVert4OK)
wall1SolidVert32 = T([1,2])([-3,3])(wall1SolidVert4OK)
wall1SolidVert42 = T([1,2])([3,3])(wall1SolidVert4OK)
wall1SolidVert52 = T([2,1])([5.8,3])(wall1SolidVert4OK)
wall1SolidVert62 = T([2,1])([5.8,-3])(wall1SolidVert4OK)

verts33piano = [[3,6],[12,6],[3,9],[12,9]]
cells33piano = [[1,2,3,4]]
pols33piano = None
wall033piano= MKPOL([verts33piano, cells33piano, pols33piano])
wall0Solid33piano = PROD([wall033piano,Q(0.2)])
wall1Solid33piano = T([3])([69])(wall0Solid33piano)
verts333piano = [[6,3],[9,3],[6,12],[9,12]]
cells333piano = [[1,2,3,4]]
pols333piano = None
wall0333piano= MKPOL([verts333piano, cells333piano, pols333piano])
wall0Solid333piano = PROD([wall0333piano,Q(0.2)])
wall1Solid333piano = T([3])([69])(wall0Solid333piano)
wallG = STRUCT([wall1Solid33piano,wall1Solid333piano])

allwallA = STRUCT([wall1SolidVert3OK,wall1SolidVert22,wall1SolidVert3,wall1SolidVert4,wall1SolidVert5,wall1SolidVert6,wall1SolidVert4OK,wall1SolidVert222,wall1SolidVert32,wall1SolidVert42,wall1SolidVert52,wall1SolidVert62,wallG])

#finestre terzo blocco

verts0Windows9 = [[6.3,3],[6.7,3],[6.3,3.2],[6.7,3.2]]
cells0Windows9 = [[1,2,3,4]]
pols0Windows9 = None
windows9 = MKPOL([verts0Windows9, cells0Windows9, pols0Windows9])
windowsProd9 = PROD([windows9,Q(0.6)])
windowsTrasl9 = T([3])([54.3])(windowsProd9)
windowsColonne9 = STRUCT([windowsTrasl9, T(1)(1)]*3)
windowsRighe9 = STRUCT([windowsColonne9, T(3)(1)]*13)
windowsTrasl8 = T([1,2])([-3,3])(windowsTrasl9)
windowsColonne8 = STRUCT([windowsTrasl8, T(1)(1)]*3)
windowsRighe8 = STRUCT([windowsColonne8, T(3)(1)]*13)
windowsTrasl81 = T([2])([8.8])(windowsTrasl9)
windowsColonne81 = STRUCT([windowsTrasl81, T(1)(1)]*3)
windowsRighe81 = STRUCT([windowsColonne81, T(3)(1)]*13)
windowsTrasl82 = T([1,2])([3,3])(windowsTrasl9)
windowsColonne82 = STRUCT([windowsTrasl82, T(1)(1)]*3)
windowsRighe82 = STRUCT([windowsColonne82, T(3)(1)]*13)
windowsTrasl83 = T([1,2])([-3,5.8])(windowsTrasl9)
windowsColonne83 = STRUCT([windowsTrasl83, T(1)(1)]*3)
windowsRighe83 = STRUCT([windowsColonne83, T(3)(1)]*13)
windowsTrasl84 = T([1,2])([3,5.8])(windowsTrasl9)
windowsColonne84 = STRUCT([windowsTrasl84, T(1)(1)]*3)
windowsRighe84 = STRUCT([windowsColonne84, T(3)(1)]*13)
windowsJ = STRUCT([windowsColonne9,windowsColonne8,windowsRighe8,windowsRighe9,windowsColonne81,windowsRighe81,windowsColonne82,windowsRighe82,windowsColonne83,windowsRighe83,windowsColonne84,windowsRighe84])
###########
verts0Windows15 = [[3,6.3],[3,6.7],[3.2,6.3],[3.2,6.7]]
cells0Windows15 = [[1,2,3,4]]
pols0Windows15 = None
windows15 = MKPOL([verts0Windows15, cells0Windows15, pols0Windows15])
windowsProd15 = PROD([windows15,Q(0.6)])
windowsTrasl15 = T([3])([54.3])(windowsProd15)
windowsColonne15 = STRUCT([windowsTrasl15, T(2)(1)]*3)
windowsRighe15 = STRUCT([windowsColonne15, T(3)(1)]*13)
windowsTrasl16 = T([2,1])([-3,3])(windowsTrasl15)
windowsColonne16 = STRUCT([windowsTrasl16, T(2)(1)]*3)
windowsRighe16 = STRUCT([windowsColonne16, T(3)(1)]*13)
windowsTrasl161 = T([1])([8.8])(windowsTrasl15)
windowsColonne161 = STRUCT([windowsTrasl161, T(2)(1)]*3)
windowsRighe161 = STRUCT([windowsColonne161, T(3)(1)]*13)
windowsTrasl162 = T([2,1])([3,3])(windowsTrasl15)
windowsColonne162 = STRUCT([windowsTrasl162, T(2)(1)]*3)
windowsRighe162 = STRUCT([windowsColonne162, T(3)(1)]*13)
windowsTrasl163 = T([2,1])([-3,5.8])(windowsTrasl15)
windowsColonne163 = STRUCT([windowsTrasl163, T(2)(1)]*3)
windowsRighe163 = STRUCT([windowsColonne163, T(3)(1)]*13)
windowsTrasl164 = T([2,1])([3,5.8])(windowsTrasl15)
windowsColonne164 = STRUCT([windowsTrasl164, T(2)(1)]*3)
windowsRighe164 = STRUCT([windowsColonne164, T(3)(1)]*13)
windowsH = STRUCT([windowsColonne15,windowsColonne16,windowsRighe16,windowsRighe15,windowsColonne161,windowsRighe161,windowsColonne162,windowsRighe162,windowsColonne163,windowsRighe163,windowsColonne164,windowsRighe164])

#quarto blocco 
verts0PVert99 = [[6,6],[6.2,6],[6,9],[6.2,9]]
cells0PVert99 = [[1,2,3,4]]
pols0PVert99 = None
wall0P99 = MKPOL([verts0PVert99, cells0PVert99, pols0PVert99])
wall0SolidVert99 = PROD([wall0P99,Q(15)])
wall1SolidVert99K = T([3])([69])(wall0SolidVert99)
wall1SolidVert61 = T([1])([5.8])(wall1SolidVert99K)

verts0PVert98 = [[6,6],[6,6.2],[12,6],[12,6.2]]
cells0PVert98 = [[1,2,3,4]]
pols0PVert98 = None
wall0P98 = MKPOL([verts0PVert98, cells0PVert98, pols0PVert98])
wall0SolidVert2222 = PROD([wall0P98,Q(15)])
wall1SolidVert98K = T([3])([69])(wall0SolidVert2222)
wall1SolidVert62 = T([2])([2.8])(wall1SolidVert98K)

allwallE = STRUCT([wall1SolidVert98K,wall1SolidVert99K,wall1SolidVert61,wall1SolidVert62])

verts4piano = [[6,6],[12,6],[12,9],[6,9]]
cells4piano = [[1,2,3,4]]
pols4piano = None
wall04piano= MKPOL([verts4piano, cells4piano, pols4piano])
wall0Solid4piano = PROD([wall04piano,Q(0.2)])
wall1Solid4piano = T([3])([84])(wall0Solid4piano)


#finestre quarto blocco

verts0Windows55 = [[6.3,6],[6.7,6],[6.3,6.2],[6.7,6.2]]
cells0Windows55 = [[1,2,3,4]]
pols0Windows55 = None
windows55 = MKPOL([verts0Windows55, cells0Windows55, pols0Windows55])
windowsProd55 = PROD([windows55,Q(0.6)])
windowsTrasl44 = T([3])([69.3])(windowsProd55)
windowsColonne55 = STRUCT([windowsTrasl44, T(1)(1)]*6)
windowsRighe55 = STRUCT([windowsColonne55, T(3)(1)]*13)
windowsTrasl98 = T([2])([2.8])(windowsTrasl44)
windowsColonne98 = STRUCT([windowsTrasl98, T(1)(1)]*6)
windowsRighe98 = STRUCT([windowsColonne98, T(3)(1)]*13)

windowsP = STRUCT([windowsColonne55,windowsRighe55,windowsColonne98,windowsRighe98])

verts0Windows77 = [[6,6.3],[6,6.7],[6.2,6.3],[6.2,6.7]]
cells0Windows77 = [[1,2,3,4]]
pols0Windows77 = None
windows77 = MKPOL([verts0Windows77, cells0Windows77, pols0Windows77])
windowsProd77 = PROD([windows77,Q(0.6)])
windowsTrasl77 = T([3])([69.3])(windowsProd77)
windowsColonne77 = STRUCT([windowsTrasl77, T(2)(1)]*3)
windowsRighe77 = STRUCT([windowsColonne77, T(3)(1)]*13)
windowsTrasl78 = T([1])([5.8])(windowsTrasl77)
windowsColonne78 = STRUCT([windowsTrasl78, T(2)(1)]*3)
windowsRighe78 = STRUCT([windowsColonne78, T(3)(1)]*13)

windowsPP = STRUCT([windowsColonne77,windowsRighe77,windowsColonne78,windowsRighe78])


opera = STRUCT([wall0SolidOrz,wall1SolidOrz,wall0SolidVert,wall1SolidVert,wall1SolidVert1OK,wall1SolidVert1,wall1SolidOrz1OK,wall1SolidOrz1,wall1SolidVert2OK,wall1SolidVert2,wall1SolidOrz2OK,wall1SolidOrz2,wall1Solid1piano,wall1Solid2piano,wall1Solid22piano,allwallA,wall0Solid111piano,allwallE,wall1Solid4piano])
opera1 = DIFFERENCE([opera,windowsColonne,windowsRighe,windowsColonne1,windowsRighe1,windowsColonne3,windowsColonne2,windowsRighe3,windowsRighe2,windowsA,windowsB,windowsJ,windowsH,windowsP,windowsPP])
VIEW(COLOR([0.38823335,0.592156,0.7098039])(S([1,2,3])([0.6,0.6,0.6])(opera1)))