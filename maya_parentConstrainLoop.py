import maya.cmds as cmds

quantity = 10

# Parent Parameters:
parentPrefix = "parentObj"
parentStartNum = 1
parentSuffix = ""
onlyParent = False		# True if parenting multiple things to single obj

# Child Parameters:
childPrefix = "childObj"
childStartNum = 1
childSuffix = ""

# Parent Constraint Parameters:

constrainName = childPrefix + "_parentConstrain1"
weight = 1.0                    # default is 1.0
maintainOffset = 0				# 0 = offset off, 1 = on
skipTranslate = []				# st = ["x", "y"]
skipRotate = []                 # sr = ["x", "z"]

# define loop parameters
parentNum = parentStartNum
childNum = childStartNum

for i in range(quantity):
    currentParent = parentPrefix + str(parentNum) + parentSuffix
    currentChild = childPrefix + str(childNum) + childSuffix
    cmds.parentConstraint( currentParent, currentChild, w = weight, name = constrainName, mo = maintainOffset, st = skipTranslate, sr = skipRotate )
    
    if onlyParent == True:
        parentNum = 1
    else:
        parentNum += 1

    childNum += 1

