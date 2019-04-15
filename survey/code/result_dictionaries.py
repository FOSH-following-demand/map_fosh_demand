#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 17:46:21 2019

@author: andre
"""

# due to the open entry nature of the questions related to most wanted and 
# most used equipment and the different languages used in the survey,
# we sorted them using dictionaries. These can be used to match the values to
#different entries in the CSV values, such as countries, degree, etc.

#define dictionaries to accomodate for different spellings, mistakes, etc.

new_equipment1={
          "2-photon microscope":["2-photon microscope","Two photon microscope","two photon microscope",
                                 "two photon microscope for calcium imaging","2-photon microscopes",
                                 "Two-photon microscope","two photon microscope","Microscope adequate for life imaging of cells ",
                                 "2-photon microscope"],
          "3d printer":["industry grade 3d printer","impressora 3d","impressora 3d"],
          "acoustic testing system":["Bancs de tests acoustiques "],
          "air hammer":["martelos pneumaticos,"],
          "aerial rov":["Improved drone","Drone tipo octocóptero","drone"],
          "atomic absorption spectroscopy":["Atomic absorpbtion spectrometer"],
          "aquatic rov":["Remotely operated underwater vehicle","Remote control underwater drones"],
          "auto clave":["autoclave"],
          "automated titrator":["Large replicate size automated alkalinity titrator"],
          "behavioural setup":["Operanda for operant chambers", "Animal behavior test","High throughput behavioural arena",
                              "startle chambers for prepulse inhibition on mouse"],
          "bioreactor":["bioreactors for the production of microbial biomass on pilot-scale",
                        "Bioreactor","biorreator"],
          "bioprinter":["Bioprinter"],
          "bio safety cabinet":["microbiological safety cabinet","Bio-safety cabinet"],
          "blood test tools":["mashines for blood test"],
          "buoys with sensors":["automated buoys to track conditions in real time at Flower Garden Banks","Buoys"],
          "centrifuge":["table top centrifuges","Very high speed centrifuge (50mL's at 15krcf)",
                        "ultracentrifuge","Microcentrifuge","refrigerated centrifuge",
                        "new ultracentrifuge and new rotors","Centrífuga",
                        "centrifuga refrigerada","centrifuga de eppendorf"],
          "CHNSO analyser":["analise elementar chns-o"],
          "cnc":["computer numerically controlled milling machine",
                 "machine outil à commande numérique","grand routeur CNC",
                 "Automatic CNC milling machine"],
          "confocal microscope":["Confocal microscope","confocal microscope","Spinning disk confocal micrscope",
                                 "Confocal microscope","Confocal microscope ","Live cell imaging confocal scope, w/laser based automfocys",
                                 "confocal microscope","Confocal microscope","microscopio confocal","microscopio confocal"],
          "components":["sensors","Multimeter","USB-GPIB (Electronics to communicate with old lab equipment)","Placas arduino"],
          "computer":["Mac pc","New laptop","CUDA-enabled card of compute capability >= 3.5",
                      "Graphic processing units (GPUs)","Better computers (better CPU)",
                      "um computador com capacidade para analises de bioinformatica",
                      "computadores workstation","computadores mais modernos",
                      "computadores e projetores com tecnologia mais avancada"],
          "computer cluster":["Supercomputer cores","Beowulf cluster"],
          "cytometer":["Flow cytometer",
                       "citometro de fluxo com imagem (imaging flow cytometer)",
                       "citometro de fluxo","citometria de fluxo"],
          "data acquisition board":["data acquisition board (DAQ)"],
          "Differential Scanning Calorimetry":["dsc"],
          "eeg":["poligrafo (para eeg)","eeg quantitativo com foto estimulador",
                 "amplificador (kit) brainproducts 64 canais com sistema sem fio"],
          "electron microscope":["Serial block-face scanning electron microscope",
                                 "Tunneling Electron Microscopy","ESEM","mev-feg",
                                 "microscopio eletronico","microscopio eletronico"],
          "electrophysiology system":["electrophysiology set-up","Electrophysiology rig","Patch clamp amplifier",
                                      "Multi-electrode array","electrophysiological tools","voltage clamp fluorometry",
                                      "Neuronal signal processor","electrophysiology data acquisition system with more channels",
                                      "setup de patch clamp com o sistema para medida de fotometria"],
          "electrical amplifier ":["electrical amplifier "],
          "electrophoresis unit":["electrophoresis unit","Electrophoresis"], 
          "electroporator":["Electroporator"],
          "eye tracker":["Eye tracker","Eye-trackers"],
          "filtration system":["Tanfential flow filtration device"],
          "fluorometer":["fluorometer"],
          "fluorescence imaging tools":["Fluorescence Imaging Tools"],
          "fluorescence microscope":["Fluorescence Microscope","Microscopio de fluorescencia","Fluorescence microscope",
                                     "A fluorescent microscope","Floresence Microscope","3i vivio"],
          "freezer":["Deep freezers"],
          "ftir microscope":["Microscope FTIR ","raman microsope"],
          "gas analyser":["pCO2 probe (functional)","analisador de gases","irga"],
          "gas chromatography system":["Gas chromatography system","Gas chromatograph orbitrap mass spectrometer ",
                                       "cg-ms","cg-ms","cg-ms","cromatografo"],
          "glassware":["vidrarias","vidrarias"],
          "hyperion imaging cyof":["Hyperion (imaging CyOF)"],
          "hlpc column":["coluna para hplc"],
          "high performance liquid chromatography":["uplc","UHPLC",
                                                    "A High Performance liquid Chromotography machine ",
                                                    "high-pressure liquid chromatograph with tandem mass-sepctrometry",
                                                    "hplc","hplc acoplado ao massa","hplc",
                                                    "hplc-ms","hplc-ms","hplc acoplado a massas","hplc"],
          "high speed camera":["high speed cameras"],
          "histological analysis tools":["equipamentos para analise histologica"],
          "ion trap analyser":["ion mobility ou orbitrap"],
          "iScript cDNA kit":["iScript cDNA kit"],
          "immunoabsorbent assay machine":["immunoabsorbent assay machine"],
          "imunoassay system":["Bioplex machine"],
          "incubator":["CO2 incubator","Controlled environment growth chamber",
                       "incubadora com agitacao",
                       "incubadora com controle de oxigenio e gas carbonico",
                       "estufa incubadora",
                       "camaras de crescimento de plantas"],
          "jabber":["jabber"],
          "kymograph":["kymograph"],
          "laminar flow":["capela de fluxo laminar","capela"],
          "laser cutter":["laser cutter"],
          "light Sheet microscope":["light Sheet microscope","Light Sheet Microscope (ideally a lattice light sheet)","Light sheet microscope"],
          "liquid chromatography purification station":["liquid chromatography purification station"],
          "liquid handling robot":["Liquid-handling robot","Liquid handling robot"],
          "liquid cintilator":["cintilador de fase liquida "],
          "litography machine":["Electron Beam Lithograph"],
          "machine to prepare carbon grids for electron microscopy":["Machine to prepare carbon grids for electron microscopy"],
          "mass spectrometer":["Mass spectrometer","detector de espectrometria de massas",
                               "espectometro de massa","espectrometro de massa",
                               "espectrometro de massas","ms/ms","qtof","icp-ms"],
          "meg system":["Mobile magnetoencephalography system"],
          "micromanipulator":["micromanipulator","Micromanipulator with accessories"],
          "microspectrophotometer":["microspectrophotometer (nanodrop)","Nanodrop"],
          "microtome":["freezing microtome","ultramicrotomo"],
          "microfluidics system":["microfluidics workstation"],
          "mobile phone":["celular top de linha, "],
          "molecular biology tools":["equipamentos de biologia molecular/epigenetica/gwas"],
          "mri":["an MRI at a Tesla higher than 3"],
          "optical microscope":["better microscopes","Optical imaging miniscope in vivo","Microscope",
                                "a second high power microscope","microscope",
                                "Transmitted light microscope","microscopios",
                                "microscopio","microscopios","microscopio invertido",
                                "microscopio invertido","microscopio com camera digital"],
          "oscilloscope":["Oscilloscope"],
          "oven for dissecating plants":["Big simplisia oven"],
          "petrographic microscope":["Petrographic microscope"],
          "plate reader":["Leitor de Absorbância de Microplacas de 96 poços com flexibilidade de comprimento de ondas",
                          "plate reader","leitor de placa p fluorescencia","leitor de placa de elisa"],
          "ph meter":["phmetro"],
          "pipettes":["pipetas de precisao","pipetas"],
          "potentiostat ":["Potentiostat "],
          "printer":["impressora"],
          "power supply":["POWER SUPPLY"],
          "pulsed Laser":["Pulsed Laser"],
          "pick and place machine":["Juli pick and place machine"],
          "pyrosequencer":["Pyrosequencer"],
          "qubit":["Qubit cuantificador con alta sensibilidad de RNA, DNA y proteína","qubit"],
          "respirometry":["Respirimetry equipment "],
          "rotary evaporator":["Rotary evaporator"],
          "raman spectrophotometer":["Portable Raman spectroscopy"],
          "real time thermocycler":["termociclador en tiempo real","Real Time Machine",
                                    "termociclador qpcr","rt-pcr","real time"],
          "server":["Microserver","servidor"],
          "sequencer":["adn reading machine","Oxford nanopore sequencer",
                       "Next generation Sequencing platform",
                       "sequenciador de nova geracao", "sequenciador de dna",
                       "sequenciador illumina","mais sequenciadores e quantificadores",
                       "sequenciador"], 
          "spectrophotometer":["Infrared Spectrophotometer","espectrofotometro",
                               "espectrofotometro","espectrofotometro",
                               "espectrofotometro de absorcao atomica"],
          
          "satelitte":["geostationary satellite with multispectral radiometers"],
          "shaker":["shaker"],
          "single cell sequencer":["Máquina de secuenciación de single cell","10X single cell sequencing machine"],
          "screen":["A better screen"],
          "stereomicroscope":["estereomicroscopios com tela","lupas"],
          "stereotaxic":["semi-automated stereotaxic"],
          "super resolution microscope":["Ultra resolution microscope","Super resolution microscope"],
          "tablet press machine":["Tablet making machine"],
          "telescope":["telescopio"],
          "thermal camera":["infrared and thermal cameras"],
          "thermocycler":["thermocycler","Thermocycler","Thermocycler", "Thermal Cycler",
                          "A thermocycler","Thermocycler","Thermocycler",
                          "Thermocycler","thermocycler","termocicladores","termociclador"],
          "tilt machine":["Tilt machine"],
          "turbidostat":["morbidostat"],
          "tissue homogenizer":["tissue homogenizer"],
          "tissue/organ bath":["tissue/organ bath"],
          "transilluminator":["Ultraviolet Transilluminator","Transilluminator"],
          "undefined":["Something unique that would allow us to be the national/international hub for leading research in a specific area",
                       "ACTA","N/A","dasdsa","2C-I","uma maquina propria"
                       "MRI processing software","Reagents ","nn consigo definir apenas um"
                       "components to build the kits described above","NA",
                       "nao sei responder","os ja citados","nao sei","entre outros",
                       "montar um laboratorio adequado. faltam praticamente todos os equipamentos por aqui",
                       "a questao muitas vezes nao e o equipamento mas sim os reagentes",
                       "softwares de terapia e avaliacao de linguagem","ilha de edicao",
                       "todos para um laboratorio de qualidade para graduacao em biologia e quimica fisica...",
                       "laboratorio completo para ensino fundamental i e ii, com material (experimentoteca e laboratorial) para ensino de quimica, fisica e biologia",
                       "inbody","equipamentos para substituir o destilador.",
                       "osmose reversa ","refletor; ","rmn"],
          "universal materials testing machine":["Universal Materials Testing Machine","Universal Testing Machine"],
          "visual stimulator":["A high-resolution, flexible digital screen to project visual stimulation",
                               "a decent light stimulation setup"],
          "x ray diffractometer":["Single Crystal X-ray Diffractometer","Xray diffractometer"],
          "western blot tools":["Western Blotting equipments"],
          "whiteboard":["more whiteboards"],

          }










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
                        "Computadores ","Laptop","computadores",
                        "computadores workstation","computadores",
                        "computadores","computador","computadores",
                        "computadores","computador","computadores/tablets"],
        
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
        "high performance liquid chromatography":["Hplc","Hplc machine",
                                                  "hplc-dad","hplc","hplc",
                                                  "hplc","hplc-ms",
                                                  "hplc/massas","hplc",
                                                  "cromatografia liquida de alta eficiencia"],
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
        "microscope":["microscope", "Microscopy","microscopes",
                      "Microscopy (Microscopes): 502","microscopes","microscopes",
                      "microscopies","Microscope","Microscope","Microscope",
                      "Microscope","Microcsopes","Microscopes","microscopes",
                      "Microscopes","microscopes", "microscope","microscope",
                      "microscopio","microscopio","microscopio","microscopio",
                      "microscopio","microscopio","microscopios","microscopios",
                      "microscopios","microscopios","microscopios","microscopios"],
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
                         "Thermocycler","PCR","termocicladora",
                         "termocicladores","termociclador","termociclador",
                         "termociclador comum e tempo real", "termociclador",
                         "termociclador","termociclador","termociclador",
                         "termociclador","termocicladores para pcr", 
                         "termocicladores","pcr"],
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


"""

"espectrofotometria uv-vis", "espectroscopia ft-ir","espectrofotometro","espectrofotometro","espectrofotometro","espectrofotometro","espectrofotometro","espectofotometro","espectrometros (uv-vis, ftir, raman)"
"microscopio de fluoresncencia"
"gc-ms", 
"rmn(analise paga, feita no iqusp)"
"aparatos de eletroforese"
"eletrodos", 
"celulas eletroquimicas", 
"potenciados", 
"agitadores magneticos"
"qtof"
"eletroencefalograma (eeg)"
"centrifugas"; ,"centrifuga, ","centrifuga","centrifugas","centrifugas","centrifugas","centrifugadora","centrifugas", "centrifuga", 
"termociclador comum e tempo real", "termociclador para pcr em tempo real","pcr em tempo real"
"shaker"
"incubadores com shaker"; 
"hplcs"
"cameras trap"
"radio colares"
"armadilhas de captura"
"raman"
"microscopio eletronico","mev","microscopio eletronico","microscopios eletronicos","mev-feg"
"plasma"
"dexa"
"lupas"
"aparelho de eletroforese"
"phmetro"
"agitador magnetico"
"camara de fluxo laminar"
"microondas"
"sequenciador" ,"sequenciador de dna"
"scanner", 
"clorofilometros"
"freezer -80c", 
"microscopio cirurgico"
"odyssey"
"citometro de fluxo"
"hpsec"
"rmn"
"icp-ms", "lc/ms-ms", "cg/ms-ms"
"nao tenho laboratorio"
"capela" 
"vidraria","vidraria"
"phmetro"
"bloco digestor de dqo"
"destilador" 
"cromatografo gasoso"
"internet"
"impressora"
"acesso a artigos cientificos"
"celular"
"balanca analitica"
"dbo"
"shaker"
"autoclave","autoclave","autoclave"
"fermentador"
"amplificadores de sinais biologicos (eletroencefalograma, eletromiograma, eletroculograma)"
"lupa"
"material de analise molecular"
"gps"
"camera fotografica"
"dls"
"potencial zeta"
"saxs"
"calorimetria"
"fluorimetro"
"lupa"
"criostato" 
"pipeta"
"nanodrop"
"western blog"
"fluxo laminar"
"analisador de gases"
"isocineticos"
"dexa"
"fluxo laminar"
"camara de crescimento de plantas"
"drx"
"uplc"
"espectrometro de massa"
"bioquimica"

"misturadores"
"sao varios"
"sequenciador de dna","sequenciador","sequenciador de dna"
"incubadora de fotoperiodo","estufas incubadoras de microrganismos" ,"incubadoras","incubadora","incubadora com controle de oxigenio e gas carbonico", 
"estereomicroscopio binocular", 
"lupa com haste articulavel"
"tissue lyzer", 
"q-tof", 
"maldi tof",
"pipetas de precisao"
"processamento histologico",
"imuno-histoquimica",
"western-blotting".
"necessito ms/ms"
"setup the patch clamp"
"photon multiplier"
"aparelhos de comportamento animal para registrar locomocao, consumo de liquidos etc"
"internet"
"reagentes"
"insumos (luvas, oculos, mascaras)"
"bancadas"
"rmn"
"hrms"
"servidor" 
"softwer de estatistica","nao utilizo ainda","softwares para uso em avaliacao e terapia de linguagem, de gravacao e transcricao de audios/videos, equipamentos de armazenamento de dados"
"estufa",
"equipamentos de mergulho autonomo", 
"freezer", 
"microtomo"
"fluxo laminar", 
"estufas"  
"telescopios",  
"lupas"
"shaker", "cromatografo", 
"laboratorio de biologia celular / genetica"
"muitos"
"aparatos comportamentais", 
"nao me lembro"

"lupas", 
"banho maria", 
"vortex"
"destilador"
"osmose reversa", , 
"estufa", 
"banho maria"
"cg-ms" ,  
"tecnologias mais avancadas"
"leitor de placas de elisa"
dissolutor, 
analizador de particulas
fluorimetro, 
calorimetro
"microscopios de varredura", 
"transmissao", 
"fluorescencia", 
"tamanho de particula", , 
"spray drier" 
 software, equipamento de filmagem
citometro de fluxo, 
dsc, 
cromatografos


"""

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
        "embroider":["brodeuse numérique"],
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