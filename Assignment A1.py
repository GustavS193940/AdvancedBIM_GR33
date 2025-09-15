# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 15:11:35 2025

@author: gusta
"""

import ifcopenshell as ifc
import time

import os
import numpy as np

model = ifc.open('25-16-D-ARCH.ifc')

"""
Validate facade material layers
25-16-D-MAT page 14
"""

GlobalId = "2kV3yFLUL4LfmQ8w7$G6Jj"
wall = model.by_guid(GlobalId)

ifc_material = ifc.util.element.get_material(wall)[0]

for i in range(len(ifc_material)):
    materialLayer = ifc_material[i]
    print("Material layer", i+1, "is", materialLayer[1], "mm thick")
    print("Material layer", i+1, "is made of:", materialLayer[3], '\n')
