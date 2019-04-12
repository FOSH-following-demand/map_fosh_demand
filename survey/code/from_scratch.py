#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:38:04 2019

@author: andre
"""

import pandas as pd
import csv
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


"""
keys:

    a03--Gender
    a06--City
    a05--State
    a04--Country
    b02--Formation
    b01--Highest degree
    b03--affilliated
    b04--which one
    
    
"""

#define dictionaries to accomodate for different spellings, mistakes, etc.

new_equipment1={
          "2-photon microscope":["2-photon microscope","Two photon microscope","two photon microscope",
                                 "two photon microscope for calcium imaging","2-photon microscopes",
                                 "Two-photon microscope","two photon microscope","Microscope adequate for life imaging of cells ",
                                 "2-photon microscope"],
          "3d printer":["industry grade 3d printer"],
          "acoustic testing system":["Bancs de tests acoustiques "],
          "aerial rov":["Improved drone","Drone tipo octocóptero","drone"],
          "atomic absorption spectroscopy":["Atomic absorpbtion spectrometer"],
          "aquatic rov":["Remotely operated underwater vehicle","Remote control underwater drones"],
          "automated titrator":["Large replicate size automated alkalinity titrator"],
          "behavioural setup":["Operanda for operant chambers", "Animal behavior test","High throughput behavioural arena",
                              "startle chambers for prepulse inhibition on mouse"],
          "bioreactor":["bioreactors for the production of microbial biomass on pilot-scale","Bioreactor"],
          "bioprinter":["Bioprinter"],
          "bio safety cabinet":["microbiological safety cabinet","Bio-safety cabinet"],
          "blood test tools":["mashines for blood test"],
          "buoys with sensors":["automated buoys to track conditions in real time at Flower Garden Banks","Buoys"],
          "centrifuge":["table top centrifuges","Very high speed centrifuge (50mL's at 15krcf)",
                        "ultracentrifuge","Microcentrifuge","refrigerated centrifuge",
                        "new ultracentrifuge and new rotors","Centrífuga"],
          "cnc":["computer numerically controlled milling machine",
                 "machine outil à commande numérique","grand routeur CNC",
                 "Automatic CNC milling machine"],
          "confocal microscope":["Confocal microscope","confocal microscope","Spinning disk confocal micrscope",
                                 "Confocal microscope","Confocal microscope ","Live cell imaging confocal scope, w/laser based automfocys",
                                 "confocal microscope","Confocal microscope"],
          "components":["sensors","Multimeter","USB-GPIB (Electronics to communicate with old lab equipment)","Placas arduino"],
          "computer":["Mac pc","New laptop","CUDA-enabled card of compute capability >= 3.5",
                      "Graphic processing units (GPUs)","Better computers (better CPU)"],
          "computer cluster":["Supercomputer cores","Beowulf cluster"],
          "cytometer":["Flow cytometer","citometro de fluxo com imagem (imaging flow cytometer)"],
          "data acquisition board":["data acquisition board (DAQ)"],
          "electron microscope":["Serial block-face scanning electron microscope","Tunneling Electron Microscopy","ESEM"],
          "electrophysiology system":["electrophysiology set-up","Electrophysiology rig","Patch clamp amplifier",
                                      "Multi-electrode array","electrophysiological tools","voltage clamp fluorometry",
                                      "Neuronal signal processor","electrophysiology data acquisition system with more channels"],
          "electrical amplifier ":["electrical amplifier "],
          "electrophoresis unit":["electrophoresis unit","Electrophoresis"], 
          "electroporator":["Electroporator"],
          "eye tracker":["Eye tracker","Eye-trackers"],
          "filtration system":["Tanfential flow filtration device"],
          "fluorometer":["fluorometer"],
          "fluorescence imaging tools":["Fluorescence Imaging Tools"],
          "fluorescence microscope":["Fluorescence Microscope","Microscopio de fluorescencia","Fluorescence microscope",
                                     "A fluorescent microscope","Floresence Microscope"],
          "freezer":["Deep freezers"],
          "ftir microscope":["Microscope FTIR ","raman microsope"],
          "gas analyser":["pCO2 probe (functional)"],
          "gas chromatography system":["Gas chromatography system","Gas chromatograph orbitrap mass spectrometer "],
          "hyperion imaging cyof":["Hyperion (imaging CyOF)"],
          "high performance liquid chromatography":["uplc","UHPLC","A High Performance liquid Chromotography machine ","high-pressure liquid chromatograph with tandem mass-sepctrometry"],
          "high speed camera":["high speed cameras"],
          "iScript cDNA kit":["iScript cDNA kit"],
          "immunoabsorbent assay machine":["immunoabsorbent assay machine"],
          "imunoassay system":["Bioplex machine"],
          "incubator":["CO2 incubator","Controlled environment growth chamber"],
          "jabber":["jabber"],
          "kymograph":["kymograph"],
          "laser cutter":["laser cutter"],
          "light Sheet microscope":["light Sheet microscope","Light Sheet Microscope (ideally a lattice light sheet)","Light sheet microscope"],
          "liquid chromatography purification station":["liquid chromatography purification station"],
          "liquid handling robot":["Liquid-handling robot","Liquid handling robot"],
          "litography machine":["Electron Beam Lithograph"],
          "machine to prepare carbon grids for electron microscopy":["Machine to prepare carbon grids for electron microscopy"],
          "mass spectrometer":["Mass spectrometer","detector de espectrometria de massas
"],
          "meg system":["Mobile magnetoencephalography system"],
          "micromanipulator":["micromanipulator","Micromanipulator with accessories"],
          "microspectrophotometer":["microspectrophotometer (nanodrop)","Nanodrop"],
          "microtome":["freezing microtome"],
          "microfluidics system":["microfluidics workstation"],
          "mri":["an MRI at a Tesla higher than 3"],
          "optical microscope":["better microscopes","Optical imaging miniscope in vivo","Microscope",
                                "a second high power microscope","microscope",
                                "Transmitted light microscope"],
          "oscilloscope":["Oscilloscope"],
          "oven for dissecating plants":["Big simplisia oven"],
          "petrographic microscope":["Petrographic microscope"],
          "plate reader":["Leitor de Absorbância de Microplacas de 96 poços com flexibilidade de comprimento de ondas","plate reader"],
          "potentiostat ":["Potentiostat "],
          "power supply":["POWER SUPPLY"],
          "pulsed Laser":["Pulsed Laser"],
          "pick and place machine":["Juli pick and place machine"],
          "pyrosequencer":["Pyrosequencer"],
          "qubit":["Qubit cuantificador con alta sensibilidad de RNA, DNA y proteína"],
          "respirometry":["Respirimetry equipment "],
          "rotary evaporator":["Rotary evaporator"],
          "raman spectrophotometer":["Portable Raman spectroscopy"],
          "real time thermocycler":["termociclador en tiempo real","Real Time Machine"],
          "server":["Microserver"],
          "sequencer":["adn reading machine","Oxford nanopore sequencer",
                       "Next generation Sequencing platform"], 
          "spectrophotometer":["Infrared Spectrophotometer"],
          
          "satelitte":["geostationary satellite with multispectral radiometers"],
          "single cell sequencer":["Máquina de secuenciación de single cell","10X single cell sequencing machine"],
          "screen":["A better screen"],
          "stereotaxic":["semi-automated stereotaxic"],
          "tablet press machine":["Tablet making machine"],
          "thermal camera":["infrared and thermal cameras"],
          "thermocycler":["thermocycler","Thermocycler","Thermocycler", "Thermal Cycler",
                          "A thermocycler","Thermocycler","Thermocycler",
                          "Thermocycler","thermocycler"],
          "tilt machine":["Tilt machine"],
          "turbidostat":["morbidostat"],
          "tissue homogenizer":["tissue homogenizer"],
          "tissue/organ bath":["tissue/organ bath"],
          "transilluminator":["Ultraviolet Transilluminator","Transilluminator"],
          "undefined":["Something unique that would allow us to be the national/international hub for leading research in a specific area",
                       "ACTA","N/A","dasdsa","2C-I","uma maquina propria"
                       "MRI processing software","Reagents ","nn consigo definir apenas um"
                       "components to build the kits described above","NA"],
          "universal materials testing machine":["Universal Materials Testing Machine","Universal Testing Machine"],
          "super resolution microscope":["Ultra resolution microscope","Super resolution microscope"],
          "visual stimulator":["A high-resolution, flexible digital screen to project visual stimulation",
                               "a decent light stimulation setup"],
          "x ray diffractometer":["Single Crystal X-ray Diffractometer","Xray diffractometer"],
          "western blot tools":["Western Blotting equipments"],
          "whiteboard":["more whiteboards"],

          }
"nao sei responder","os ja citados","nao sei"
"poligrafo (para eeg)","eeg quantitativo com foto estimulador"
analise elementar chns-o
microscopio confocal
hplc-ms
ion mobility ou orbitrap
"hplc","hplc acoplado ao massa"
incubadora com agitacao
computadores workstation
analisador de gases
inbody
irga
phmetro
autoclave
sequenciador illumina
"citometro de fluxo","citometria de fluxo"
impressora 3d e sequenciador de dna
microscopio eletronico
rmn
equipamentos de biologia molecular/epigenetica/gwas
capela
vidrarias
coluna para hplc/espectrometro de massas
celular top de linha, impressora e telescopio
hplc, espectrofotometro de absorcao atomica
amplificador (kit) brainproducts 64 canais com sistema sem fio
montar um laboratorio adequado. faltam praticamente todos os equipamentos por aqui
leitor de placa p fluorescencia
todos para um laboratorio de qualidade para graduacao em biologia e quimica fisica...
espectometro de massa
espectrofotometro
camaras de crescimento de plantas
mev-feg
espectrometro de massa
softwares de terapia e avaliacao de linguagem
cromatografo
microscopio
biorreator
microscopio confocal
mais sequenciadores e quantificadores
estufa incubadora
martelos pneumaticos, equipamentos para analise histologica
um computador com capacidade para analises de bioinformatica, 
qtof, 
termocicladores, 
qubit
microscopios e pipetas de precisao
ms/ms;
"termociclador qpcr","rt-pcr","real time",
setup de patch clamp com o sistema para medida de fotometria
laboratorio completo para ensino fundamental i e ii, com material (experimentoteca e laboratorial) para ensino de quimica, fisica e biologia
computadores mais modernos
3i vivio
capela de fluxo laminar
cg-ms
sequenciador de nova geracao
servidor
espectrofotometro
a questao muitas vezes nao e o equipamento mas sim os reagentes
centrifuga refrigerada
estereomicroscopios com tela
shaker
sequenciador
termociclador 
microscopio invertido
microscopios, vidrarias
cintilador de fase liquida
microscopio eletronico
microscopio com camera digital, impressora 3d, entre outros
incubadora com controle de oxigenio e gas carbonico, microscopio invertido, lupas
equipamentos para substituir o destilador.
osmose reversa e pipetas
cg-ms e hplc-ms
computadores e projetores com tecnologia mais avancada
ultramicrotomo
leitor de placa de elisa
espectrofotometro
hplc
refletor; 
ilha de edicao
cg-ms, 
hplc acoplado a massas
centrifuga de eppendorf
dsc
icp-ms




new_equipment2 = {"2-photon microscope":["Two photon microscope","two photon mesoscope"],
                  "3d printer":["High end 3D printer (or suite of them that printed different substrate like resin, filament, paper)",
                                "3d printer"],
                  "aerial rov":["drone for aerial survey of field station","ROV"],
                  "aquatic rov":["Wave glider"],
                  "augmented reality tool":["équipement de réalité virtuelle / augmentée"],
                  "behavioural setup":["System for behavioral analysis by touch for small rodents",
                                       "8 arms radial maze for mice","Automated movement analysis machine for monitoring flies",
                                       "an open loop animal behavioural paradigm under a two photon microscope"],
                  "bioanalyser":["bioanalycer para comprovar el estado de conservacion de las extracciones de RNA"],
                  "camera":["a good camara","Advanced camera traps","Underwater cameras with long battery life",
                            "more microscope cameras so we didn't have to move the one camera we have between microscopes","Live feed camera technology from FGBNMS"],
                  "centrifuge":["new high speed centrifuges","ultra centrifuge swinging bucket rotor", "Centrifuge","centrifugadora refrigerada"],
                  "cnc":["Circuit board making machine"],
                  "colony picking robot":["Colony-picking robot"],
                  "components":["raspberry pi","Raspberry Pi","Sensores de señales para placas arduino"],
                  "computer":["Super-fast computer","More RAM and HDD storage.","Fast computer","enough computers and softwares for data analysis"],
                  "confocal microscope":["Airyscan confocal microscope"],
                  "cluster":["Upgrades to cluster in terms of speed and memory"],
                  "cytometer":["bench-top cytometer","Flow cytometer"],
                  "data acquisition board":["High quality data aquision cards"],
                  "dishwasher":["A glassware/lab dishwasher"],
                  "dissolution apparatus":["Dissolution apparatus"],
                  "dna manipulation tools":["DNA Manipulation Tools"],
                  "dual energy x ray absorpiometry":["dual X-ray absorptimeter"],
                  "endoscopes":["Miniendoscopes"],
                  "electrical stimulator":["electrical stimulator"],
                  "electron microscope":["Scanning Election Microscopy"],
                  "electroencephalogram":["Mobil EEG, GSR","Electroencephalograph"],
                  "electrophoresis":["Electrophoresis system for agarose gels","SDS-PAGE gel plates and electrophoresis equipment"],
                  "electrophysiology system":["amplifiers for electrophysiology","two electrode voltage clamp","Linear Recording Probes"],
                  "fluorescence microscope":["fluorescence microscope","Fluorescence microscope",
                                             "total-internal-reflection fluorescence microscope","A fluorescent microscope", 
                                             "Fluorescent microscope","Reflected fluorescence microscope"],
                  "fluorometer":["Imaging PAM Chlorophyll Fluorometer"],
                  "freezer":["Big freezer","-80C freezer","-80°C fridge"],
                  "gas analyser":["Off line gas analyser","mobile atmospheric CO2 sensor"],
                  "gas chromatography system":["Gass-chromatography mass spectrometry machine","Gas chromatograph isotope ratio mass spectrometer"],
                  "heating block":["heat blocks"],
                  "high performance liquid chromatography":["Hplc" ,"HPLC machine"],
                  "homogeneizer":["Homogenizer"],
                  "incubator":["Incubator","Incubators","Green house"],
                  "laminar flow hood":["UV hood","Laminar flowhood"],
                  "laser":["Laser uncaging system for electrophysiology rig",
                           "Femtosecond Laser with tunable wavelength from X-ray to IR"],
                  "laser shutter":["Shutters for lasers"],
                  "liquid handling robot":["Robot rna extractor",
                                           "Liquid handling station",
                                           "All in one robotic culture system"],
                  "mass spectrometer":["Mass spectrophotometer"],
                  "micromanipulator":["Electrode drive with motors"],
                  
                  "mri":["Magnetic Resonance Imaging machine"],
                  "nanopumps":["nanopumps"],
                  "noble gas source":["Remplissage de gaz nobles"],
                  "nucleic acid analyser":["Nucleic acid Analyzer "],
                  "plate reader":["Elisa reader","Microplate reader"],
                  "pipette":["New working pipettes","Micropipettes"],
                  "potentiostat":["Portable potentiostat"],
                  "qubit":["Qubit Flourometer"],
                  "optical microscope":["Inverted microscope","Automated microscope","Microscope",
                                        "Top of the line Nikon microscope ","Microscopio",
                                        "Live cell imaging wide field scope, auto xyz, w/ laser based autofocus"],
                  "optogenetics tools":["Equipment for optogenetics ","Wireless optogenetic stimulation"],
                  "oven":["Horno"],
                  "real time thermocycler":["Termociclador em Tempo Real"],
                  "robot to flip flies":["A robot to flip fruit flies"],
                  "screens":["Monitors"],
                  "sequencer":["next generation sequencer","State of the art DNA/RNA sequencing machine like the new PacBio"],
                  "shaker":["temperature controlled shaker for Eppendorf tubes and well-plates"],
                  "soldering":["Soldering oven","Selective solder machine"],
                  "spectrophotometer":["Espectrofotometro","spectrometer","Spectrophotometer","FTIR spectrometer "],
                  
                  "super resolution microscope":["Super resolution microscope"],
                  "thermal camera":["Cámara termográfica tipo FLIR vue proR"],
                  "thermocycler":["Thermocycler","thermocycler","Thermocycler","Thermocycler"],
                  "thermometer":["nist traceable thermometer, other calibration equipment"],
                  "tide gauge":["Tide guage"],
                  "transilluminator":["Ultraviolet Transilluminator","gel dock","Chemiluminescence imager"],
                  "transducer calibration tools":["équipements de calibration de transducteurs "],
                  "undefined":["Simulation tools","Testbench",
                               "Something more generic that provides us with greater capacity to meet demand (eg. Microscope Suites in response to the previous answer)."],
                  
                  "visual stimulator":["high speed projectors"],
                  "water bath":["Waterbath"],
                  "western blot tools":["western blot equipment"],
                  "x ray fluorescence analyser":["Xray florecence"],                  
                  }








new_equipment3 = {

                  "2 photon holographic stimulator":["Two-photon hologram set-up"],
                  "2-photon microscope":["two photon microscope"],
                  "autoclave":["Autoclave"],
                  "behavioural setup":["touch screen operant conditioning chambers for mice",
                                       "Build more customised behavioural equipment"],
                  "bioreactor":["Chemostats"],
                  "camera":["video tracking "],
                  "camera for single molecule imaging":["camera for single molecule imaging"],
                  "colony picking robot":["Colony picking robot"],
                  "colorimeter":["Small colorimeter"],
                  "centrifuge":["new low speed centrifuges","untracentrifuge"],
                  "confocal microscope":["Confocal Microscope"],
                  "computer":["Tablet","More powerful workstation","GPU based PC"],
                  "electrophysiology system":["Electrophysiology extracellular recording setup",
                                               "Electrophysiology rigs for in vivo recordings",
                                               "wire myograph"],
                  "electrophoresis system":["Gel electrophoresis equipment"],
                  "flash evaporator":["flash evaporator"],
                  "fluorescence microscope":["Fluorescence microscope"],
                  "freezer":["-80*C freezer","-90°C refrigerator"],
                  "fribilator":["Friabilator"],
                  
                  "heating block":["Heatblock"],
                  "high performance liquid chromatography":["Liquid chromatograpy-mass spectrometer"],
                  "high resolution infrared":["imagerie haute résolution infra rouge ou rayons x"],
                  "high resolution x-ray imaging":["imagerie haute résolution infra rouge ou rayons x"],
                  "in situ hydridisation setup":["fluorescent in situ hybridisation set ups"],
                  "incubator":["Estufa de cultivo"],
                  "laser":["Lasers","F2 Excimer Laser","Tunable laser"],
                  "laser cutter":["Giant laser cutter","Laser cutter"],
                  "liquid handling robot":["liquid handling robot like a qiacube","Plate spreading robot",
                                           "Robot for miniprep","automated protein purification system"],
                  "lyophilisation setup":["Freeze dryer"],
                  "mask aligner":["mask aligner for photolithography"],
                  "mri":["Diffusion Tensor Imager for humans"],
                  "multispectral camera":["Cámara multiespectral"],
                  "micromanipulator":["motorized microscope stage"],
                  "microphones":["microphones and amplifiers and filters","Hydrophone array"],
                  "nanoinjector":["Nanoinjector for Drosophila"],
                  "olfactometer":["Olfactometer"],
                  "optical microscope":["Digital microscope","Microscope"],
                  "optogenetics tools":["An optogenetics equipment for behavioural paradigms"],
                  "peristaltic pump":["bomba peristaltica para perfusion cardiaca"],
                  "ph meter":["pH meter"],
                  "plate reader":["Elisa reader"],
                  "plethysmograph":["plethysmograph"],
                  "pipette":["Pipettes"],
                  "thermocycler":["Termociclador","thermocycler","Gradient 96 well thermocycler","Thermocycler"],
                  "real time thermocycler":["Thermocycler for quantitative real time assays ",
                                            "real time thermocycler machine",
                                            "New quantitative real time monocycler "],
                  "rotary evaporator":["Rotovapor"],
                  "scale":["Digital scales"],
                  "sensors":["Advanced environmental sensors"],
                  "sequencer":["Sequencer","Minion millipore sequencing","Nanopore","Sequencer"],
                  "software defined radio box":["Adlam Pluto SDR"],
                  "spectrophotometer":["Spectrophotometer","Uv-vis spectrophotometer",
                                       "Nanospectrophotomer ","Nano-spectrophotometer"],
                  "spray dryer":["Spray drying"],
                  "stereomicroscope":["Fluorescent stereomicroscope"],
                  "shaker":["small shakers"],
                  "soldering":["Reflow oven"],
                  "undefined":["optics material","Dynamic Light scattering","Trizol",
                               "Outils spécifiques","Access to VLSI","Chromatography",
                               "équipements électroniques ","SDS-PAGE "],
                  "vacuum pump":["vacuum infiltration pump"],
                  "x ray":["Portable X-ray radiography"],
                  "x ray diffractometer":["X ray difractometer"],
                  "water cutter":["Water jet cutter"],
                  }





                

most_used1={
        "2-photon microscope":["Two-photon microscope","2 photon microscopes","Two-photon microscope",
                               "2Photon scope","2-photon microscope","Two-photon microscope"],
        "3d printer":["Impresora 3D","3D printers","3d printer","3D printers"],
        "aerial rov":["dron",],
        "Autoclave":["Autoclaves"],
        "behavioural setup":["behavioural setup","Operant chambers","Behavioral Test in animal",
                             "behaviour rooms/associated set ups","Behavioral monitoring equipment",
                             "Animal operant behavior boxes","cages for behavioral research, Custom-made treadmills for mice",
                             "open field, T-maze, elevated plus maze","automated equipment for mouse behavior ",
                             "Laberintos para analizar conducta en roedores","actimetros"],
        "binoculars":["binocular"],
        "bioreactor":["Bioreactor"],
        "buoys":["Buoys"],
        "camera":["Drop camera","Cameras","high speed videography stereovision"],
        "centrifuge":["ultracentrifuge","Centrifuges","Centrifuge",
                      "sentrifuge","centrifuges","centrifuges",
                      "Centrifuge","Centrifuge","Centrifuge"],
        "chromatograph":["Gas chromatograph","Chromatography - Akta protein purification"],
        "computer cluster":["High Performance Computing Cluster"],
        "confocal microscope":["microscopes (including confocal microscope)","confocal microscope","Confical microscopes"],
        "computer":["Computer", "Computer","PC","Computer","PC","computers","computer",
                        "Computer","Computers","Laptop","Computer","Desktop computers",
                        "Computer","Computers","Desktop pc","Computer","Computers","Ordenador",
                        "Laptop","Computadora","Laptop","computer","computer","PC",
                        "Computadores ","Laptop","computadores"],
        
        "diving gear":["Diving eguiptments"],
        "drosophila handling tools":["Drosophila tube and medium"],
        "electroencephalogram":["Eeg","poligrafo (medida des de sinais bieletricos)"],
        "electron microscope":["Electron microscope"],
        "electrophoresis equipment":["Agarose gel electrophoresis equipments "],
        "electrophysiology setup":["Electrophysiology rigs","microelectride array",
                                  " electrophysiology equipment (pipettes, head stages, slicers, stereotax frames)",
                                  "Patch clamp rig","electrophysiology","Electrophysiology rig",
                                  "Patch clamp rig","Patch Clamp Amplifier","Neuronal signal processor"],
        "elisa machine":["ELisa machines"],
        "evaporator":["Rotarg evaporator"],
        "fast protein liquid chromatography":["FPLC"],
        "flow cytometer":["flow cytometer","Cell counter"],
        "fluorescence microscope":["Fluorescence microscope systems"],
        "fourier transform infra red spectroscopy":["FTIR Spectroscopy"],
        "freezer":["Freezer"],
        "fusion oven":["fusion oven"],
        "glassware":["Verrie scientifique "],
        "high performance liquid chromatography":["Hplc","Hplc machine"],
        "incubator":["Incubator","Incubators (both shaking and static)"],
        "isotope sample preparation tools":["isotope sample preparation tools - mortar, pestle, etc."],
        "kymograph":["kymographs"],
        "laminar flow hood":["Laminar flow hood","Fluxo Laminar","Tissue culture hood"],
        "laser cutter":["Mostly shopbot, laser cutter", "laser cutter"],
        "laser":["laser","découpe laser"],
        "lathe":["Lathe"],
        "magnetic ressonance imaging system":["Magnetic Resonance Imaging Scanner", "MRI"],
        "metrology instruments":["instruments de métrologie : pied à coulisse, micromètre, comparateur, etc"],
        "microfluidics workstation":["microfluidics workstation"],
        "microscope":["microscope", "Microscopy","microscopes","Microscopy (Microscopes): 502","microscopes","microscopes",
                      "microscopies","Microscope","Microscope","Microscope","Microscope","Microcsopes","Microscopes","microscopes",
                      "Microscopes","microscopes", "microscope","microscope"],
        "microcontrollers":["microcontroller","FPGA", "AVR ATmega328", "50ME"],
        "molecular biology tools":["Pipets/ consumables/ general molecular bio stuff" ,"Molecular biology equipment",
                                   "Molecular biology tools","molecular biology (PCR, etc)","tips",  ],
        "oceanographic instruments":["Oceanographic instruments","Seabird Scientific SBE16plus V2"],
        "optical microscope":["Petrographic Microscope","Microscope",
                              "Microscopios","Microscope",
                              "Optical microscopes (older models)",
                              "microscope (light micoscope only)",
                              "Transmitted light microscope","Microscope"],
        "optogenetic system":["optogenetics equipment (lasers, LEDs, light fibers)"],
        "Oscilloscope":["Oscilloscope","Oscilloscope","Osciloscope"],
        "oven":["Oven"],
        "paper":["Post it"],
        "pippete":["Pipettes", "Pipettes","Pipettes","Pipette","Pipettes"],
        "pick and place machine":["Pick and place machine"],
        "plate reader":["ELISA reader","Uv/Visible/Fluorescence mictoplate reader",
                        " Elisa readers","Microplate reader","Plate readers",
                        "luminometer - plate reader","ELISA Machine"],
        "potentiostat":["Potentiostat"],
        "print and cut machine":["Print and Cut Machine"],
        "radiometer":["barra para medir radiación (radiómetro)"],
        "raman microscope":["Raman Microscope"],
        "real time thermocycler":["Rtpcr"],
        "scale":["Analytical balance","balance","analytical scales"],
        "separation columns":["Separation columns"],
        "server":["Computer servers","servers "],
        "spectrophotometer":["Spectrometers","UV Spectrophotometer","spectrophotometer","photospectrometer",
                             "UV-Vis Spectrometer","Spectrophotometer","Spectrophotometer",
                             "Spectrophotometer"],
        "stereo microscope":["dissection microscopes"],
        "transilluminator":["Transilluminator"],
        "thermocyclers":["PCR Thermocyclers","pcr","thermocycler","Thermocyclers","Thermal cycler",
                         "Thermocycler","PCR thermocycler","Thermocycler","Thermocycler",
                         "Thermocycler","PCR",],
        "tissue bath":["tissue/organ baths"],
        "undefined":["software for analysis of behavioral data","N/A","electrodes","dd"
                     "Characterization equipment ","Customized computer algoritms",
                     "Matlab","jibber","Optic equipment","water and soil quality"
                     "Producing electricity ( renewable et allowing mobility)","asdas",
                     "SYBR green","Trizol","Mulit-Photon","gel station","Western blot",
                     "Reagents ","Mechanical ","Green tea","Environnement de développement ","Culture media"],
        "x ray difractometer":["xrd","X ray difractometer"],
        "x ray fluorescence":["X-ray fluorescence for elementary analysis"],
        "western blot tools":["western blot facilities"],
        "zebra fish handling tools":["Equipment for zebrafish maintenance and breeding."],      
        }





espectrofotometria uv-vis, espectroscopia ft-ir
espectrofotometro, microscopio

hplc-dad, gc-ms, rmn(analise paga, feita no iqusp)
termocicladores e aparatos de eletroforese
eletrodos, celulas eletroquimicas, potenciados, agitadores magneticos
qtof
eletroencefalograma (eeg)
centrifuga, termociclador comum e tempo real, shaker
incubadores com shaker; centrifugas; hplcs
computadores workstation, cameras trap, radio colares, armadilhas de captura

raman, microscopio eletronico, plasma
computadores

dexa
microscopios, lupas, aparelho de eletroforese, centrifuga

autoclave, phmetro, agitador magnetico, camara de fluxo laminar, microondas
sequenciador, termociclador
scanner, clorofilometros
freezer -80c, pcr em tempo real, microscopio cirurgico, odyssey, hplc
citometro de fluxo
sequenciador de dna
hpsec
rmn
icp-ms, lc/ms-ms, cg/ms-ms
nao tenho laboratorio
capela; vidraria

incubadoras, phmetro, bloco digestor de dqo, espectrofotometro, centrifugas, destilador, cromatografo gasoso
microscopios eletronicos
cromatografia liquida de alta eficiencia
computador, internet, impressora, acesso a artigos cientificos, celular
espectrofotometro, balanca analitica, dbo, shaker, autoclave, fermentador

amplificadores de sinais biologicos (eletroencefalograma, eletromiograma, eletroculograma)
lupa, microscopios, material de analise molecular, gps, camera fotografica
dls, potencial zeta, saxs, calorimetria, fluorimetro

lupa e microscopio
criostato, hplc
pipeta, nanodrop, pcr, western blog, fluxo laminar, incubadora
analisador de gases; isocineticos; dexa
termociclador e fluxo laminar
camara de crescimento de plantas
drx, mev-feg, espectrometros (uv-vis, ftir, raman)
uplc, espectrometro de massa, bioquimica
nao utilizo ainda
softwares para uso em avaliacao e terapia de linguagem, de gravacao e transcricao de audios/videos, equipamentos de armazenamento de dados
misturadores
sao varios
hplc
microscopio
computadores


sequenciador de dna
incubadora de fotoperiodo
estereomicroscopio binocular, lupa com haste articulavel
termocicladores para pcr, tissue lyzer, sequenciador, q-tof, maldi tof
microscopios, pipetas de precisao
processamento histologico, imuno-histoquimica, western-blotting. necessito ms/ms
estufas incubadoras de microrganismos e termocicladores
setup the patch clamp, photon multiplier, microscopio de fluoresncencia, aparelhos de comportamento animal para registrar locomocao, consumo de liquidos etc
computadores/tablets, internet, microscopios, vidraria, reagentes, insumos (luvas, oculos, mascaras), bancadas


computadores



rmn e hrms

termocicladora
sequenciador de dna, servidor, computadores

softwer de estatistica, estufa, equipamentos de mergulho autonomo, freezer, microtomo..
termociclador

fluxo laminar, centrifugas, estufas
microscopios,  telescopios,  lupas
shaker, cromatografo, centrifuga, termociclador
termociclador
laboratorio de biologia celular / genetica
microscopio
muitos
aparatos comportamentais, espectrofotometro, termociclador
microscopio
nao me lembro
incubadora com controle de oxigenio e gas carbonico, lupas, microscopios, centrifugas, banho maria, vortex
espectrofotometro, destilador e centrifugadora.
termociclador, osmose reversa,  espectofotometro, estufa, banho maria
cg-ms ,  hplc-ms
tecnologias mais avancadas
microscopio eletronico
termociclador para pcr em tempo real; leitor de placas de elisa
dissolutor, analizador de particulas
fluorimetro, calorimetro
microscopios de varredura, transmissao, fluorescencia, tamanho de particula, autoclave, spray drier; hplc/massas
computador, software, equipamento de filmagem
hplc
citometro de fluxo, centrifugas
dsc, mev, microscopio
cromatografos




most_used2={
        "2-photon microscope":["Two-photon microscopes","Two photon microscope",
                               "2-photon microscopes","2-photon microscope",
                               "2-photon microscope"], 
                               
        "3d printer":["3D printer","imprimante 3D"],
        "aerial rov":["Drones","drone"],
        "autoclave":["Autoclave","Autoclave","Autoclave"],
        "aquatic sound tools":["underwater ultrasonic transducers, amplifiers"],
        "bat detector":["Bat detectors"],
        "behavioural setup":["Custom built behavioural equipment","Animal behaviour equipment"
                     "Animal behavioural paradigms","Behavioral Tracking","Animal behavior tracking system"],
        "bioprinter":["Bioprinter"],
        "breathing chamber":["microbiological breathing chamber"],
        "camera":["CCD camera","Imaging (Cameras): 277",
                  "underwater cameras","remote cameras","Camcorder"],
        "carbon analyser":["bench-top dissolved inorganic carbon analyzer"],
        "centrifuge":["Centrifuga","Centrifuge","centrifuges","Centrifuge","Centrifuge"],
        "cluster":["Supercomputer","Computing cluster",
                   "High performance computing cluster","High-performance computing cluster"],
        "cnc machine":["Large CNC Milling Mahcine"],
        "coffee machine":["Coffe machine"],
        "compressor":["compressor"],
        "computer":["Computer","computer","PCs","computers","Ordinateur"],
        "confocal microscope":["Confocal microscope","Confocal microscope",
                               "Confocal microscope","confocales","Confocal microscope"],
        "diving equipment":["SCUBA gear"],
        "electrical amplifiers":["electrical amplifiers"],
        "electrophysiology setup":["Patch clamp","Electrophysiology equipment",
                                   "electrophysiology rig",
                                   "Electrophysiology setup","Neurophysiology", 
                                   "electrophysiology"],
        "electrophoresis":["Electrophoresis","Electrophoresis",
                           "electrophoresis aparatus","electrophoresis"],
        "electron microscope":["transmission electronic microscope","Scanning Election Microscopy"],
        "electronic equipment":["équipements électroniques "],
        "fast protein liquid chromatography":["FPLC"],
        "flow cytometer":["Cytometro de flujo","flow cytometry"],      
        "ftir scpectrophotometer":["FTIR"],
        "fluorescence activated cell sorter":["FACS sorter","fluorescence activated cell sorter (FACS)"],
        "fluorescence microscope":["Reflected fluorescence microscope"],
        "fpga":["Xlinx Spatron"],
        "fruit fly manipulation tools":["Fly pads/dissecting scopes etc"],
        "gas flow meter":["Ventury meter"],
        "high performance liquid chromatography":["HPLC","high-pressure liquid chromatograph"],
        "immunohistochemistry tools":["Wetlabware immunohistochemistry"],
        "immunoassay tools":["Bioplex machines"],
        "incubator":["Microplate shaker/incubator","incubator","incubators"],
        "kymographs":["Kymographs"],
        "laminar flow":["laminar flow hood","Cell culture hood"],
        "laser cutter":["laser cutter"],
        "logic analyser":["logic analyser"],
        "machining tools":["machine outil (fraisage, tournage)"],
        "magnetic resonance imaging system":["MRI"],
        "magnetic susceptibility instruments":["Magnetic susceptibility instruments"],
        "microinjection system":["microinjectors"],
        "micromanipulator":["Electrode manipulators"],
        "microscope":["Microscopes","Microscopes","microscope","Microscopes","Microscope","Microscope"],
        "microtome":["microtome"],
        "molecular biology equipment":["Molecular biology equipment"],
        "multimeter":["Multimeter"],
        "oscilloscope":["Oscilloscope"],
        "pipettes":["Pipetas","Pipette","pipettes","pipettes","Pipettes"],
        "ph meter":["pH meter","pH meter"],
        "photometry systems":["photometry systems"],
        "plate reader":["Elisa Reader","Microplate reader"],
        "primate chairs":["Primate chairs"],
        "printer":["Large scale printer"],
        "real time thermocycler":["real-time thermocycler"],
        "robotic hand":["Robotic hand"],
        "rotary evaporator":["Rotary evaporator"],
        "scale":["Analytical balance"],
        "server":["server"],
        "shaker":["Microplate shaker/incubator"],
        "software defined radio":["Software Defined Radios"],
        "soldering":["Soldering station","Soldering station","solder paste screen printer"],
        "spectrophotometer":["Spectrophotometer","Spectrophotometer","Uv-VIs spectrophotometer","Raman spectroscopy"],
        "syringe pump":["Syringe pump"],
        "tablet making machine":["Tablet making machine"],
        "tags":["Tags"],
        "temperature loggers":["temperature loggers"],
        "thermocycler":["thermocycler","Thermocycler","thermocycler","PCR",
                        "various thermocycler systems","Thermocycler",
                        "Thermocycler","PCR machine","pCR equipment",
                        "Thermocycler" ,"polymerase chain reaction thermocycler",
                        "Thermocycler"],
        "transects":["Transects"],
        
        "undefined":["puzzle box","Brain function in human","imaging","Surgery","Surgery room",
                     "neuronal physiology","Recording set","Gaz","Radioactivity","sensors",
                     "Compression frames","air quallity","Sequencing"],
        "vacuum pump":["vacuum infiltration pump"],
        "x ray diffractometer":["Xray diffractometer  (XRD)"],
        "western blot equipment":["western blot equipment","Chemiluminescence Imager",
                                  "Western blot equipment"],
        "whiteboard":["whiteboard"],
        } 








most_used3={
       
        "3d printer":["imprimante 3d","3D Printer"],
        "behavioural setups":["custom behaviour rig","Apparatus to test fly motility"],
        "biosafety cabinet":["biosafety cabinets","Microbiological safety cabinet"],
        "blood pressure monitor":["Blood pressure monitors"],
        "caliper":["vernier caliper"],
        "camera":["cameras"],
        "computer":["Computer for data analysis","raspberrypis"],
        "centrifuge":["Centrifuges","centrifuges","Centrífugas",
                      "ultra centrifuges","Cold centrifuge"],
        "confocal microscope":["Confocal miceoscopes","Confocal microscope",
                               "Confocal microscope","Confocal microscopes"],
        "clean room":["Clean room"],
        "cluster":["computational cluster"],
        "cytometer":["Flow cytometer"],
        "data acquisition board":["data acquisition board"],
        "data logger":["data loggers"],
        "dissolution testing system":["Dissolution apparatus "],
        "electron microscope":["Tunneling Electron Microscopy","Electron Microscope"],
        "electrophoresis tools":["electrophoretic unit","Electrophoresis","Electrophoresis system",
                                 "Electrophoresis","Electrophoresis apparatus",
                                 "SDS-PAGE equipment"],
        "electrophysiology setup":["Patch clamp amplifier","Electrophysiology","Electrophysiology",
                                   "Neuroscience electrophysiology equipment","Electrophysiology rig"],
        "embroider":["brodeuse numérique"]
        "fourier transform spectrometer":["FTIR spectrometer"],
        "gel imager":["Gel Imager"],
        "hard drive":["Hard Drive"],
        "heat blocks":["heat blocks"],
        "high performance liquid chromotographers":["High Performance liquid chromotographers ",
                                                    "Hplc"],
        "hydrophone":["Hydrophones"],
        "incubator":["Incubadoras","Incubadora","shaking incubators","Incubators"
                     "Incubator","Incubator","Shaking incubator",
                     "CO2 incubator","Growth chambers","incubators"],
        "laminar flow":["laminar flow hood "],
        "mechanical tools":["équipements mécaniques "],
        "microcontroller":["Arduino Microcontroller",
                           "Arduino microcontrollers","PLC"],
        "microphone":["Microphone"],
        "microscope":["Microscope","microscope (bacteria)",
                      "Microscopio","Microscope","microscopes","Microscopy",
                      "Microscope"],
        "microwave oven":["Microwave oven"],
        "mixers":["Vortex mixer","stirrersand mixers"],
        "monitor":["Additional monitor"],
        "optomechanics":["Optomechanics - (mirror mounts, etc)","optical bench"],
        "oxygen monitor":["dissolved oxygen monitoring"],
        "picospritzer":["Picospritzer"],
        "plate reader":["ELISA Reader"],
        "power source":["Power source"],
        "quartz microbalance":["Qcm"],
        "real time thermocycler":["qPCR","real time themocycler machine"],
        "scale":["Scale","Weight scale"],
        "sensors":["Sensor netowrks","Various sensors for tracking fishes. ",
                   "different types of sensors"],
        "sequencer":["secuencidares","next gen sequencing",
                     "Genetic Techniques (Sequencers): 243"],
        "shakers":["Shakers"],
        "sieves":["Sieving instruments"],
        "soldering tools":["soldering stuff"],
        "spectrometer":["laser spectrometer","spectrometer",
                        "Mass spectrometer","nanodrop"],
        "stereo microscope":["sterescopes"],
        "surgery tools":["Surgical tools","stereotaxic surgery machine"],
        "thermo camera":["cámara termográfica"],
        "thermocycler":["PCR","PCR","Thermocycler","Thermocycles",
                        "thermocycler","Thermocycler","thermocycler",
                        "PCR machine","Pcr",
                        "Molecular biology-related tools such as thermocycler"],
        "thermometer":["thermometers"],
        "transcanial electrical stimulator":["Transcranial electrical stimulator"],                
        "undefined":["user/population tracking","Biomedical examination","imaging",
                     "Software for image analysis","Immuno",
                     "Imaging brains","Direct shear tests",
                     "sound recording","colorimetry","western blotting",
                     "Molecular lab equipment","Outils spécifiques "],
        "x ray fluorescence":["Xray florecence (XRF)"],
        "water quality meter":["YSI handheld water quality meter"],
        "workshop tools":["Dremel","Soldering iron","oscilloscope",
                          "network analyser","Reflow oven",
                          "soldering iron","Circuit board mill",
                          "Tubes"],
       
        }



















def load_tsv(filename):
    data = pd.read_csv(filename, delimiter="\t")
    return data

def get_header_position(data,header_string="Country"):
    position = data.filter(like=header_string)
    
    return position

def organize_by_header(data,header_string="Country"):
    header = data.filter(like=header_string)
    dummie = pd.DataFrame(index=header.values,data=data.values, columns = data.columns) 
    return dummie

filename = "test"
data = load_tsv(filename=filename)
byCountry = organize_by_header(data,header_string="Country")


# plot example with respondents from france
france = byCountry.filter(like="France",axis=0)
frGender = get_header_position(france,"Gender")
#frGender.

plt.plot(france)     


#new_equipment1["keys"]=list(new_equipment1.keys())
#new_equipment2["keys"]=list(new_equipment2.keys())

df1 = pd.DataFrame.from_dict(new_equipment1,orient="index")
df2 = pd.DataFrame.from_dict(new_equipment2,orient="index")
df3 = pd.DataFrame.from_dict(new_equipment3,orient="index")

df1.index.name = "equipment"
df2.index.name = "equipment"
df3.index.name = "equipment"
#df1 = df1.transpose()
#df1 = df1.set_index("keys")
#df1 = df1.transpose()

#df2 = df2.transpose()
#df2 = df2.set_index("keys")
#df2 = df2.transpose()

test = df1.join(df2, on="equipment",lsuffix="1",rsuffix="2")
test = test.join(df3, on="equipment",lsuffix="3",rsuffix="4")

# make the columns be increasing numbers from 0 to max num
test.columns = list(range(len(test.columns)))

# substitute nans and nones for zeros
test = test.fillna(0)
#save it as csv
test.to_csv("test.csv")

print("results are:\n")

equipment=list()
quantity=list()
for key in test.index:
    
    tempsum = np.sum(test.loc[key]!=0)
    equipment.append(key)
    quantity.append(tempsum)
    #print(key +": "+str(tempsum))

ordered = sorted(zip(quantity,equipment))
dummie1 = [x for _,x in sorted(zip(quantity,equipment))]
dummie2 = [x for x,_ in sorted(zip(quantity,equipment))]
equipment = pd.DataFrame.from_dict(equipment,orient="index")
equipment.columns.name = "quantity"
